"""
Finite State Machines from Diagrams
Moore Machine (Image 1) and Mealy Machine (Image 2)
"""

class MooreMachine:
    """
    Moore Machine from Image 1
    States: A/0, B/0, C/1 (state/output)
    Detects pattern "01"
    """
    def __init__(self):
        # Initial state
        self.state = 'A'
        # State outputs
        self.outputs = {
            'A': '0',
            'B': '0',
            'C': '1'
        }
    
    def transition(self, input_symbol):
        """Handles state transitions based on input symbol."""
        if self.state == 'A':
            if input_symbol == '0':
                self.state = 'A'
            elif input_symbol == '1':
                self.state = 'B'
        
        elif self.state == 'B':
            if input_symbol == '0':
                self.state = 'C'
            elif input_symbol == '1':
                self.state = 'B'
        
        elif self.state == 'C':
            if input_symbol == '0':
                self.state = 'A'
            elif input_symbol == '1':
                self.state = 'B'
    
    def process(self, input_string):
        """Process input string and return output string."""
        output = self.outputs[self.state]  # Initial state output
        for symbol in input_string:
            self.transition(symbol)
            output += self.outputs[self.state]
        return output


class MealyMachine:
    """
    Mealy Machine from Image 2
    States: A, B, C
    Prints "a" whenever sequence "01" is encountered
    """
    def __init__(self):
        # Define states
        self.state = 'A'
    
    def transition(self, input_symbol):
        """
        Transition logic for the Mealy Machine that outputs:
        - 'a' when sequence '01' is encountered
        - 'b' otherwise
        """
        if self.state == 'A':
            if input_symbol == '0':
                self.state = 'B'
                return 'b'
            elif input_symbol == '1':
                self.state = 'A'
                return 'b'
        
        elif self.state == 'B':
            if input_symbol == '0':
                self.state = 'B'
                return 'b'
            elif input_symbol == '1':
                self.state = 'C'
                return 'a'  # "01" detected!
        
        elif self.state == 'C':
            if input_symbol == '0':
                self.state = 'B'
                return 'b'
            elif input_symbol == '1':
                self.state = 'A'
                return 'b'
    
    def process(self, input_string):
        """Process the full input binary string and return the output string."""
        output = ''
        for symbol in input_string:
            output += self.transition(symbol)
        return output


# Example usage
if __name__ == "__main__":
    print("="*50)
    print("MOORE MACHINE (Image 1)")
    print("="*50)
    
    # Test Moore Machine
    moore1 = MooreMachine()
    input1 = "01001"
    output1 = moore1.process(input1)
    print(f"Input:  {input1}")
    print(f"Output: {output1}")
    print()
    
    moore2 = MooreMachine()
    input2 = "110011"
    output2 = moore2.process(input2)
    print(f"Input:  {input2}")
    print(f"Output: {output2}")
    print()
    
    print("="*50)
    print("MEALY MACHINE (Image 2)")
    print("="*50)
    
    # Test Mealy Machine
    mealy1 = MealyMachine()
    input3 = "01001"
    output3 = mealy1.process(input3)
    print(f"Input:  {input3}")
    print(f"Output: {output3}")
    print(f"Pattern '01' detected: {output3.count('a')} time(s)")
    print()
    
    mealy2 = MealyMachine()
    input4 = "110011"
    output4 = mealy2.process(input4)
    print(f"Input:  {input4}")
    print(f"Output: {output4}")
    print(f"Pattern '01' detected: {output4.count('a')} time(s)")