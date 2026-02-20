class Funcionario:
    funcionarios = []
    def __init__ (self, _nome, _idade, _cargo, __salario):
        self.nome = _nome
        self.idade = _idade
        self.cargo = _cargo
        self.salario = __salario
        Funcionario.funcionarios.append(self)
    @property
    def alteracao_salario(self):
        return self.salario

    @alteracao_salario.setter
    def alteracao_salario(self, novo_salario):
        self.salario *= 1 + novo_salario/100
        return f"Salário alterado para: R${self.salario:.2f}"
    @property
    def alteracao_cargo(self):
        return self.cargo

    @alteracao_cargo.setter
    def alteracao_cargo(self, novo_cargo):
        self.cargo = novo_cargo
        return f"Cargo alterado para: {self.cargo}"

    def mostrar_dados(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nCargo: {self.cargo}\nSalário: R${self.salario:.2f}"

func1 = Funcionario("João", 30, "Desenvolvedor", 3000)
print(func1.mostrar_dados())

func1.alteracao_salario = 10
print(f"Novo salário: R${func1.salario:.2f}")

func1.alteracao_cargo = "Lider de Desenvolvimento"
print(f"Novo cargo: {func1.cargo}")
