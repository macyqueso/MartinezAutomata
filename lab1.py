print("Problem #1")

def dfa_ends_with_empty(string):
    state = "a"  # start at a
    
    for int in string:
        if state == "a":
            if int == "0":
                state = "a"
            elif int == "1":
                state = "b"
        elif state == "b":
            if int == "0":
                state = ""
            elif int == "1":
                state = "a"
        elif state == "":
            if int == "1":
                state = ""
            elif int == "0":
                state = "b"
    
    return state == ""  # accepting if ends in empty state

examples = ["1110", "01000", "101", "0110", "110100", "01001"]
for e in examples:
    print(f"{e} -> {'Accepted' if dfa_ends_with_empty(e) else 'Rejected'}")

print()
print("Problem #2")

def dfa_ends_with_q0q1(string):
    state = "q0"  # start at q0
    
    for char in string:
        if state == "q0":
            if char == "a":
                state = "q1"
            elif char == "b":
                state = "q2"
        elif state == "q1":
            if char == "b":
                state = "q3"
            elif char == "a":
                state = "q0"
        elif state == "q3":
            if char == "b":
                state = "q1"
            elif char == "a":
                state = "q2"
        elif state == "q2":
            if char == "a":
                state = "q3"
            elif char == "b":
                state = "q0"
    
    return state == "q0"  or state == "q3" # accepting if ends in q0 0r q3

examples = ["aabb", "babb", "abaa", "bba", "ababb", "baaba"]
for e in examples:
    print(f"{e} -> {'Accepted' if dfa_ends_with_q0q1(e) else 'Rejected'}")