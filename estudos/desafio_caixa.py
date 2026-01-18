class Caixa_eletronico:
    def __init__(
        self, saldo_disponivel=1000, notas_disponiveis=[100, 50, 20, 10, 5, 2, 1]
    ):
        self.saldo_disponivel = saldo_disponivel
        self.notas_disponiveis = notas_disponiveis

    def sacar(self, valor):
        if valor >= self.saldo_disponivel:
            print(f"Saldo insuficiente! Limite atual: {self.saldo_disponivel}")
        else:
            self.saldo_disponivel -= valor
            print(f"Saque liberado no valor de: {valor}.")
            print(f"Saldo restante de: {self.saldo_disponivel}.")
            print("-" * 20)
            print("Calculando notas...")

            notas_entregar = {}

            for nota in self.notas_disponiveis:
                quanti_notas = valor // nota
                valor = valor % nota
                if quanti_notas > 0:
                    notas_entregar[nota] = quanti_notas

            for nota, quantidade in notas_entregar.items():
                print(f"{quantidade} nota(s) de R$ {nota},00")

            print("-" * 20)


saque = Caixa_eletronico(1000, [100, 50, 20, 10, 5, 2, 1])
mensagem = saque.sacar(380)
