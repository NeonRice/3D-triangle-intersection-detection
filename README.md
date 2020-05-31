# 🔺 Triangle - Triangle Intersection Detection 🔺
![](https://i.imgur.com/z6Mzpng.png)

## References

Implementation of Tomas Akenine Moeller's Fast Triangle-Triangle interesection detection algorithm in Python

* [Original implementation](http://fileadmin.cs.lth.se/cs/Personal/Tomas_Akenine-Moller/code/tritri_isectline.txt)
* [Reference paper](https://web.stanford.edu/class/cs277/resources/papers/Moller1997b.pdf)

## Program functionalities
#### Input: T1 vertices and T2 vertices

Input can be supplied in any of the given formats:

* OFF file format
* TXT file format (input has to be 6 vertices, each coordinate seperated by spaces and and vertex by a newline)
* Hand input

Example of a possible TXT file:
```sh
5.790 9.870 2.628 - 1 vertex 3 coordintes x y z
6.572 4.942 1.053
7.939 2.860 1.922  
5.892 5.015 4.031 - Triangle 2 starts here
8.874 9.951 2.820
0.054 5.089 0.300
```

## Output
1. Generates an OFF file representing the two triangles
2. Outputs into the console whether the two triangles intersect

### Example
#### Input / Output
![](https://i.imgur.com/1G0rxNx.png)
#### Output OFF Representation
![](https://i.imgur.com/EMuCDNz.png)
