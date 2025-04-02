import pytest
from src.basic.conta import Conta

def test_transferencia_com_saldo(capsys):
    conta = Conta(saldo=3000, limite=1000, pix="123", numero="001")
    conta.transferir("456", 2000)
    assert conta.saldo == 1000
    capturado = capsys.readouterr().out
    assert "Pix de R$ 2000 realizado para 456" in capturado

def test_transferencia_usando_limite(capsys):
    conta = Conta(saldo=3000, limite=1000, pix="123", numero="001")
    conta.transferir("456", 3500)
    assert conta.saldo == -500
    capturado = capsys.readouterr().out
    assert "Pix de R$ 3500 realizado para 456" in capturado

def test_transferencia_ultrapassando_limite(capsys):
    conta = Conta(saldo=3000, limite=1000, pix="123", numero="001")
    conta.transferir("456", 4500) 
    assert conta.saldo == 3000
    capturado = capsys.readouterr().out
    assert "O valor do pix é maior do que o saldo disponível." in capturado

def test_transferencia_para_propria_conta(capsys):
    conta = Conta(saldo=3000, limite=1000, pix="123", numero="001")
    conta.transferir("123", 500)
    assert conta.saldo == 3000
    capturado = capsys.readouterr().out
    assert "Não é possível transferir para a própria conta." in capturado
