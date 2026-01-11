# LIFO is followed by stack(Last In First Out)
stack=[]
# Push operation
stack.append("A")
stack.append("D")
stack.append("R")
stack.append("E")
# Peek
peek=stack[-1]
print("Peek",peek)
# Pop
pop=stack.pop()
print("Stack after pop",pop)
# Size of stack
print("Size of stack is ",len(stack))

