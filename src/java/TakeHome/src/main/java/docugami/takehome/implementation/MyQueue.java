// Copyright (c) Docugami, Inc. All rights reserved.

package docugami.takehome.implementation;

import docugami.takehome.base.BaseQueue;

public class MyQueue<T> extends BaseQueue<T> {

    public MyQueue(Class<T> type, int maxInMemory) {
        super(maxInMemory);
    }

    public int getCount() {
        // TODO Auto-generated method stub
        return 0;
    }

    public void enqueue(T item) throws IllegalStateException {
        // TODO Auto-generated method stub
        
    }

    public T dequeue() throws IllegalStateException {
        // TODO Auto-generated method stub
        return null;
    }

    public T peek() throws IllegalStateException {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public int getInMemoryCount() {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public int getOnDiskCount() {
        // TODO Auto-generated method stub
        return 0;
    }
}

