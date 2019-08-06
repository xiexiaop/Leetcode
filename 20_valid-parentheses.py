word = input("Provide a string only containing '(){}[]'")
stack = []
outputFlag = False
for c in word:
    if c == '(':
        stack.append(')')
    elif c == '{':
        stack.append('}')
    elif c == '[':
        stack.append(']')
    elif len(stack) == 0 or stack.pop() != c:
        if outputFlag == False:
            print('No')
            outputFlag = True
    
if outputFlag == False:
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')


