for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

str1 = "(my variable )"
count_paren = 0
for i in str1:
    if (i == '(') or (i == ')'):
        count_paren = count_paren + 1
print ("parentheses count = {}".format(count_paren))
