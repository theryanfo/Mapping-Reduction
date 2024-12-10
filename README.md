# Mapping Reduction Computable Function for Halt-TM to Accept-TM

This project implements a mapping reduction that demonstrates the undecidability of the **Acceptance Problem for Turing Machines (Accept-TM)** by reducing it to the **Halting Problem (Halt-TM)**. 

## Overview

The project defines a mapping reduction from the the Halt-TM problem to the Accept-TM problem. It constructs a new Turing machine \( M' \) by modifying the accept and reject states of the given Turing machine \( M \) to give a new string representation in Accept-TM only if the original string representation was in Halt-TM

The program performs the following steps:
1. **Parse input:** A JSON string representation of a Turing machine and an input string is parsed.
2. **Construct \( M' \):** A new machine \( M' \) is constructed by modifying the accept and reject states.
3. **Return transformed problem:** The transformed problem, represented as a new Turing machine \( M' \) and input string, is returned.

## Requirements

- Python 3.x
- JSON format for input representations of Turing machines and input strings.

## Files

- **`mapping_reduction.py`**: Contains the main implementation of the mapping reduction function.
- **`testing.py`**: A test runner to validate the implementation using various test cases.

## Functions

### `parse_input(string_representation)`
Parses a JSON string representation of a Turing machine and an input string, returning a dictionary for the Turing machine and the input string.

### `construct_M_prime(tm)`
Constructs a modified Turing machine \( M' \) by combining the accept and reject states of the original machine.

### `mapping_reduction(string_representation)`
Applies the mapping reduction to a given Turing machine and input string, transforming it into a new Turing machine \( M' \).

**Input:**
- A JSON-formatted string containing the Turing machine and input string.

**Output:**
- A JSON-formatted string representing the transformed Turing machine \( M' \) and input string or a failure string.

## Running the Tests

To run the tests, execute the following:

```bash
python testing.py
