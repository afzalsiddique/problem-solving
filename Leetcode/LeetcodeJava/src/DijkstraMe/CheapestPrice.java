//package DijkstraMe;
//
//import java.util.*;
//
//public class NetworkTimeDelay.Solution {
//    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
//        List<List<Pair>> graph = buildGraph(n, flights);
//        Queue<City> pq = new PriorityQueue<>((a, b) -> a.distanceFromSource - b.distanceFromSource);
//        pq.add(new City(src, 0, 0));
//        while (!pq.isEmpty()) {
//            City currentCity = pq.poll();
//
//            if (currentCity.city == dst)
//                return currentCity.distanceFromSource;
//
//            if (currentCity.stopsFromSource < K) {
//                List<Pair> neighbors = graph.get(currentCity.city);
//                for (Pair neighbor : neighbors)
//                    pq.add(new City(neighbor.city, currentCity.stopsFromSource + 1, currentCity.distanceFromSource + neighbor.cost));
//
//
//            }
//            return -1;
//        }
//    }
//    public List<List<Pair>> buildGraph(int n, int[][] flights){
//        List<List<Pair>> graph = new ArrayList<>();
//        for(int i=0;i<n;i++)
//            graph.add(i, new ArrayList<>());
//        for(int[] list: flights){
//            int sourceCity = list[0];
//            int destinationCity = list[1];
//            int cost = list[2];
//            graph.get(sourceCity).add(new Pair(destinationCity,cost));
//        }
//        return graph;
//    }
//}
//class City {
//    int city;
//    int stopsFromSource;
//    int distanceFromSource;
//
//    public City(int city, int stopsFromSource, int distanceFromSource) {
//        this.city = city;
//        this.stopsFromSource = stopsFromSource;
//        this.distanceFromSource = distanceFromSource;
//    }
//}
//
//class Pair{
//    int city;
//    int cost;
//
//    public Pair(int city, int cost) {
//        this.city = city;
//        this.cost = cost;
//    }
//}
