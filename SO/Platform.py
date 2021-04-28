import platform
import getpass
from datetime import datetime

print("Distribuicao do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versao do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Maquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versao do Python....................: ", platform.python_version())

print(datetime.now())
print(datetime.now().time())
print(datetime.now().year)
print(datetime.now().day)

print(getpass.getuser())
usuario = input("\nDigite o usuario: ").upper()
senha = getpass.getpass("Digite a senha: ")
if usuario == "BITMED" and senha == "FiAp1222":
 print("Usuario logado")
else:
 print("Login Negado")