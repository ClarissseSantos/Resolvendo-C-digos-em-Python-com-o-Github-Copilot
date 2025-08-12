#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outro IA) para melhorar a estrutura do código.
# Recebendo um número inteiro do usuário
print("Bem-vindo ao programa de verificação de par ou ímpar!")
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar
if numero % 2 == 0:
    resultado = "O número é par."
else:
    resultado = "O número é ímpar."

# Exibindo o resultado

print(resultado)

# Fim do código 