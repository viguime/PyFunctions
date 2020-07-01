a=[1, 2, 3, [4.1, [4.21, 4.22, 4.23, 4.24], 4.3], 5, 6, 7]
b=[1, 2, 3, 'pe-de-cabra', 5, 'a', 7] 
c=[1, 2, 3, [4.1, 'a', [4.21, 4, True, 2, 'Maria'], ''], 5, 7]
d=[1, 2, ['l@23N, --q', [7.5, 151, 'Faz sol!'], [4, 4.23, False]], 4.3, 5, 'ana']

#um número inteiro par deve ser substituído por ele próprio somado com o índice de sua posição na lista sendo percorrida;    
#um número inteiro ímpar deve ser substituído por ele próprio multiplicado pelo índice de sua posição na lista sendo percorrida;  
#uma string deve ter seus caracteres alfabéticos transformados em maiúsculos;
#um elemento de qualquer outro tipo deve permanecer inalterado.

def alteraLista(lista):
    for i,el in enumerate(lista):

        if type(el)==list:
            alteraLista(lista[i])
        if type(el)==int:
            if el%2==0:
                lista[i]=el+i
            else:
                lista[i]=el*i

        if type(el)==str:
            lista[i]=el.upper()

    return lista

print(alteraLista(a))
print(alteraLista(b))
print(alteraLista(c))
print(alteraLista(d))
