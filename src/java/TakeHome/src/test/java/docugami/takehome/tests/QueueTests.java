// Copyright (c) Docugami, Inc. All rights reserved.
package docugami.takehome.tests;

import org.junit.Assert;
import org.junit.Test;
import docugami.takehome.implementation.MyQueue;
public class QueueTests {

    public QueueTests() {
        super();
    }

    @Test
    public void testPeek() {
        MyQueue<Integer> queue = new MyQueue<Integer>(Integer.class, 5);
        queue.enqueue(5);
        Assert.assertEquals((Integer)5, queue.peek());
    }
}
