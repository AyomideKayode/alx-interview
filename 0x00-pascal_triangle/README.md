# Project 0x00 Pascal Triangle

## Overview

This Python module implements a function to generate Pascal's Triangle up to the nth row. Pascal's Triangle is a mathematical concept where each number in the triangle is the sum of the two numbers directly above it.

### Requirements

- Python 3.x

### Installation

No installation is required. Simply import the `pascal_triangle` function from the `pascal_triangle` module.

```py
from pascal_triangle import pascal_triangle
```

## Example Usage

```py
from pascal_triangle import pascal_triangle

triangle = pascal_triangle(5)
print(triangle)
```

Output:

```sh
ayomide@Kazzywiz:~/alx-interview/0x00-pascal_triangle$ ./0-main.py 
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
ayomide@Kazzywiz:~/alx-interview/0x00-pascal_triangle$ 
```
