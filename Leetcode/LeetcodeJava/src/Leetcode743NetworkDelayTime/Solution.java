package Leetcode743NetworkDelayTime;

import java.util.*;

//network delay time
public class Solution {
    Queue<int[]> pq = new PriorityQueue<>((a, b)->a[0]-b[0]);
    Boolean[] visited;
    int[] time;
    int N;
    int src;
    final int LARGENUMBER = 1000006;
    Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
    public int networkDelayTime(int[][] times, int N, int K) {//K is source Node
        this.visited = new Boolean[N];
        Arrays.fill(visited, false);
        this.N = N;
        this.src = K-1;//converted to 0 based indexing
        this.time = new int[N];
        for(int i=0;i<N;i++){
            map.put(i,new HashMap<>());
            time[i] =LARGENUMBER;
        }
        for(int[] entry:times){
            int node1No = entry[0]-1;//0 based indexing
            int node2No = entry[1]-1;
            int time = entry[2];
            map.get(node1No).put(node2No, time);
        }
        time[src] = 0;
        pq.add(new int[] {0,src});
        int res = -1;
        while(!pq.isEmpty()){
            int[] currentNode = pq.poll();
            int currentNodeNo = currentNode[1];
            int currentNodetime = currentNode[0];
            if(visited[currentNodeNo]) continue;
            visited[currentNodeNo] = true;
            N--;
            res = currentNodetime;
            if(map.containsKey(currentNodeNo)) {
                for (int dst : map.get(currentNodeNo).keySet()) {
                    time[dst] = Math.min(time[dst], time[currentNodeNo] + map.get(currentNodeNo).get(dst));
                    pq.add(new int[]{time[dst], dst});
                }
            }

        }
        return N == 0 ? res : -1;
    }
}
