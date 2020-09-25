package DijkstraMe;

import java.util.List;

public class LeetcodeMain {
    public static void main(String[] args) {
        Leetcode leetcode = new Leetcode();
        int[][] flights={{0,1,2},{0,2,2},{0,3,2},{1,8,8},{2,4,2},{3,8,7},{4,8,2}};
        int ans = leetcode.findCheapestPrice(6,flights,0,8,1);
        System.out.println(ans);
    }
}
