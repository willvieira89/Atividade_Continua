# Linguagem de Programação II
# Atividade Contínua 02 - Classes e Herança
# e-mail: willian.vieira@aluno.faculdadeimpacta.com.br


class Mamifero:
    
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1:
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)

class Reptil:
    
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)

class Cachorro(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca
    
    def latir(self):
        return "{} latindo".format(self.nome)

    def rosnar(self):
        return "{} rosnando".format(self.nome)

class Cavalo(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar(self):
        return "{} galopando".format(self.nome)

    def relinchar(self):
        return "{} relinchando".format(self.nome)

class Gato(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = 7

    def miar(self):
        return "{} miando".format(self.nome)
    
    def morrer(self):
        self.vidas = self.vidas - 1
        if self.vidas <= 0:
            return "{} morreu!!".format(self.nome)
        else:
            return "{} tem {} vidas sobrando".format(self.nome, self.vidas)

class Camaleao(Reptil):
  
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)

class Cobra(Reptil):
    
    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return "{} rastejando".format(self.nome)

    def trocar_pele(self):
        return "{} trocando pele".format(self.nome)

class Jacare(Reptil):

    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return "{} atacando".format(self.nome)

    def dormir(self):
        return "{} dormindo".format(self.nome)

def main():
    cachorro = Cachorro("Sansão", "Preto", 2, "Quadrupede", "Pitbull")
    print(cachorro.__dict__)
    print(cachorro.nome)
    print(cachorro.cor_pelo)
    print(cachorro.idade)
    print(cachorro.tipo_pata)
    print(cachorro.raca)
    print(cachorro.latir())
    print(cachorro.rosnar())
    print(cachorro.correr())
    print(cachorro.mamar())
    print("________________________________________________________________________________________________________________")

    cavalo = Cavalo("Pé de pano", "Branco", 10, "Quadrupede", "Bicolor")
    print(cavalo.__dict__)
    print(cavalo.nome)
    print(cavalo.cor_pelo)
    print(cavalo.idade)
    print(cavalo.tipo_pata)
    print(cavalo.cor_crina)
    print(cavalo.galopar())
    print(cavalo.relinchar())
    print(cavalo.correr())
    print(cavalo.mamar())
    print("________________________________________________________________________________________________________________")

    gato = Gato("Thanos", "Malhado", 3, "Quadrupede")
    print(gato.__dict__)
    print(gato.nome)
    print(gato.cor_pelo)
    print(gato.idade)
    print(gato.tipo_pata)
    print(gato.miar())
    print(gato.morrer())
    print(gato.morrer())
    print(gato.morrer())
    print(gato.morrer())
    print(gato.morrer())
    print(gato.morrer())
    print(gato.morrer())
    print(gato.correr())
    print(gato.mamar())
    print("________________________________________________________________________________________________________________")

    camaleao = Camaleao("Lilo", "Azul", 2, "Grilo")
    print(camaleao.__dict__)
    print(camaleao.nome)
    print(camaleao.cor)
    print(camaleao.idade)
    print(camaleao.inseto_favorito)
    print(camaleao.tomar_sol())
    print(camaleao.botar_ovo())
    print(camaleao.comer_inseto())
    print(camaleao.mudar_de_cor())
    print("________________________________________________________________________________________________________________")

    cobra = Cobra("Nagini", "Vermelha", 5, True)
    print(cobra.__dict__)
    print(cobra.nome)
    print(cobra.cor)
    print(cobra.idade)
    print(cobra.veneno)
    print(cobra.tomar_sol())
    print(cobra.trocar_pele())
    print(cobra.rastejar())
    print(cobra.botar_ovo())
    print("________________________________________________________________________________________________________________")

    jacare = Jacare("Dandy", "Verde", 10, 50)
    print(jacare.__dict__)
    print(jacare.nome)
    print(jacare.cor)
    print(jacare.idade)
    print(jacare.num_dentes)
    print(jacare.tomar_sol())
    print(jacare.botar_ovo())
    print(jacare.atacar())
    print(jacare.dormir())
    
if __name__ == "__main__":
    main()