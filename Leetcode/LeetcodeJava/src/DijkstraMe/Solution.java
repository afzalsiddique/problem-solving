//package DijkstraMe;
//
//import java.util.ArrayList;
//import java.util.List;
//
//public class NetworkTimeDelay.Solution {
//    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
//        DPQ dpq = new DPQ(n);
//        List<List<Node>> adj = new ArrayList<>();
//        for(int i=0;i<n;i++){
//            List<Node> list = new ArrayList();
//            adj.add(list);
//        }
//        for(int[] list:flights){
//            int firstNode = list[0];
//            int secondNode = list[1];
//            int cost = list[2];
//            adj.get(firstNode).add(new Node(secondNode,cost));
//        }
//        dpq.dijkstra(adj,src,K);
//
//        int price = Integer.MAX_VALUE;
//        for(int i=0;i<dpq.dist.length;i++){
//            if(i==dst && price > dpq.dist[i] && dpq.pathLength.get(i)<=K && dpq.pathLength.get(i)>0)
//                price = dpq.dist[i];
//        }
//        if(price == Integer.MAX_VALUE)
//            return -1;
//        else
//            return price;
//    }
//}
