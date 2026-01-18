import random

# Lista de palavras em português
PALAVRAS = [
    "python",
    "programacao",
    "computador",
    "teclado",
    "mouse",
    "desenvolvimento",
    "codigo",
    "variavel",
    "funcao",
    "classe",
    "algoritmo",
    "sistema",
    "software",
    "hardware",
    "internet",
    "aplicativo",
    "dados",
    "arquivo",
    "memoria",
    "processador",
]

palavra = random.choice(PALAVRAS)


class Forca:
    def __init__(self):
        self.palavra_secreta = palavra
        self.vidas = 6
        self.letras_adivinhadas = ["_"] * len(palavra)
        self.letras_erradas = []

    def jogar(self):
        print("Bem-vindo ao jogo da Forca!")
        while self.vidas > 0 and "_" in self.letras_adivinhadas:
            print("\nPalavra: " + " ".join(self.letras_adivinhadas))
            print(f"Vidas restantes: {self.vidas}")
            print("Letras erradas: " + ", ".join(self.letras_erradas))

            letra = input("Digite uma letra: ").lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, digite apenas uma letra.")
                continue

            if letra in self.letras_adivinhadas or letra in self.letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                continue

            if letra in self.palavra_secreta:
                for idx, char in enumerate(self.palavra_secreta):
                    if char == letra:
                        self.letras_adivinhadas[idx] = letra
                print("Boa! Você acertou uma letra.")
            else:
                self.vidas -= 1
                self.letras_erradas.append(letra)
                print("Letra errada.")

        if "_" not in self.letras_adivinhadas:
            print(f"Parabéns! Você ganhou! A palavra era: {self.palavra_secreta}")
        else:
            print(f"Você perdeu! A palavra era: {self.palavra_secreta}")


if __name__ == "__main__":
    jogo = Forca()
    jogo.jogar()
