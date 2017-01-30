"""How many ways can we get an expression to evaluate to true?

Input will consist of symbols i.e. 0 and 1's and operations such as & | ^ etc. Print all ways the expression
can evaluate to true.
Note: the program should not recognize a string like 1^0|1&0 as true. Hint: take a look at precidence
and see what you can do about it.
"""
def ways_of_truth(symbols, operation, expression=''):
    #print(expression)
    if len(symbols) + len(operation) == 0 and eval(expression) == 1:
        print(expression)
    else:
        for i in range(len(symbols)):
            for j in range(len(operation)):
                ways_of_truth(symbols[:i] + symbols[i+1:],
                              operation[:j] + operation[j+1:], '(' +
                              expression + symbols[i] + ')' + operation[j])

        if len(symbols) == 1:
            ways_of_truth('', operation, expression + symbols[0])
print(ways_of_truth(['0','1','0', '1'], ['&', '|', '^']))
print(eval('((1|1)^0)&0'))

