package deletethis;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void Test1(){
        Solution solution = new Solution();
        int[] stones = new int[] {5,3,4,5};
        boolean actual = solution.stoneGame(stones);
        Assert.assertEquals(true, actual);
    }

}