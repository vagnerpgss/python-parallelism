# Python Parallelism

![Logo](techtalkpython.png)

## Table of Contents

* [Getting Started](#getting-started)
* [Motivation](#motivation)
* [When can parallel programming help us?](#when-can-parallel-programming-help-us)
* [Why did Parallel Programming come about?](#why-did-parallel-programming-come-about)
* [Thread Benefits](#thread-benefits)
* [Use Threads with Care](#use-threads-with-care)
* [Demystifying](#demystifying)
* [Concepts to remember](#concepts-to-remember)
* [Understanding the Codes](#understanding-the-codes)
* [Contributions](#contributions)
* [Author](#author)
* [License](#license)
* [Acknowledgments](#acknowledgments)
* [References](#references)

## Getting Started

Repository with concepts and codes used in the study and presentation of Movile Tech Talk Python Zoop.
The concepts and codes presented here may help those who want to learn more about parallel algorithms using the Python modules Threads, Multiprocessing, and asyncIO (Asynchronous I/O).

## Motivation

What motivated me to start this research:  
Writing correct programs is difficult;  
Writing parallel algorithms correctly is much more difficult (A lot of things can go wrong);  
Demystify concepts;  
Arouse interest in the subject and to find people interest to help and share knowledge.  

## When parallel programming help us?

Traditionally, parallel programming has been motivated by solving fundamental science problems, the so-called Grand Challenge Problems (GCPs)  
In addition to scientific studies, bringing a little more to the world of systems programming, we can benefit from using parallel programming at problems that have the following characteristics:  

### I/O Bound:
* Webscraping
* Disk read and write
* Data sharing between programs
* Network communications

### CPU Bound:
* Calculations
* Text formatting
* Image rescheduling
* Data analysis  

## Why did Parallel Programming come about?

Initially, computers did not have Operating Systems. 
They ran a single program from start to finish with direct access to all machine resources.  
Running a single program at a time was an inefficient use of scarce and expensive computing resources.  
  
Then came the OSs whose goal was to allow more than one program to run at the same time through **processes**.  
  
Some motivators for this to happen were to take better advantage of external I/O operations, to make it possible for users and programs with equal priorities to share resources equally and have the convenience of being able to divide the programs into smaller units, each with their computational responsibility.  
  
Well, in these early timeshare systems, each process was a virtual computer by Von Neumann.  
Instructions were sequential.  
For each instruction executed there was a “next instruction”.  
Almost all the programming languages ​​created followed this model of sequential programming, where one instruction was followed after another.  
  
However, many instructions needed to wait for resources outside the logical unit, we call them I/O.  
And finding the right balance between sequentiality and asynchronicity is a necessary feature to make programs more efficient.  
  
It was there that Threads appeared.  
The same concerns (resource utilization, fairness, and convenience) that motivated the development of **processes** also motivated the development of **threads**.  
Threads allow multiple streams of program control flow to coexist within a process. They share process-wide resources such as memory and file handles, but each thread has its own program counter, stack, and local variables.  
Threads also provide a natural decomposition for exploiting hardware parallelism on multi-processor systems; multiple threads within the same program can be scheduled simultaneously on multiple CPUs.  
Threads are sometimes called lightweight processes, and most modern operating systems treat threads, not processes, as the basic units of scheduling.  
In the absence of explicit coordination, threads execute simultaneously and asynchronously with respect to one another. Since threads share the memory address space of their owning process, all threads within a process have access to the same variables and allocate objects from the same heap, which allows finer-grained data sharing than inter-process mechanisms. But without explicit synchronization to coordinate access to shared data, a thread may modify variables that another thread is in the middle of using, with unpredictable results.

## Thread Benefits

It is faster to create/terminate a thread than a process;  
It is faster to switch between threads of the same process;  
Threads can communicate without invoking the CPU as they share a memory;  
Improve the performance of complex applications;  
Transform asynchronous flows into largely sequential workflows;  
Better responsiveness of GUI applications;  
Better throughput on application servers.  

## Use Threads with Care

Thread safety is the concept that a function needs all resources to be contained in the context of the thread. Global variables are not contained in the context of threads and therefore, when using these variables, you need synchronization mechanisms to avoid unexpected results.

### Starvation 
Describes a situation where a thread keeps resources stuck for a long period of time, and other threads are blocked forever. So they end up "starving."  

### Deadlock
Is an extreme case in which no thread executes because resources are blocked by N threads and none leaves the bone.  

## Demystifying

Parallelism is a technique that consists of breaking large and often complex tasks into smaller tasks, distributing them among interconnected processors and simultaneously executing instructions in order to obtain faster results. It operates on two levels: hardware and software parallelism. It is paralleled to obtain increased performance, computational performance gains, and decreased processing costs.  
Software parallelism is the ability to speed up the execution of a program, roughly speaking, dividing it into pieces and assigning each part of that division to be executed between the nodes, leaving each node with a piece of code.  
Parallel processing consists of dividing a given application so that it can be executed by several processing elements, which in turn must cooperate with each other (communication and synchronism), seeking efficiency by breaking the paradigm of sequential execution of the flow of information. instructions, dictated by von Neumann's philosophy.  
Multithreading is not the same as parallel processing. When we talk about parallel processing, we talk about using hardware resources with multiple processors and executing code at the same time, that is, in parallel. Multithreading concerns competition in the execution of processes. A computer with a single core cannot execute code in parallel, although it can execute code concurrently. The competition is about disputing the CPU usage for different processes, while parallelism is about using different "cores". However, as the operating system handles running threads, it can also cause a multithreaded system to be parallel if there are hardware resources for that.  

## Concepts to remember

Parallelism = technique that uses N streams to complete a computation.  
Threading = specific implementation of parallelism.  
Multithreading = threads of the same process running simultaneously.  
Multithreading is better for I / O.  
Multiprocessing is best for calculations.  
Multiprocessing always with n_process = n_cores and never more than that.  
There can be only one thread running in a python process.  

## Understanding the Codes

### Requirements

You need Python 3.7 or later. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

I recommend and use pyenv [Pyenv](https://github.com/pyenv/pyenv#installation)

A wonderful Python Version Management tool. Previously known as Pythonbrew, pyenv lets you install multiple Python versions, set directory (project)-specific Python versions, and create/manage virtual python environments ("virualenv's"). All this is done on Linux and OS X without depending on Python itself and it works at the user-level, no need for any sudo commands. Even if you already have Python installed on your system, it is worth having pyenv installed so that you can easily try out new language features or help contribute to a project that is on a different version of Python.

### Python

The default Python interpreter was designed with simplicity in mind and has a thread-safe mechanism, the so-called “GIL” (Global Interpreter Lock). In order to prevent conflicts between threads, it executes only one statement at a time (so-called serial processing, or single-threading).

### Threading

Run Code Concurrently Using the Threading Module.  
[threading module](https://docs.python.org/3/library/threading.html)

This module, nicely encapsulates threads, providing a clean interface to work with them and can be directly imported.  

Since almost everything in Python is represented as an object, threading also is an object in Python. A thread is capable of:
* Holding data.  
* Stored in data structures like dictionaries, lists, sets, etc.  
* Can be passed as a parameter to a function.  

A thread can also be executed as a process.  
A thread in Python can have various states like:  

### Multiprocessing

multiprocessing is a package that supports spawning processes using an API similar to the threading module.
[multiprocessing module](https://docs.python.org/3/library/multiprocessing.html)

### Threading vs Multiprocessing

* Spawn
  * A new thread is spawned within the existing process
  * A new process is started independent from the first process

* Velocity
  * Starting a thread is faster than starting a process

* Memory
  * All threads share the memory
  * Memory is not shared between processes

* Thread Synchronization
  * Necessary on threads to conrol access to shared data
  * Not necessary for processes unless threading in the new process 

* GIL
  * One GIL for all threads
  * One GIL for each process

### asyncio - Asynchronous I/O

asyncio is a library to write concurrent code using the async/await syntax.
[asyncio module](https://docs.python.org/3/library/asyncio.html)

## Contributions

* If you found something is missing, inaccurate, or misspelled, create a branch, code, update this guide and send a Pull Request.

## Author

* **Vagner Santos** - *Initial work* - [GitHub](https://github.com/vagnerpgss)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details

## Acknowledgments

* Euclides da Cunha by encouragement - https://github.com/euclidescunha

## References

[Fluent Python Support files for the O'Reilly book by Luciano Ramalho](https://github.com/fluentpython)  
[multiprocessing — Process-based parallelism](https://docs.python.org/3.7/library/multiprocessing.html)  
[threading — Thread-based parallelism](https://docs.python.org/3.7/library/threading.html)  
[asyncio — Asynchronous I/O](https://docs.python.org/3.7/library/asyncio.html)  
[Python modules for simulating and manipulating VLBI data](https://github.com/achael/eht-imaging)  
[Parallelism in One Line](https://chriskiehl.com/article/parallelism-in-one-line)  
[Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)  
[Improve Your Python Skills](https://dbader.org/blog/)  
