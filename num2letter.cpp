
class Solution {
public:
    vector<string> wordBreak(string s, unordered_set<string>& wordDict) {
        string result;
        vector<string> solutions;
        vector<bool> possible(s.size()+1, true);
        dfs(0, s, wordDict, result, solutions, possible);
        return solutions;
    }

    void dfs(int start, string& s, unordered_set<string> &dict, string& result, vector<string>& solutions, vector<bool>& possible){
        if(start==s.size()){
            solutions.push_back(result.substr(0, result.size()-1));
            return;
        }

        for(int i=start; i<s.size(); ++i){
            string piece = s.substr(start, i - start + 1);
            if (dict.count(piece) ==1 && possible[i+1]) // [0, start-1]ok  [start,i]ok ?[i+1, end]
            {
                 result.append(piece).append(" ");
                 int beforeChange= solutions.size();
                 dfs(i + 1, s, dict, result, solutions, possible);
                 if(solutions.size() == beforeChange) // if no solution, set the possible to false
                     possible[i+1] = false;
                 result.resize(result.size() - piece.size()-1);
             }
        }
    }
};


// letterCombinations
vector<string> letterCombinations(string digits){

    string translations[] = {"", " ", "abc", "def", "ghi"};
    vector<string> set;
    string seq;
    dfs(translations, digits, 0, seq, set);
    return set;

}

void dfs(string translations[], string &digits, int deep, string &result, vector<string> &set){
    if(deep==digits.size()){
        set.push_back(result);
        return;
    }
    int curDig = digits[deep] - '0';
    for(int i=0; i<translations[curDig].size(); i++){
        result.push_back(translations[curDig][i]);
        dfs(translations, digits, deep+1, result, set);
        result.resize(result.size()-1);
    }

}

如果可以拼出multiple words的组合。那也输出这些组合。面试官说单词的长度至少为3，然后电话号码长度为7。所以其实只有3种组合方法。改一改就好了。

// letterCombinations
vector<string> letterCombinations(string digits){

    string translations[] = {"", " ", "abc", "def", "ghi"};
    vector<string> set;
    string seq;
    dfs(translations, digits, 0, seq, set);
    return set;

}

void dfs(string translations[], string &digits, int deep, string &result, vector<string> &set){
    if(deep==digits.size()){
        if(set.count(result)==1){
            set.push_back(result);
            return;
        }
    }

    int curDig = digits[deep] - '0';
    for(int i=0; i<translations[curDig].size(); i++){
        result.push_back(translations[curDig][i]);
        dfs(translations, digits, deep+1, result, set);
        result.resize(result.size()-1);
    }


}

    void dfs(int start, string& s, unordered_set<string> &dict, string& result, vector<string>& solutions, vector<bool>& possible){
        if(start==s.size()){
            solutions.push_back(result.substr(0, result.size()-1));
            return;
        }

        for(int i=start; i<s.size(); ++i){
            string piece = result+translations[i];
            if (dict.count(piece) ==1) // [0, start-1]ok  [start,i]ok ?[i+1, end]
            {
                 result.append(piece).append(" ");
                 dfs(i + 1, s, dict, result, solutions, possible);
                 result.resize(result.size() - piece.size()-1);
             }
        }
    }



