lisp = '((lambda (arg) (+ arg 1)) 5)'

count = 0
for i in lisp:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1

if count == 0:
    print ("Matching parentheses")
else:
    print ("Not matching parentheses")
