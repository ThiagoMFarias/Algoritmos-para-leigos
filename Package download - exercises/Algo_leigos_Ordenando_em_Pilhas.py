# Stack = pilha
MyStack = []
StackSize = 3

def DisplayStack():
    print('Stack currently contains: ')
    for Item in MyStack:
        print(Item)

def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print('Stack is full.')
def Pop():
    if len(MyStack) > 0:
        print('Popping: ', MyStack.pop()) # Pop remove e devolve o último item da lista. 
    else:
        print('Stack is empty.')

Push(1)
Push(2)
Push(3)
DisplayStack()

Push(4)

Pop()
DisplayStack()

Pop()
Pop()
Pop()