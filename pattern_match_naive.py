
import copy
def dfs(p, s, mapping):

	print mapping
	if len(p)==0 and len(s)==0:
		return True

	key = p[0]

	if key in mapping:
		mapped = mapping[key]
		if s[0]==mapped:
			return dfs(p[1:], s[1:], mapping)
		else:
			return False

	else:
		if len(p)==1:
			return True

		guess = s[0]
		guess_mapping = copy.copy(mapping)
		guess_mapping[key] = guess
		
		if dfs(p[1:], s[1:], guess_mapping):
			return True


	return False







if __name__ == "__main__":
    print dfs("abab", ["red","blue","red","blue"], {})
    #print patternMatches("aaaa", "asdasdasdasd")
    #print patternMatches("aabb", "xyzabcxzyabc")