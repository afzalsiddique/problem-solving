package Leetcode743NetworkDelayTime;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void test1(){
        int [][] times = {{2,1,1},{2,3,1},{3,4,1}};
        int N = 4;
        int K = 2;
        Solution solution= new Solution();
        int actual = solution.networkDelayTime(times, N, K);
        int expected = 2;
        Assert.assertEquals(expected,actual);
    }
}
