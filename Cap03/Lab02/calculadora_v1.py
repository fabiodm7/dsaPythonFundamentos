# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def opcaoCalculo() :
    opcao = int(input(
'''\nSelecione a operação que deseja realizar:
\n1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair
\n'Digite a opção desejada entre 1,2,3,4: '''))
    return opcao

def entrada() :
    return float(input('Digite um numero: '))

def calculadora() :
    op = opcaoCalculo()
    while op != 0 :
        if op not in [1,2,3,4]:
            print('Opcao inválida, tente novamente: ')
        else :
            ent01 = entrada()
            ent02 = entrada()
            if op == 1 :
                print('Resultado: %.2f' %(ent01 + ent02))
            elif op == 2 :
                print('Resultado: %.2f' %(ent01 - ent02))
            elif op == 3 :
                print('Resultado: %.2f' %(ent01 * ent02))
            else :
                print('Resultado: %.2f' %(ent01 / ent02))
        op = opcaoCalculo()
    print('Obrigado por usar a "Python Calculator"!')

calculadora()