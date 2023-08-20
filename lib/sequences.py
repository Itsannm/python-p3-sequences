#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  # Print an empty list for length == 0
    elif length == 1:
        print([0])  # Print [0] when length == 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            next_value = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_value)
        print(fib_sequence)

