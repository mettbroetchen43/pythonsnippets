import moreBool

def nl():
    print()

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
print (f'Based on the input True and False, xor() returns {xor_result_truefalse}.')
print (f'Based on the input False and False, xor() returns {xor_result_falsefalse}.')
print (f'Based on the input True and True, xor() returns {xor_result_truetrue}.')
nl()
print (f'Based on the input True, inv() returns {inv_result_true}.')
print (f'Based on the input False, inv() returns {inv_result_false}.')
nl()
print (f'Based on the input True and False, nor() returns {nor_result_truefalse}.')
print (f'Based on the input False and False, nor() returns {nor_result_falsefalse}.')
print (f'Based on the input True and True, nor() returns {nor_result_truetrue}.')
nl()
print (f'Based on the input True and False, nand() returns {nand_result_truefalse}.')
print (f'Based on the input False and False, nand() returns {nand_result_falsefalse}.')
print (f'Based on the input True and True, nand() returns {nand_result_truetrue}.')
nl()
print (f'Based on the input True and False, xnand() returns {xnand_result_truefalse}.')
print (f'Based on the input False and False, xnand() returns {xnand_result_falsefalse}.') 
print (f'Based on the input True and True, xnand() returns {xnand_result_truetrue}.')

