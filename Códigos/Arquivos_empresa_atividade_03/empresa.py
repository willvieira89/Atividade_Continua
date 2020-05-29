﻿# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
#
# e-mail: willian.vieira@aluno.faculdadeimpacta.com.br

from typing import Dict, List


class Pessoa:
    '''
    Classe Abstrata Pessoa - não deve ser alterada
    '''

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    '''
    Classe Abstrata funcionário.
    Métodos que tenham exatamente a mesma implementação em todas as classes filhas
    podem ser editados nesta classe, por exemplo consulta_carga_horaria, que sempre retorna
    o valor de carga horária salvo no objeto. No entanto, todos os métodos que tenham uma
    implementação específica para dada classe, devem ser sobrescrito em tais classes.
    '''

    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):
        '''
        Construtor da classe Funcionário - lembre-se de usar o super para acessar o construtor da classe mãe
        e criar atributos que já estão definidos lá.
        '''
        super().__init__(nome, idade)
        self.email = email
        self.carga_horaria_semanal = carga_horaria_semanal

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        raise NotImplementedError

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        raise NotImplementedError

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self.carga_horaria_semanal

    def aumenta_salario(self) -> None:
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        self.salario_base = (self.salario_base * 0.05) + self.salario_base


'''
DICAS:

Se uma classe não possui um método definido, mas este método é definido em
alguma classe mãe acima, a classe irá herdar e usar tal método exatamente como
ele está definido na classe acima.

Isto também se aplica ao construtor, se Programador não define um __init__, então
esta classe está automaticamente usando o __init__ da classe Funcionário (se
funcionário tampouco definisse um __init__, então seria usado o de Pessoa, e se
pessoa tampouco o fizesse, seria usado o de Object, que é a classe base do Python
usada automaticamente para todos as classes que criamos).

Caso você queira ou precise adicionar atributos extras na classe Programador
(ou qualquer outra classe filha de Funcionário), defina o método construtor,
faça a utilização do super e adicione os atributos extra que serão específicos
daquela classe, sejam eles recebidos por parâmetros ou não.

Lembrando sempre que o enunciado define quais são os parâmetros obrigatórios
de uma classe, então se forem criados parâmetros obrigatórios extras, isso
irá gerar erros nos testes de correção.
'''


class Programador(Funcionario):
    '''
    Funcionário do tipo programador:
    - salario base por hora 35.00;
    - regime de trabalho entre 20h e 40h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal e considere que o mês
      possui sempre 4.5 semanas.
    '''

    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):
        super().__init__(nome, idade, email, carga_horaria_semanal)
        self.salario_base = 35.00
        

    @property
    def carga_horaria_semanal(self):
        return self._carga_horaria_semanal

    @carga_horaria_semanal.setter
    def carga_horaria_semanal(self, carga_horaria_semanal):
        if carga_horaria_semanal >= 20 and carga_horaria_semanal <= 40:
            self._carga_horaria_semanal = carga_horaria_semanal
        else:
            raise ValueError


    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        self.carga_horaria_semanal = nova_carga_horaria
    
    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        salario_mensal = (self.salario_base * self.carga_horaria_semanal * 4.5) 
        return salario_mensal


class Estagiario(Funcionario):
    '''
    Funcionário do tipo estagiário:
    - salario base por hora 15.50;
    - auxilio alimentação fixo de 250 reais por mês;
    - regime de trabalho deve estar entre 16h e 30h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal, considere que o mês
      possui sempre 4.5 semanas, e por fim adicione o auxílio alimentação.
    '''

    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):
        super().__init__(nome, idade, email, carga_horaria_semanal)
        self.salario_base = 15.50
        self.auxilio_alimentacao = 250.00
        

    @property
    def carga_horaria_semanal(self):
        return self._carga_horaria_semanal

    @carga_horaria_semanal.setter
    def carga_horaria_semanal(self, carga_horaria_semanal):
        if carga_horaria_semanal >= 16 and carga_horaria_semanal <= 30:
            self._carga_horaria_semanal = carga_horaria_semanal
        else:
            raise ValueError

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        self.carga_horaria_semanal = nova_carga_horaria

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        salario_mensal = (self.salario_base * self.carga_horaria_semanal * 4.5) + self.auxilio_alimentacao
        return salario_mensal


class Vendedor(Funcionario):
    '''
    Funcionário do tipo vendedor:
    - salario base por hora 30.00;
    - auxilio alimentação fixo de 350 reais por mês;
    - auxilio transporte fixo de 30 reais por visita realizada ao cliente;
    - regime de trabalho deve estar entre 15h e 45h semanais, caso contrário
      levanta um ValueError;
    - possui um atributo privado que guarda o número de visitas realizadas no mês,
      começando sempre em zero;
    - cálculo do sálario mensal: calcule o pagamento semanal, considere que o mês
      possui sempre 4.5 semanas, e por fim calcule e adicione os auxílios;
    - além dos métodos de Funcionário, deve implementar os métodos:
      * realizar_visita; e
      * zerar_visitas.
    '''

    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):        
        super().__init__(nome, idade, email, carga_horaria_semanal)
        self.__numero_visitas = 0
        self.salario_base = 30.00
        self.auxilio_alimentacao = 350.00
        self.auxilio_transporte = 30
        

    @property
    def carga_horaria_semanal(self):
        return self._carga_horaria_semanal

    @carga_horaria_semanal.setter
    def carga_horaria_semanal(self, carga_horaria_semanal):
        if carga_horaria_semanal >= 15 and carga_horaria_semanal <= 45:
            self._carga_horaria_semanal = carga_horaria_semanal
        else:
            raise ValueError


    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        self.carga_horaria_semanal = nova_carga_horaria

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        salario_mensal = (self.salario_base * self.carga_horaria_semanal * 4.5) + self.auxilio_alimentacao + (self.auxilio_transporte * self.__numero_visitas)
        return salario_mensal

    def consulta_visitas(self) -> int:
        """
        Retorna o número de visitas realizadas pelo vendedor até o momento
        """
        return self.__numero_visitas

    def realizar_visita(self, n_visitas: int) -> None:
        '''
        Recebe um número inteiro e incrementa o número de visitas realizadas no mês
        com o valor recebido. Antes de fazer a alteração, verifique se n_visitas é
        um número inteiro e levante um TypeError caso contrário; Em seguida verifique
        se n_visitas é positivo e maior que zero, levantando um ValueError caso contrário.
        '''
        if not type(n_visitas) is int:
            raise TypeError
        elif n_visitas <= 0:
            raise ValueError
        else:
            self.__numero_visitas += n_visitas

    def zerar_visitas(self) -> None:
        '''
        Quando chamado deve redefinir o número de visitas realizadas pelo vendedor para zero,
        de modo a começar a contagem para o mês seguinte.
        '''
        self.__numero_visitas = 0


class Empresa:
    '''
    Classe empresa, gerencia diversos funcionários
    '''

    def __init__(self, nome: str, cnpj: int, area_atuacao: str,
                 equipe: List[Funcionario] = []):
        '''
        Construtor da classe empresa
        '''
        self.nome = nome
        self.cppj = cnpj
        self.area_atuacao = area_atuacao
        self.equipe = equipe

    def contrata(self, novo_funcionario: Funcionario) -> None:
        '''
        Contrata um novo funcionário para a empresa (adicionando ele à lista de funcionários)
        '''
        self.equipe.append(novo_funcionario)

    def lista_fucionarios(self) -> List[Funcionario]:
        '''
        
        Devolve um lista com todos os funcionarios
        '''
        return self.equipe

    def folha_pagamento(self) -> float:
        '''
        Devolve o valor total gasto com o pagamento de todos os funcionários
        DICA: Itere sobre a lista de funcionários, fazendo cada objeto do tipo Funcionário
        calcular o próprio salário e acumule isso numa variável auxiliar.
        '''
        total_folha = []
        
        for func in self.equipe:
            total_folha.append(func.calcula_salario())
            
        return sum(total_folha)

    def dissidio_anual(self) -> None:
        '''
        Aumenta o valor da hora trabalhada em 5% para todos os funcionários
        DICA: idem ao método de folha de pagamento, percorra a lista de funcionários faça
        cada objeto funcionário aumentar o próprio salário base por hora.
        '''

        for func in self.equipe:
            func.aumenta_salario()

    def listar_visitas(self) -> Dict[str, int]:
        '''
        Retorna um dicionário com as visitas realizadas por cada vendedor;
        Como a chave do dicionário precisa ser única, deve ser usado o email do vendedor
        e o valor deve ser o número de visitas realizadas por aquele funcionário.
        DICA: percorra a lista de funcionários e use o operador 'is' para verificar se
        o funcionário é um vendedor, em caso positivo, adicione as informações pedidas
        ao dicionário, e por fim retorne esse dicionário (não precisa guardar em um atributo).
        '''
        visitas_por_vendedor = {}

        for func in self.equipe:
          
          if isinstance(func, Vendedor):
              visitas_por_vendedor[func.email] = func.consulta_visitas()
        
        return visitas_por_vendedor


    def zerar_visitas_vendedores(self) -> None:
        '''
        Zera as visitas de todos os funcionário, use a dica do método listar_visitas e
        para cada vendedor, chame o método de zerar visitas do vendedor.
        '''
        for func in self.equipe:
            if isinstance(func, Vendedor):
                func.zerar_visitas()
