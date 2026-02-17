# Uso POO com classe
class Funcionario:
    funcionarios = []
    def __init__ (self, _nome, _idade, _cargo, __salario):
        self.nome = _nome
        self.idade = _idade
        self.cargo = _cargo
        self.salario = __salario
        Funcionario.funcionarios.append(self)

    def alteracaoSalario(self, novo_salario):
        self.salario = self.salario * (1 + novo_salario/100)
        return f"Salário alterado para: R${self.salario:.2f}"

    def alteracaoCargo(self, novo_cargo):
        self.cargo = novo_cargo
        return f"Cargo alterado para: {self.cargo}"

    def mostrarDados(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nCargo: {self.cargo}\nSalário: R${self.salario:.2f}"

func1 = Funcionario("João", 30, "Desenvolvedor", 3000)
print(func1.mostrarDados())

func1.alteracaoSalario(10)
print(f"Novo salário: R${func1.salario:.2f}")

func1.alteracaoCargo("Lider de Desenvolvimento")
print(f"Novo cargo: {func1.cargo}")
