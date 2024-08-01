#include <iostream>
#include <stdlib.h>

using namespace std;

class Solution {
public:
    int countSeniors(vector<string>& details) {
        
        int sol=0;
        for(string& x:details){
            int age = stoi(x.substr(11, 2));
            if(age>60){
                sol++;
            }
            
        }
        
        return sol;
        
    }
};