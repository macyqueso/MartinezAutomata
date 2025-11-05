moore_machine = {
    'A': {'0': 'A', '1': 'B', 'output': 'A'},
    'B': {'0': 'C', '1': 'B', 'output': 'B'},
    'C': {'0': 'D', '1': 'B', 'output': 'B'},
    'D': {'0': 'B', '1': 'C', 'output': 'C'},
    'E': {'0': 'D', '1': 'E', 'output': 'C'}
}

def process_input(machine, start_state, input_str):
    state = start_state
    output = machine[state]['output']  # initial state's output

    for symbol in input_str:
        if symbol not in ['0', '1']:
            print("Invalid input symbol:", symbol)
            return None
        state = machine[state][symbol]
        output += machine[state]['output']
    return output

# given input strings
inputs = ["00110", "11001", "1010110", "101111"]

# process each input
for inp in inputs:
    result = process_input(moore_machine, 'A', inp)
    print(f"Input: {inp}  →  Output: {result}")
