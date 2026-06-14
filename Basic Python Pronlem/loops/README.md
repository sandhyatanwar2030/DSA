# Loops

Basic loop constructs and pattern problems in Python.

## Concepts Covered

- `for` loops and `while` loops
- Nested loops
- `break`, `continue`, `pass`
- Loop with `else`
- Range-based iteration

## Common Problems

| Problem | Description |
|---------|-------------|
| Pattern Printing | Stars, pyramids, diamonds using nested loops |
| Number Patterns | Floyd's triangle, Pascal's triangle |
| Sum / Count | Sum of digits, count of even/odd numbers |
| Reverse a Number | Using while loop |
| Multiplication Table | Using for loop |

## Example

```python
# Print multiplication table
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

## Key Notes

- `range(start, stop, step)` — stop is exclusive
- Prefer `for` loop when iterations are known
- Use `while` when condition-based termination is needed
