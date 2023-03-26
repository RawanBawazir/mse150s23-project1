# mse150s23-project1

* Author: RAWAN BAWAZIR
* Class MSE 150
* Semester: Spring 2023

## Overview
This repository contains the starting point for Project 1 for MSE 150 Spring 2023 at Boise State University.


## How to use this code

To use this, clone the repository by running the code below in a command line

```{none}
 git clone git@github.com:RawanBawazir/mse150s23-project1.git
 ```
 
 ## How to run this code
 
 Navigate to the folder containing the cloned repository and type the command below in the command line.
 
```{none}
 python plot.py xargs 
```
 
 Here `xargs` represents the file to be worked on.
 
 ## An example of how to use the code
 
 ```{none}
 python plot.py raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw 
```

Where Sp22_245L_sec-001_tensiletest-pekk_bulk.raw is the data name and can be replaced with any data in the raw_data folder.

## What user should expect

The user should expect the stress-strain graph, and the young's modulus. In addition, a stress-strain graph with the instrument name and the corresponding Young's Modulus as title will be stored in the current working directory.

## Software Dependencies

The required libraries to run this code can be installed as follows:

```{none}
pip install numpy~=1.21.5
```
```{none}
pip install matplotlib~=3.5.2
```

## License

* GNU


