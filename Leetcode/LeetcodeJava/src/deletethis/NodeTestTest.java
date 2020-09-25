package deletethis;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

import static org.junit.Assert.*;

public class NodeTestTest {
    @Test
    public void nodeTest1(){
        Node node = new Node(10,12);
        int expected = 10;
        int actual = node.a;
        Assert.assertEquals(actual,expected);
    }

}