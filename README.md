# Python Parallelism
Repository with the codes used in the study and presentation of Movile Tech Talk Python Zoop.
The code presented here may help those who want to learn more about parallel algorithms using the Python modules Threads, Multiprocessing, and asyncIO (Asynchronous I/O).

![Logo](techtalkpython.png)

## Table of Contents

* [Getting Started](#getting-started)
* [When can parallel programming help us?](#when-can-parallel-programming-help-us)
* [Why did Parallel Programming come about?](#why-did-parallel-programming-come-about)
* [Use Threads with Care](#use-threads-with-care)
* [Concepts to remember](#concepts-to-remember)
* [Understanding the Codes](#understanding-the-codes)
* [Contributions](#contributions)
* [Author](#author)
* [License](#license)
* [Acknowledgments](#acknowledgments)
* [References](#references)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## When can parallel programming help us?

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
  
Then came the OSs whose goal was to allow more than one program to run at the same time through processes.  
  
Some motivators for this to happen were to take better advantage of external IO operations, to make it possible for users and programs with equal priorities to share resources equally and have the convenience of being able to divide the programs into smaller units, each with their computational responsibility.  
  
Well, in these early timeshare systems, each process was a virtual computer by Von Neumann.  
Instructions were sequential.  
For each instruction executed there was a “next instruction”.  
Almost all the programming languages ​​created followed this model of sequential programming, where one instruction was followed after another.  
  
However, many instructions needed to wait for resources outside the logical unit, we call them I/O.  
And finding the right balance between sequentiality and asynchronicity is a necessary feature to make programs more efficient.  
  
It was there that Threads appeared, of course the same reasons that made OSs also lead us to threads.  

## Use Threads with Care

Thread safety is the concept that a function needs all resources to be contained in the context of the thread. Global variables are not contained in the context of threads and therefore, when using these variables, you need synchronization mechanisms to avoid unexpected results.

### Starvation 
Describes a situation where a thread keeps resources stuck for a long period of time, and other threads are blocked forever. So they end up "starving."  

### Deadlock
Is an extreme case in which no thread executes because resources are blocked by N threads and none leaves the bone.  


## Concepts to remember

## Understanding the Codes

### Requirements

You need Python 3.7 or later. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

I recommend and use pyenv [Pyenv](https://github.com/pyenv/pyenv#installation)

A wonderful Python Version Management tool. Previously known as Pythonbrew, pyenv lets you install multiple Python versions, set directory (project)-specific Python versions, and create/manage virtual python environments ("virualenv's"). All this is done on Linux and OS X without depending on Python itself and it works at the user-level, no need for any sudo commands. Even if you already have Python installed on your system, it is worth having pyenv installed so that you can easily try out new language features or help contribute to a project that is on a different version of Python.

## Contributions

* If you found something is missing or inaccurate, create a branch, code, update this guide and send a Pull Request.

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
