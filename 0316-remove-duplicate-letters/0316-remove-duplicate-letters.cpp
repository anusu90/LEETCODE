#include <unordered_map>
#include <vector>
#include <set>
#include <string>
using namespace std;
class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> stack;
        unordered_map<char,int> count_map = {};
        set<char> used ={};
        for (char c:s){
            if(count_map.count(c)==0){
                count_map[c]=1;
            }else{
                count_map[c]++;
            }
        }
        for (char c:s){
            count_map[c]--;
            if(used.count(c)==0){
                while(stack.size()>0 && count_map[stack.back()]>0 && c<stack.back()){
                    char popped = stack.back();
                    used.erase(popped);
                    stack.pop_back();
                }
                stack.push_back(c);
                used.insert(c);
            }
            
        }
        string st="";
        for(char x:stack){
            st = st+x;
        }
        return st;
        
    }
};