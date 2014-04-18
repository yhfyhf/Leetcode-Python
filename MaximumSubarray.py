"""
For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = max_sum = A[0]
        if len(A) > 1:
            for i in range(1, len(A)):
                sum = A[i] if sum<0 else sum+A[i]
                max_sum = sum if sum>max_sum else max_sum
        return max_sum