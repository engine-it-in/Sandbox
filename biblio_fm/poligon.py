from contracts import contract

@contract(x='int,>=0')
def f(x):
    pass

f(-2)