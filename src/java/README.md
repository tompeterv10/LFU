# Java Take Home Question

Welcome to the Docugami Java take home question! We also have this same question available in C# and Python, so please select the language the you are most comfortable with.

## Problem Outline and Requirements
1. Implement a disk backed queue. As a refresher, a Queue is a FIFO data structure with O(1) insert and remove operations.

1. The queue will implement the `SimpleQueue` interface and inherit from the `BaseQueue` abstract class. Please do not modify anything in the `*.base` package.

1. The queue constructor takes an integer when it is constructed. That integer dictates the maximum number of queue nodes that can be kept in memory at any given time. All other nodes in the queue must be written to disk.

1. The implementation should not use any of the built in Java collection classes (e.g. ArrayList, LinkedList, etc.) as part of the queue implementation.

1. Place your implemenation in the `*.implementation` package. We believe that the project contains all of the required references to implement this solution. If you would like to add an external reference, please ask!

1. There is a traditional JUnit test class in the `*.tests* package. Please implement any unit tests that you feel would be helpful to test your code.

1. The code will be evaluated on the following criteria:
    1. **Correctness.** We have a private set of unit tests that we will run on the code to evaluate this.
    1. **Robustness.** Is the code "production" quality?
    1. **Readability and Organization.** Is your code easy to read? Could another developer easily make changes to your code?
    1. **Unit Tests.** Did you write a thorough set of unit tests for your queue? Did you correctly handle all of the corner cases? Maybe you thought of some tests that we missed! :)

1. Please do not use external resources to help with the algorithmic aspects of this problem. We really want to see how you think and code. That said, if you have basic questions on the functionality of Java libraries, feel free to find answers on the internet. To clarify, here is a good and bad example of when to use external resources:
    - **Good:** Searching Stack Overflow to understand a nuance of how the Java File APIs work.
    - **Bad:** Searching Stack Overflow for how to implement a queue.

1. Please provide a README.md with your submission to describe:
    - The design choices you made and why you made them.
    - Any external resources you used for help.
    - The amount of time that it took you to write the code and test cases.

1. **Have fun!** If you have any questions, feel stuck or have any concerns, please email enghiring@docugami.com.

## Required Tools

1. Install Java 8+.

1. The IDE of your choice. (This is a Maven project that was prepared in Eclipse, but IntelliJ should work ok too)

