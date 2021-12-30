
int majorityElement(int* nums, int numsSize){
    int me = nums[0];
    int count  = 1;
    int i;
    for (i=0;i<numsSize;i++){
        if (me==nums[i]){
            count++;
        } else{
            count--;
            if(count==0){
                me=nums[i];
                count=1;
            }
        }
    }
    return me;

}