def xor(expr1, expr2):
    '''
    The exclusive-or logic. One expression (and only one expression!) needs to be true.
    If both are true, the function returns False.
    '''
    return (expr1 and not expr2) or (expr2 and not expr1)

def nor(expr1, expr2):
    '''
    Compares two expressions and returns whether both are False. Neither expr1 nor expr2 may be true to return True. 
    '''
    return (not expr1) and (not expr2)

def inv(expr):
    '''
    Inverts the input signal. A true expression returns false vice-versa.
    '''
    return (not expr)    

def nand(expr1, expr2)
    '''
    Compares two expressions and returns whether at least one of them is false.
    Returns True if at least one of two expressions is false.
    '''
    return (not expr1) or (not expr2)
