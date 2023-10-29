class Solution {
public:
    int kthGrammar(int n, int k) {
        if(n==1){
            return 0;
        }
        int parent = kthGrammar(n-1,k/2+k%2);
        if ((parent==1 && k%2!=0)||(parent==0 && k%2==0)){
            return 1;
        }
        return 0;
        
    }
};