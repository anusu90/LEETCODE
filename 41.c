
int firstMissingPositive(int* nums, int numsSize){
    int i=0;
    int v;
    for(i=0;i<numsSize;i++){
        if(nums[i]<=0){
            nums[i]=numsSize+1;
        }
    }
    for(i=0;i<numsSize;i++){
        v = nums[i];
        if(v<0){
            v=v*-1;
        }
        if(v<=numsSize){
            if(nums[v-1]>0){
                nums[v-1] = nums[v-1] * -1;
            }
        }
    }
    for(i=0;i<numsSize;i++){
        
        if(nums[i]>0){
            return i+1;
        }
    }
    return numsSize+1;
}