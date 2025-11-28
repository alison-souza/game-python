print("🎲 Bem-vindo ao jogo: Adivinhe o Número!")
print("Estou pensando em um número entre 1 e 100...")

numero_secreto = 7  # valor fixo
tentativas = 0

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("📉 Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("📈 Muito alto! Tente novamente.")
        else:
            print(f"🎉 Parabéns! Você acertou o número 7 em {tentativas} tentativas!")
            break
    except ValueError:
        print("Digite apenas números!")
