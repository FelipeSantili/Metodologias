
# from src.password.generate import encrypt_password
# import pytest

# data = [
#     ("password123", "cbfdac6008f9cab4083784cbd1874f76618d2a97"),
#     ("1234", "7110eda4d09e062aa5e4a390b0a572ac0d2c0220"),
# ]

# def load_csv():
#     """ helper function """
#     from path import Path
#     import csv
#     data = []
#     file_name = "passwords.csv"
#     file_path = Path(__file__).parent / file_name
#     with Path.open(file_path, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append((row['password'], row['encrypted']))
#         return data


# class TestPassword:

#     def test_generate_1234(self):     
#         # Esperado:
#         password = "1234"
#         criptografado = "7110eda4d09e062aa5e4a390b0a572ac0d2c0220"

#         res = encrypt_password(password)
#         assert res == criptografado


#     @pytest.mark.parametrize("password, encrypted", data)
#     def test_generate_list(self, password, encrypted):
#         res = encrypt_password(password)
#         assert res == encrypted


#     @pytest.mark.parametrize("password, encrypted", load_csv())
#     def test_generate_list_csv(self, password, encrypted):
#         res = encrypt_password(password)
#         assert res == encrypted
