import moreBool

def nl():
    '''
    This is meant as a helper function.
    It's used to create a visual separation between the outputs
    for improving readability of both the output and the code.
    '''
    print()

str_truefalse = "Based on the input True and False,"
str_falsefalse = "Based on the input False and False,"
str_truetrue = "Based on the input True and True,"
str_falsetrue = "Based on the input False and True,"
str_true = "Based on the input True,"
str_false = "Based on the input False,"

xor_result_truefalse = moreBool.xor(True, False)
xor_result_falsefalse = moreBool.xor(False, False)
xor_result_truetrue = moreBool.xor(True, True)
xor_result_falsetrue = moreBool.xor(False, True)

inv_result_true = moreBool.inv(True)
inv_result_false = moreBool.inv(False)

nor_result_truefalse = moreBool.nor(True, False)
nor_result_falsefalse = moreBool.nor(False, False)
nor_result_truetrue = moreBool.nor(True, True)
nor_result_falsetrue = moreBool.nor(False, True)

xnor_result_truefalse = moreBool.xnor(True, False)
xnor_result_falsefalse = moreBool.xnor(False, False)
xnor_result_truetrue = moreBool.xnor(True, True)
xnor_result_falsetrue = moreBool.xnor(False, True)

nand_result_truefalse = moreBool.nand(True, False)
nand_result_falsefalse = moreBool.nand(False, False)
nand_result_truetrue = moreBool.nand(True, True)
nand_result_falsetrue = moreBool.nand(False, True)

xnand_result_truefalse = moreBool.xnand(True, False)
xnand_result_falsefalse = moreBool.xnand(False, False)
xnand_result_truetrue = moreBool.xnand(True, True)
xnand_result_falsetrue = moreBool.xnand(False, True)

nl()
print (f'{str_truefalse} xor() returns {xor_result_truefalse}.')
print (f'{str_falsefalse} xor() returns {xor_result_falsefalse}.')
print (f'{str_truetrue} xor() returns {xor_result_truetrue}.')
print (f'{str_falsetrue} xor() returns {xor_result_falsetrue}.')
nl()
print (f'{str_true} inv() returns {inv_result_true}.')
print (f'{str_false} inv() returns {inv_result_false}.')
nl()
print (f'{str_truefalse} nor() returns {nor_result_truefalse}.')
print (f'{str_falsefalse} nor() returns {nor_result_falsefalse}.')
print (f'{str_truetrue} nor() returns {nor_result_truetrue}.')
print (f'{str_falsetrue} nor() returns {nor_result_falsetrue}.')
nl()
print (f'{str_truefalse} xnor() returns {xnor_result_truefalse}.')
print (f'{str_falsefalse} xnor() returns {xnor_result_falsefalse}.')
print (f'{str_truetrue} xnor() returns {xnor_result_truetrue}.')
print (f'{str_falsetrue} xnor() returns {xnor_result_falsetrue}.')
nl()
print (f'{str_truefalse} nand() returns {nand_result_truefalse}.')
print (f'{str_falsefalse} nand() returns {nand_result_falsefalse}.')
print (f'{str_truetrue} nand() returns {nand_result_truetrue}.')
print (f'{str_falsetrue} nand() returns {nand_result_falsetrue}.')
nl()
print (f'{str_truefalse} xnand() returns {xnand_result_truefalse}.')
print (f'{str_falsefalse} xnand() returns {xnand_result_falsefalse}.') 
print (f'{str_truetrue} xnand() returns {xnand_result_truetrue}.')
print (f'{str_falsetrue} xnand() returns {xnand_result_falsetrue}.')

