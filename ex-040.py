idade = int(input('Insira a idade do atleta :'))

if idade <= 9:
    print('O Atletta se enquadra na modalidade \033[1;32mMIRIM\033[m')
elif (idade == 10) or (idade <= 14):
    print('O Atleta se enquandra na modalidade \033[1;32mINFANTIL\033[m')
elif (idade == 15) or (idade <= 19):
    print('O Atleta se enquandra na modalidade \033[1;32mJUNIOR\033[m')
elif idade == 20:
    print('O Atleta se enquandra na modalidade \033[1;32mSÊNIOR\033[m')
elif idade >= 21:
    print('O Atleta se enquandra na modalidade \033[1;32mMASTER\033[m')
