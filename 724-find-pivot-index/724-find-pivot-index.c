int pivotIndex(int *nums, int numsSize)
{

    int totalSum = 0;
    for (int i = 0; i < numsSize; i++)
        totalSum += nums[i];

    for (int i = 0, leftSum = 0; i < numsSize; i++)
    {
        if (i>0)
            leftSum += nums[i - 1];
        if (leftSum * 2 == totalSum - nums[i])
            return i;
    }
    return -1;
}