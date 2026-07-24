# Finite State Automaton (FSA)
# Accepts strings ending with "ab"

def finite_state_automaton(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    if state == 2:
        print("Accepted")
    else:
        print("Rejected")

# Input
text = input("Enter a string: ")

# Check the string
finite_state_automaton(text)
