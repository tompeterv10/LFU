# C# Take Home Question

Welcome to the Docugami C# take home question! We also have this same question available in Python and Java, so please select the language the you are most comfortable with.

## Problem Outline and Requirements
1. Implement a disk backed queue. As a refresher, a Queue is a FIFO data structure with O(1) insert and remove operations.

1. The queue will implement the IQueue interface and inherit from the BaseQueue abstract class. Please do not modify anything in the Base directory.

1. The queue constructor takes an integer when it is constructed. That integer dictates the maximum number of queue nodes that can be kept in memory at any given time. All other nodes in the queue must be written to disk.

1. The implmentation should not use any of the built in C# collection classes (e.g. List, etc.) as part of the queue implementation.

1. Place your implemenation in the Implementation directory. We believe that Implementation.csproj contains all of the required references to implement this solution. If you would like to add another nuget package to the solution, please ask!

1. There is a test project in the Implementation.Tests directory. Please implement any unit tests that you feel would be helpful to test your code.

1. The code will be evaluated on the following criteria:
    1. **Correctness.** We have a private set of unit tests that we will run on the code to evaluate this.
    1. **Robustness.** Is the code "production" quality?
    1. **Readability and Organization.** Is your code easy to read? Could another developer easily make changes to your code?
    1. **Unit Tests.** Did you write a thorough set of unit tests for your queue? Did you correctly handle all of the corner cases? Maybe you thought of some tests that we missed! :)

1. Please do not use external resources to help with the algorithmic aspects of this problem. We really want to see how you think and code. That said, if you have basic questions on the functionality of C# library APIs, feel free to find answers on the internet. To clarify, here is a good and bad example of when to use external resources:
    - **Good:** Searching Stack Overflow to understand a nuance of how the C# File APIs work.
    - **Bad:** Searching Stack Overflow for how to implement a queue.

1. Please provide a README.md with your submission to describe:
    - The design choices you made and why you made them.
    - Any external resources you used for help.
    - The amount of time that it took you to write the code and test cases.

1. **Have fun!** If you have any questions, feel stuck or have any concerns, please email enghiring@docugami.com.

## Required Tools

1. Install the appropriate dotnet 2.2.x SDK for your platfrom from the following URL: https://dotnet.microsoft.com/download/dotnet-core/2.2.

2. The IDE of your choice. We recommend Visual Studio Code: https://code.visualstudio.com/Download. If you use VS Code, here are some nice extensions:
    - C#
    - .NET Core Test Explorer
    - Solution Explorer

