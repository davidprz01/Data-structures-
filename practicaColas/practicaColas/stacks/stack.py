class Stack:
    def __init__(self):
        self.stack = []

    def push(self, datos):
        self.stack.append(datos)
    
    def pop(self):
        if self.IsEmpty():
            print("La pila esta vacia")
        return self.stack.pop()
    
    def peek(self):
        if self.IsEmpty():
            print("la pila esta vacia")
        return self.stack[-1]
    
    def IsEmpty(self):
        return len(self.stack) == 0
    

stack1 = Stack()
stack1.push(10)
stack1.push(2)
print(stack1.peek())
print(stack1.pop())
print(stack1.IsEmpty())