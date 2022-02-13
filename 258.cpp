class Solution {
public:
    int s(int num){
        int q = 0;
        while(num>0){
            q+=num%10;
            num = num/10;
        }
        return q;
    }
    int addDigits(int num) {
        if (num/10<1){
            return num;
        }
        return addDigits(s(num));
    }
};