package com.jqc.dp;

/**
 * 最长上升子序列
 * @author appbanana
 * @date 2019/12/1
 */
public class LIS {
    public static void main(String[] args) {
        System.out.println("lengthOfLIS= " + lengthOfLIS(new int[]{10, 2, 2, 5, 1, 7, 101, 18}));
    }

    /**
     * 动态规划求最长上升子序列  时间复杂度O(n^2) 空间复杂度O(n)
     * @param nums
     * @return
     */
    static int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int[] dp = new int[nums.length];
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] <= nums[j]) continue;
                dp[i] = Math.max(dp[j] + 1, dp[i]);
            }
            max = Math.max(dp[i], max);
        }
        return max;
    }
}
