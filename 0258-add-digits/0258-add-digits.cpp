using namespace std;
class Solution {
public:
    
    int recur(int n){
        cout<<n<<endl;
        int x = n/10;
        if(x==0){
            return n;
        }
        int i=0;
        while(n>0){
        i+=(n%10);
        n=n/10;
        }
        return recur(i);
    }
    
    int addDigits(int num) {
        return recur(num);
    }
};