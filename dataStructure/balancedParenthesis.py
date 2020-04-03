#generate balanced parentesis using stack

class Stack:
    #initialized list elements
    def __init__(self):
        self.elements=[]

    #check if stack is empty or not
    def isEmpty(self):
        return self.elements==[]

    #add element in stack
    def push(self,item):
        self.elements.append(item)

    #delete an element from stack
    def pop(self):
        self.elements.pop()


stObj=Stack()
expr=input('Enter arithmetic Expression to check if parenthesis is balanced or not : ')
x=""
# Traversing the Expression
for i in range(len(expr)) :
    if (expr[i] == '(' or expr[i] == '[' or expr[i] == '{') :
        # Push the element in the stack
        stObj.push(expr[i]);
        continue;
        # IF current character is not opening
        # bracket, then it must be closing.
        # So stack cannot be empty at this point.
    if stObj.isEmpty() :
        isBalanced=False;

    if expr[i] == ')' :
        # Store the top element in a
        x=stObj.pop();

    elif expr[i] == '}':
        # Store the top element in b
        x = stObj.pop();

    elif x == ']':
        # Store the top element in c
        x = stObj.pop();

    # Check Empty Stack
    if stObj.isEmpty():
        isBalanced=True
    else :
        isBalanced=False

if isBalanced:
    print("Parenthesis of Expression ",expr ," is valid")
else:
    print("Parenthesis of Expression ",expr ," is not valid")