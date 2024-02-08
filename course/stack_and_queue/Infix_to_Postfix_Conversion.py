# a/b-c+d*e-a*c
# ab/c-de*+ac*-

# a+b*c
# abc*+

# a*b+c
# ab*c+

def infix_to_postfix(expression):
    def precedence(op):
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedences.get(op, 0)

    output = []
    stack = []
    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '(' from stack
        else:  # Operator
            while stack and precedence(char) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

print(infix_to_postfix("A+B*(C^D-E)"))  # Should output "ABCD^E-*+"
print(infix_to_postfix("a/b-c+d*e-a*c"))  # Should output "ab/c-de*+ac*-"
print(infix_to_postfix("a+b*c"))  # Should output "abc*+"
print(infix_to_postfix("a*b+c"))  # Should output "ab*c+"
