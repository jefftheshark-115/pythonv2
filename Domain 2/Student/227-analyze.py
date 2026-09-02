operands = ['+','-','*','/','//','%']
for operand in operands:
    if operand == '//':
        print('// is a floor division operand')
        #break
        continue
    print(operand, 'is an operand')