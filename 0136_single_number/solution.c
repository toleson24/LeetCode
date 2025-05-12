#include <stdlib.h>

int singleNumber(int* nums, int numsSize) {
    int single = 0;
    for (int i = 0; i < numsSize; i++) {
        single = single ^ nums[i];
    }

    return single;
}