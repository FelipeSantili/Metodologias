import pytest
from src.basic.conta import Conta

def conta():
    # Cria uma conta com saldo de R$ 3000 e limite de R$ 1000 para os testes
    return Conta(saldo=3000, limite=1000)

def test_transferencia_com_saldo(conta):
    conta.transferir(pix="test_pix", valor=2000)
    assert conta.saldo == 1000

def test_transferencia_usando_limite(conta):
    conta.transferir(pix="test_pix", valor=3500)
    assert conta.saldo == -500

def test_transferencia_ultrapassando_limite(conta):
    saldo_inicial = conta.saldo
    conta.transferir(pix="test_pix", valor=4500)
    assert conta.saldo == saldo_inicial
