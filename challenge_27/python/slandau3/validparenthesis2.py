"""Given a number, n, generate all possible valid parenthesis. N is the number of valid parentehsis you will have.
For example if N = 2, one answer will be ()(), (2 openers and 2 closers)"""

def valid_parenthesis(openers, closers, string):
    if closers == 0 and openers == 0:
        print(string)
    if openers > 0:
        valid_parenthesis(openers-1, closers+1, string + '(')
    if closers > 0:
        valid_parenthesis(openers, closers-1, string + ')')

valid_parenthesis(15,0, "")