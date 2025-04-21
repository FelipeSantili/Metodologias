import pytest
from src.basic.conta import Conta

@pytest.fixture
def conta_com_limite():
    return Conta(saldo=100, limite=200, pix="123", numero="001")

@pytest.fixture
def conta_sem_limite():
    return Conta(saldo=100, limite=0, pix="123", numero="001")

def test_nao_instanciar_saldo_alem_limite_negativo():
    with pytest.raises(ValueError) as exc:
        Conta(saldo=-201, limite=200, pix="123", numero="001")
    assert "Saldo negativo superior ao limite" in str(exc.value)

def test_nao_instanciar_saldo_negativo_sem_limite():
    with pytest.raises(ValueError) as exc:
        Conta(saldo=-1, limite=0, pix="123", numero="001")
    assert "Conta sem limite não pode ter saldo negativo" in str(exc.value)

def test_instanciacao_valida_com_limite_e_sem_limite(conta_com_limite, conta_sem_limite):
    assert conta_com_limite.saldo == 100
    assert conta_sem_limite.saldo == 100

def test_transferir_para_propria_conta(conta_com_limite, capsys):
    conta_com_limite.transferir(conta_com_limite.pix, 50)
    captured = capsys.readouterr().out
    assert "Não é possível transferir para a própria conta." in captured
    assert conta_com_limite.saldo == 100

def test_transferencia_valida_ajusta_saldo(conta_com_limite, capsys):
    conta_com_limite.transferir("999", 150)
    captured = capsys.readouterr().out
    assert "Pix de R$ 150 realizado para 999" in captured
    assert conta_com_limite.saldo == -50

def test_transferencia_alem_limite_negativo(conta_com_limite, capsys):
    conta_com_limite.transferir("999", 400)
    captured = capsys.readouterr().out
    assert "O valor do pix é maior do que o saldo disponível." in captured
    assert conta_com_limite.saldo == 100
