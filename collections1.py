# idades = [39, 30, 27, 18]
#
#
# print(len(idades))
#
# idades.remove(30)
#
# idades.clear()
#
# print(idades)

class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Código: {self.codigo} \n Saldo: {self.saldo}'


conta1 = ContaCorrente(15)
conta2 = ContaCorrente(23)

conta1.deposita(500)
conta2.deposita(1200)

contas = [conta1, conta2]

for conta in contas:
    print(conta)

######################################################################

class Conta:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
