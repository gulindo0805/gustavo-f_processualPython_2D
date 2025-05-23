numero = int(input("Digite um número: "))
variavel1= 0
while variavel1 <= 100:
   
    produto = numero * variavel1
    print(f"{numero} x {variavel1} = {produto}")
    if produto > 1000:
       print("maior que mil") 
    variavel1 += 1
