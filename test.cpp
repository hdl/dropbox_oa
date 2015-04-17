#include <iostream>
#include <vector>
#include <stdio.h>


using namespace std;
int main(){


    vector<int> a;
    a.push_back(1);
    a.push_back(2);
    auto it= a.end();
    a.push_back(3);
    cout << *prev(a.end());
}
