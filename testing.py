from mapping_reduction import mapping_reduction

# Example of a Turing machine and string in ATM that halts
atm_positive_input = '''
{
    "tm": {
        "states": ["q0", "q1", "q2"],
        "input_alphabet": ["0", "1"],
        "tape_alphabet": ["0", "1", "_"],
        "transition": {
            "('q0', '0')": ["q1", "0", "R"],
            "('q1', '1')": ["q2", "1", "R"],
            "('q2', '_')": ["q2", "_", "R"]
        },
        "start_state": "q0",
        "accept_states": ["q2"],
        "reject_states": ["q1"]
    },
    "input": "01"
}
'''

# Example of a Turing machine and string not in ATM that halts
atm_negative_input = '''
{
    "tm": {
        "states": ["q0", "q1", "q2"],
        "input_alphabet": ["0", "1"],
        "tape_alphabet": ["0", "1", "_"],
        "transition": {
            "('q0', '0')": ["q1", "0", "R"],
            "('q1', '1')": ["q1", "1", "R"],
            "('q1', '_')": ["q2", "_", "R"]
        },
        "start_state": "q0",
        "accept_states": ["q2"],
        "reject_states": ["q1"]
    },
    "input": "01"
}
'''

# Example of a Turing machine and string that doesn't halt
non_halting_input = '''
{
    "tm": {
        "states": ["q0", "q1", "q2", "q3"],
        "input_alphabet": ["0", "1"],
        "tape_alphabet": ["0", "1", "_"],
        "transition": {
            "('q0', '0')": ["q1", "0", "R"],
            "('q1', '_')": ["q1", "_", "R"],
            "('q1', '0')": ["q2", "0", "R"]
        },
        "start_state": "q0",
        "accept_states": ["q2"],
        "reject_states": ["q3"]
    },
    "input": "0"
}
'''

# Invalid input (non-string format)
invalid_input_1 = 123  

# Invalid input (missing reject_states in TM description)
invalid_input_2 = '''
{
    "tm": {
        "states": ["q0", "q1", "q2"],
        "input_alphabet": ["0", "1"],
        "tape_alphabet": ["0", "1", "_"],
        "transition": {
            "('q0', '0')": ["q1", "0", "R"],
            "('q1', '1')": ["q2", "1", "R"]
        },
        "start_state": "q0",
        "accept_states": ["q2"]
    },
    "input": "01"
}
'''

# Test runner
def run_tests():
    test_cases = [
        # ("String in ATM that halts", atm_positive_input),
        ("String not in ATM that halts", atm_negative_input),
        ("Non-Halting Input", non_halting_input),
        # ("Invalid Input 1 (non-string)", invalid_input_1),
        ("Invalid Input 2 (missing required keys)", invalid_input_2)
    ]
    
    for name, case in test_cases:
        print(f"Running test: {name}")
        try:
            result = mapping_reduction(case)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")


# Call the test runner
run_tests()
