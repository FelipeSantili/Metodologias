import src.basic.conta as c
import pytest

data = []

def load_csv_data():
    """helper function"""
    from pathlib import Path
    import csv
    data = []
    file_name = "contas.csv"
    file_path = Path(__file__).parent / file_name
    with Path.open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row['saldo'], row['limite'], row['valor'], row['esperado']))
        return data

class TestConta:
    @pytest.mark.parametrize("saldo,limite,valor,esperado", load_csv_data())
    def test_transferir(self, saldo, limite, valor, esperado):
        saldo = float(saldo)
        limite = float(limite)
        valor = float(valor)
        expected = float(esperado)
        
        conta = c.Conta(saldo, limite, "10000-0")
        total_inicial = saldo + limite
        conta.transferir("testepix123", valor)
        
        if valor > total_inicial:
            assert conta.saldo + conta.limite == expected
        else:
            assert conta.saldo < 0
