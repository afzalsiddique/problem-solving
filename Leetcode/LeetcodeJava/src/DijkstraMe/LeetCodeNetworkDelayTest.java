package DijkstraMe;

public class LeetCodeNetworkDelayTest {
    public static void main(String[] args) {
        LeetcodeNetworkDelayTime solution = new LeetcodeNetworkDelayTime();
        int[][] times = {{2,1,1},{2,3,1},{3,4,1}};
        int N = 4;
        int K = 2;
        System.out.println(solution.networkDelayTime(times,N,K));
    }
}
