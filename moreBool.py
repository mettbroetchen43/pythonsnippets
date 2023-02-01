def xor(expr1, expr2):
    '''
    The exclusive-or logic. One expression (and only one expression!) needs to be true.
    If both are true, the function returns False.
    '''
    if (expr1 and not expr2) or (expr2 and not expr1):
        return True
    return False

def nor(expr1, expr2):
    '''
    Compares two expressions and returns whether both are False. Neither expr1 nor expr2 may be true to return True. 
    '''
    if (not expr1) and (not expr2):
        return True
    return False

def inv(expr):
    '''
    Inverts the input signal. A true expression returns false vice-versa.
    '''
    if (not expr):
        return True
    return False
    