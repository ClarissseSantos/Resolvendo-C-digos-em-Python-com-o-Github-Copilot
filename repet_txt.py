# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar uma string repetida o número de vezes informado.
# Recebendo números do usuário
print("Bem-vindo ao programa de repetição de texto!")
texto = input("Digite o texto que deseja repetir: ")
repeticoes = int(input("Quantas vezes você gostaria de repetir o texto? ")) 

# Repetindo o texto
texto_repetido = (texto + " ") * repeticoes 

# Exibindo o resultado
print("Texto repetido:", texto_repetido.strip())
# Fim do código