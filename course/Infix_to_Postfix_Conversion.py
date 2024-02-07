# a / b - c + d * e - a * c
# ab/c-de*+ac*-

# a + b * c
# abc*+

# a * b + c
# ab*c+

# Wrong Answer
lst = input().split()
stack = []
ans = []
for element in lst:
    if element.isalpha():
      ans.append(element)
    else:
       stack.append(element)
    if len(ans) >= 2:
       if ans[-1].isalpha() and ans[-2].isalpha():
           ans.append(stack.pop())

if stack:
  for token in range(len(stack)):
    ans.append(stack.pop())
print(ans)
print(stack)
