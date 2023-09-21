# Initialize lists to keep track of brackets and nesting level
expression_list = []
bracket_stack = []  # We'll use a stack to keep track of nested brackets
# User input
expression = str(input("Enter an expression: "))
# Add user input characters into the list
expression_list = list(expression)
# Iterate through the expression
for char in expression_list:
    if char == '(':
        bracket_stack.append('(')  # Push an opening bracket onto the stack
    elif char == ')':
        if len(bracket_stack) > 0 and bracket_stack[-1] == '(':
            bracket_stack.pop()  # Pop a matching opening bracket from the stack
        else:
            bracket_stack.append(')')  # Push a closing bracket onto the stack if it's unmatched

# Check the final state of the bracket stack
if len(bracket_stack) == 0:
    print("Correct.")
else:
    print("Incorrect.")
