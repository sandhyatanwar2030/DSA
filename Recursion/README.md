# 🔄 Recursion in Python

A collection of recursion problems and solutions implemented in Python.

This repository is part of my Data Structures and Algorithms (DSA) learning journey. It contains fundamental to intermediate-level recursion problems designed to strengthen problem-solving skills and build a strong foundation for advanced topics like backtracking, dynamic programming, and trees.

## 📚 What is Recursion?

Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.

It is Basically used when we can divide our problem into sub problem 

Every recursive solution has two essential components:

- **Base Case:** The condition that stops the recursion.
- **Recursive Case:** The part where the function calls itself with a smaller or simpler input.

### Basic Structure

```python
def recursive_function(parameters):
    if base_case:
        return result

    return recursive_function(smaller_problem)