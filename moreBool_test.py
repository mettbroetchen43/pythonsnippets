import moreBool

def nl():
    print()

str_truefalse = "Based on the input True and False,"
str_falsefalse = "Based on the input False and False,"
str_truetrue = "Based on the input True and True,"
str_true = "Based on the input True,"
str_false = "Based on the input False,"

xor_result_truefalse = moreBool.xor(True, False)
xor_result_falsefalse = moreBool.xor(False, False)
xor_result_truetrue = moreBool.xor(True, True)

inv_result_true = moreBool.inv(True)
inv_result_false = moreBool.inv(False)

nor_result_truefalse = moreBool.nor(True, False)
nor_result_falsefalse = moreBool.nor(False, False)
nor_result_truetrue = moreBool.nor(True, True)

nand_result_truefalse = moreBool.nand(True, False)
nand_result_falsefalse = moreBool.nand(False, False)
nand_result_truetrue = moreBool.nand(True, True)

xnand_result_truefalse = moreBool.xnand(True, False)
xnand_result_falsefalse = moreBool.xnand(False, False)
xnand_result_truetrue = moreBool.xnand(True, True)

nl()
print (f'{str_truefalse} xor() returns {xor_result_truefalse}.')
print (f'{str_falsefalse} xor() returns {xor_result_falsefalse}.')
print (f'{str_truetrue} xor() returns {xor_result_truetrue}.')
nl()
print (f'{str_true} inv() returns {inv_result_true}.')
print (f'{str_false} inv() returns {inv_result_false}.')
nl()
print (f'{str_truefalse} nor() returns {nor_result_truefalse}.')
print (f'{str_falsefalse} nor() returns {nor_result_falsefalse}.')
print (f'{str_truetrue} nor() returns {nor_result_truetrue}.')
nl()
print (f'{str_truefalse} nand() returns {nand_result_truefalse}.')
print (f'{str_falsefalse} nand() returns {nand_result_falsefalse}.')
print (f'{str_truetrue} nand() returns {nand_result_truetrue}.')
nl()
print (f'{str_truefalse} xnand() returns {xnand_result_truefalse}.')
print (f'{str_falsefalse} xnand() returns {xnand_result_falsefalse}.') 
print (f'{str_truetrue} xnand() returns {xnand_result_truetrue}.')

