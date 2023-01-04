class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first,second,num;
        bool hastwo = false;
        first = nums[0];
        for (int i=1;i<nums.size();i++){
            num = nums[i];
            if (num <= first){
                first  = num;
        }else{
                if(hastwo){
                    

                     if (num<=second){
                        second = num;
             
                    }else{
                        return true;
                    }
                    
                }else{
                    second = num;
                    hastwo = true;
                }
            }
        }
        return  false;
    }
};