print("Hello word, oque voce precisa?")
print("1-Cadastrar uma conta")
print("2-Entrar em uma conta")
Querer = int(input(""))

def escolha (numero):
    print("Você escolheu a opção {numero}")

if Querer == 1:
    escolha(Querer)
elif Querer == 2 :
    escolha(Querer)
else: 
    print("Por favor, insira um valor entre 1 e 2")