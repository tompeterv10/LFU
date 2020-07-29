// Copyright (c) Docugami, Inc. All rights reserved.

namespace TakeHome.Implementation.Tests
{
    using TakeHome.Implementation;
    using Microsoft.VisualStudio.TestTools.UnitTesting;

    [TestClass]
    public class QueueTests
    {

        [TestMethod]
        public void TestPeek()
        {
            var queue = new Queue<int>(10);

            queue.Enqueue(1);
            Assert.IsTrue(queue.Peek() == 1);
        }
    }
}
