#include <numeric>

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (accumulate(gas.begin(),gas.end(),0) < accumulate(cost.begin(),cost.end(),0)) return -1;
    int index = 0;
    int currGas = 0;
    for (int i = 0; i<gas.size() ; i++){
        currGas += gas[i] - cost[i];
        if (currGas < 0 ){
            index = i+1;
            currGas = 0;
        }
    }
    return index;
    }
};