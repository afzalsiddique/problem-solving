package DijkstraMe;

import java.util.*;

public class LeetcodeNetworkDelayTime {
    List<List<Node>> graph;
    Set<Integer> settled;
    Integer[] time; //actually distance in dijkstra
    Queue<Node> pq;
    int src;
    public int networkDelayTime(int[][] times, int N, int K) {//K is source Node
        this.src = K-1;
        this.graph = buildGraph(N,times);
        this.pq = new PriorityQueue(N,new Node());
        this.settled = new HashSet<>();
        this.time = new Integer[N];
        for(int i=0;i<N;i++)
            time[i] = Integer.MAX_VALUE;

        time[src] = 0;

        pq.add(new Node(src, 0));

        while(!pq.isEmpty()){
            Node currentNode = pq.poll();
            settled.add(currentNode.nodeNo);
            e_neighbor(currentNode.nodeNo);
        }
        int max=-1;
        for(int i=0;i<N;i++){
            if(max<time[i])
                max = time[i];
        }
        if(max==Integer.MAX_VALUE)
            return -1;
        return max;
    }
    private void e_neighbor(int nodeNo){
        for(Node neighbor:graph.get(nodeNo)){
            int neighborNodeNo = neighbor.nodeNo;
            int neighborTime = neighbor.time;
            if(!settled.contains(neighborNodeNo)){
                int newTime = time[nodeNo] + neighbor.time;
                if(newTime<time[neighborNodeNo])
                    time[neighborNodeNo] = newTime;

                pq.add(new Node(neighborNodeNo,time[neighborNodeNo]));
            }


        }
    }
    public List<List<Node>> buildGraph(int N, int[][] times){
        List<List<Node>> graph = new ArrayList<>();
        for(int i=0;i<N;i++)
            graph.add(i, new ArrayList<>());
        for(int[] list:times){
            int sourceNode = list[0]-1;//converting 1 based indexing to 0 based indexing
            int nodeNo = list[1]-1;//converting 1 based indexing to 0 based indexing
            int time = list[2];
            graph.get(sourceNode).add(new Node(nodeNo, time));
        }
        return graph;
    }
}

class Node implements Comparator<Node> {
    int nodeNo;
    int time;

    public Node(){

    }
    public Node(int nodeNo, int time) {
        this.nodeNo = nodeNo;
        this.time = time;
    }

    @Override
    public int compare(Node node1, Node node2) {
        if(node1.time < node2.time)
            return -1;
        if(node1.time > node2.time)
            return 1;
        return 0;
    }
}
