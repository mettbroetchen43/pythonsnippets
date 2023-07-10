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


def isint(value):
    '''
    Checks whether given value is of type 'int'
    '''
    return isinstance(value, int)

def isnotstring(value):
    '''
    Checks whether given value is of type 'str' 
    since calculations with strings are pointless.
    '''
    return not isinstance(value, str)

def isnotzero(value):
    return value < 0 or value > 0


def rec(value):
    '''
    Returns the reciprocal of given value.
    '''
    if isnotstring(value) and isnotzero(value):
       return 1/value
    return None

def pow(val1, val2):
    '''
    Returns val1 to the power of val2
    '''
    if isnotstring(val1) and isnotstring(val2):
        return val1 ** val2
    return None

def sqrt(value):
    '''
    Returns the Square Root of val
    '''
    if isnotstring(value):
        return pow(value, 0.5)
    return None

def cbrt(value):
    '''
    Returns the Cube Root of val
    '''
    if isnotstring(value):
        return pow(value, rec(3))
    return None

def root(val1, val2):
    '''
    Returns the val2. root of val1.
    '''
    if isnotstring(val1) and isnotstring(val2):
        return pow(val1, rec(val2))
    return None

def addPercent(val1, val2):
    '''
    Adds val2 % of val1 to val1
    '''
    if isnotstring(val1) and isnotstring(val2):
        return val1 * (1 + (val2 / 100))
    return None

def subPercent(val1, val2):
    '''
    Subtracts val2 % of val1 from val1
    '''
    if isnotstring(val1) and isnotstring(val2):
        return val1 * (1 - (val2 / 100))
    return None

def getPercent(val1, val2):
    '''
    Returns val2 % of val1
    '''
    if isnotstring(val1) and isnotstring(val2):
        return val1 * (val2 / 100)
    return None

def mod(val1, val2):
    '''
    Returns the modulo of val1 / val2
    '''
    if isnotstring(val1) and isnotstring(val2) and isnotzero(val2):
        return val1 % val2
    return None

def val2bin(value):
    '''
    Converts given int value to binary format, 
    but cuts off the "0b" prefix. 
    '''
    if isint(value):
        ret = bin(int(value))[2:]
        return ret
    return None

def val2hex(value):
    '''
    Converts given int value to hexadecimal format, 
    but cuts off the "0x" prefix.
    '''
    if isint(value):
        ret = hex(int(value)).upper()[2:]
        return ret
    return None

def val2oct(value):
    '''
    Converts given int value to octadecimal format,
    but cuts off the 0o prefix.
    '''
    if isint(value):
        ret = oct(int(value))[2:]
        return ret
    return None

def div(val1, val2):
    '''
    I am fully aware that divisions are provided natively
    by Python, but I find it useful though to introduce 
    a division functionality. The special about this function 
    is that it checks whether val2 is not 0, since divisions 
    by zero are mathematically prohibited.
    However, this function divides val1 by val2 and returns the
    result, given the requirements that both values are not strings
    and val2 is not 0. 
    '''
    if isnotstring(val1) and isnotstring(val2) and isnotzero(val2):
        return val1/val2
    return None

