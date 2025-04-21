from rich import print  # pip install rich

class Conta:
    def __init__(self, saldo=0, limite=0, pix="", numero=""):
        self.saldo = saldo
        self.limite = limite  # cheque especial
        if limite > 0:
            if saldo < -limite:
                raise ValueError("Saldo negativo superior ao limite")
        else:
            if saldo < 0:
                raise ValueError("Conta sem limite não pode ter saldo negativo")
        self.pix = pix
        self.numero = numero
        self.agencia = 0
        self.banco = None
        self.cliente = None

    def transferir(self, pix: str, valor: float):
        """
        Realiza transferência pix com as seguintes validações:
         - Não permite transferência para a própria conta;
         - O valor a ser transferido não pode ser superior à soma do saldo e do limite.
        """
        if pix == self.pix:
            print("Não é possível transferir para a própria conta.")
            return
        if valor > (self.saldo + self.limite):
            print("O valor do pix é maior do que o saldo disponível.")
            return
        self.saldo -= valor
        print(f"Pix de R$ {valor} realizado para {pix}")

    def depositar(self, valor):
        """Adiciona grana no saldo."""
        self.saldo += valor
        print(f"Depósito de [blue]R$ {valor}[/]")

    def consulta(self):
        """Consulta saldo em conta."""
        cl = "red" if self.saldo < 0 else "blue"
        print(f"Saldo atual R$ [{cl}]{self.saldo}[/]")

    def extrato(self):
        """Gera extrato das operações financeiras."""
        pass

if __name__ == "__main__":
    print("*" * 30)
    conta = Conta(saldo=3000, limite=1000, numero="12200-2", pix="45-984011110")
    conta.consulta()
    print("*" * 30)

    conta.transferir(pix="45-984011110", valor=2000)
    conta.consulta()

    print("*" * 30)
    conta.depositar(350)
    conta.consulta()

    print("*" * 30)
    conta.transferir(pix="fulano@gmail.com", valor=4000)
    conta.consulta()

    print("*" * 30)
    conta.transferir(pix="fulano@gmail.com", valor=1000)
    conta.consulta()

    print("*" * 30)
    conta.depositar(3050)
    conta.transferir(pix="45-984011110", valor=1000)
    conta.consulta()

    print("-" * 30)
    conta.extrato()
