//package DijkstraMe;
//
//import java.util.Comparator;
//
//class Node implements Comparator<Node> {
//    public int node;
//    public int cost;
//
//    public Node()
//    {
//    }
//
//    public Node(int node, int cost)
//    {
//        this.node = node;
//        this.cost = cost;
//    }
//
//    @Override
//    public int compare(Node node1, Node node2)
//    {
//        if (node1.cost < node2.cost)
//            return -1;
//        if (node1.cost > node2.cost)
//            return 1;
//        return 0;
//    }
//}