def han(height,a='a',b='b',c='c'):
    if height==1:
        print(f'从{a}移向{c}')
    else:
        han(height-1,a,c,b)
        print(f'从{a}移向{c}')
        han(height-1,b,a,c)
he=input('height')
han(int(he))