package Dijkstra;


import java.util.ArrayList;
import java.util.List;

public class DijkstraTest2 {
    public static void main(String arg[])
    {
        int V = 5;
        int source = 3;

        // Adjacency list representation of the
        // connected edges
        List<List<Node>> adj = new ArrayList<List<Node> >();

        // Initialize list for every node
        for (int i = 0; i < V; i++) {
            List<Node> item = new ArrayList<Node>();
            adj.add(item);
        }

        // Inputs for the DPQ graph
        adj.get(2).add(new Node(1, 9));
        adj.get(2).add(new Node(0, 6));
        adj.get(2).add(new Node(3, 5));
        adj.get(2).add(new Node(4, 3));

        adj.get(0).add(new Node(1, 2));
        adj.get(0).add(new Node(3, 4));

        adj.get(3).add(new Node(4, 4));

        // Calculate the single source shortest path
        DPQ dpq = new DPQ(V);
        dpq.dijkstra(adj, source);

        // Print the shortest path to all the nodes
        // from the source node
        System.out.println("The shorted path from node :");
        for (int i = 0; i < dpq.dist.length; i++)
            System.out.println(source + " to " + i + " is "
                    + dpq.dist[i]);
    }
}
