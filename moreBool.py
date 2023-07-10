# MIT License

# Copyright (c) 2023 Sascha Mester

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



def isBool(expr):
    '''
    Checks whether Expression is of type Bool, which is fundamentally 
    important here.
    '''
    return isinstance(expr, bool)

def xor(expr1, expr2):
    '''
    The exclusive-or logic. One expression (and only one expression!) needs to be true.
    If both are true or both are false, the function returns False.
    '''

    if isBool(expr1) and isBool(expr2):
        return (expr1 and not expr2) or (expr2 and not expr1)

def inv(expr):
    '''
    Inverts the input signal. A true expression returns false vice-versa.
    '''
    if isBool(expr):
        return (not expr)    

def nor(expr1, expr2):
    '''
    Compares two expressions and returns whether both are False. Neither expr1 nor expr2 may be true to return True. 
    '''
    if isBool(expr1) and isBool(expr2):
        return inv(expr1) and inv(expr2)

def xnor(expr1, expr2):
    '''
    Compares two expressions and returns whether both are True or both are False.
    Returns True if expr1 and expr2 are True. 
    Also returns True if expr1 and expr2 are False.
    Returns False if expr1 is True and expr2 is False vice-versa.
    '''
    if isBool(expr1) and isBool(expr2):
        return (expr1 and expr2) or (inv(expr1) and inv(expr2))

def nand(expr1, expr2):
    '''
    Compares two expressions and returns whether at least one of them is false.
    Returns True if at least one of two expressions is false.
    '''
    if isBool(expr1) and isBool(expr2):
        return inv(expr1) or inv(expr2)

def xnand(expr1, expr2):
    '''
    Compares two expressions and returns whether one of them is false.
    Returns True if one of two expressions is false. If both expressions
    are true or both expressions are false, this function returns False.
    '''
    if isBool(expr1) and isBool(expr2):
        return xor(inv(expr1), inv(expr2))

