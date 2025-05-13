#include <stdlib.h>

// runtime: 100.00%, memory: 32.09%
int singleNumber(int* nums, int numsSize) {
    int single = 0;
    for (int i = 0; i < numsSize; i++) {
        single ^= nums[i];
    }

    return single;
}