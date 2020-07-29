// Copyright (c) Docugami, Inc. All rights reserved.

namespace TakeHome.Implementation
{
    using TakeHome.Base;

    public class Queue<T> : BaseQueue<T>
    {
        public Queue(int maxInMemory) : base(maxInMemory)
        {
        }

        public override int Count => throw new System.NotImplementedException();

        public override int InMemoryCount => throw new System.NotImplementedException();

        public override int OnDiskCount => throw new System.NotImplementedException();

        public override T Dequeue()
        {
            throw new System.NotImplementedException();
        }

        public override void Enqueue(T item)
        {
            throw new System.NotImplementedException();
        }

        public override T Peek()
        {
            throw new System.NotImplementedException();
        }
    }
}