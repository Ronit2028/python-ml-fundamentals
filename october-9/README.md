# October 9: Python Fundamentals

This tutorial introduces core Python syntax and ends with a small feature-scaling example. The examples are collected in [`my-file.py`](my-file.py); most are commented out so you can uncomment and run them one at a time.

## Topics

- Common data types: integers, floats, strings, lists, tuples, sets, and dictionaries
- Arithmetic, comparison, logical, assignment, ternary, and bitwise operators
- Conditional branches, `match` statements, and `for` and `while` loops
- A greeting function, dictionary iteration, and a lambda expression
- Min-max feature scaling for values with known bounds

## Run the script

From this directory, run:

```bash
python3 my-file.py
```

The active scaling example prints:

```text
{'feature1': 0.5, 'feature2': 0.5}
```

The scaling function transforms each sample value with a matching bounds entry using `(value - min_bound) / (max_bound - min_bound)`. Features without bounds are skipped. For this formula, each maximum bound must be greater than its minimum bound.

## Try it

Change the sample values or bounds in the final `scale_feature` call and run the script again. You can also uncomment the earlier examples to explore their output. The `match` example requires Python 3.10 or newer if you choose to enable it.