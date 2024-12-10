import json

def parse_input(string_representation):
    try:
        parsed = json.loads(string_representation)
        tm = parsed.get("tm")
        input_string = parsed.get("input")

        required_keys = ['states', 'input_alphabet', 'tape_alphabet', 'transition', 'start_state', 'accept_states', 'reject_states']
        if not all(key in tm for key in required_keys):
            raise ValueError("Turing machine representation is missing required keys.")

        if not isinstance(tm['transition'], dict):
            raise ValueError("Transition function must be a dictionary.")
        
        return tm, input_string
    except Exception as e:
        # print(f"Error parsing input: {e}")
        return None, None
    

def construct_M_prime(tm):
    tm_prime = tm.copy()
    tm_prime['accept_states'] += tm['reject_states']
    tm_prime['reject_states'] = []
    return tm_prime


def mapping_reduction(string_representation):
    tm, w = parse_input(string_representation)

    if tm is None or w is None:
        return "failure string" 
    
    M_prime = construct_M_prime(tm)

    res = json.dumps({"tm": M_prime, "input": w})

    return res
