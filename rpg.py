import random
import time
import sys

# Função para rolar um dado de n lados
def rolar_dados(n_lados):
    return random.randint(1, n_lados)

# Exemplo de rolagem de um D8
resultado = rolar_dados(8)
time.sleep(2)  # Pausa de 2 segundos

# Biblioteca de armas
armas = {
    "Espada e Escudo": {"dano": 5, "defesa": 4},
    "Arco": {"dano": 8, "defesa": 1},
    "Cajado": {"dano": 9, "defesa": 1},
    "Espada de duas mãos": {"dano": 9, "defesa": 1}
}

# Biblioteca de inimigos e seus atributos
inimigos = {
    1: {"nome": "Troll", "hp": 12, "str": 5, "df": 2},
    2: {"nome": "Skull", "hp": 16, "str": 6, "df": 1},
    3: {"nome": "Zumbi", "hp": 22, "str": 4, "df": 2},
    4: {"nome": "Mago Caído", "hp": 27, "str": 12, "df": 4},
    5: {"nome": "Demônio Antigo", "hp": 35, "str": 12, "df": 5}
}

# Classe para definir as classes de personagens
class Classe:
    def __init__(self, nome, arma, ataque_basico, ataque_especial):
        self.nome = nome
        self.arma = arma
        self.ataque_basico = ataque_basico
        self.ataque_especial = ataque_especial

# Definindo as classes de personagens
classes_personagem = {
    "Cavaleiro": Classe("Cavaleiro", "Espada e Escudo", "Golpe com Espada 🗡️💫", "Lâmina da Bravura 🗡️💫✨"),
    "Mago": Classe("Mago", "Cajado", "Bola de Fogo 🔥", "Tempestade Arcana ✨🌀"),
    "Arqueiro": Classe("Arqueiro", "Arco", "Flecha Rápida 🏹", "Chuva de Flechas 🏹🌟"),
    "Bárbaro": Classe("Bárbaro", "Espada de duas mãos", "Corte Selvagem 🗡️💫", "Fúria do Bárbaro 🗡️💥")
}

# Classe para definir o personagem
class Personagem:
    def __init__(self, nome, classe, nivel=1):
        self.nome = nome
        self.classe = classe
        self.str = 0
        self.int = 0
        self.dex = 0
        self.ag = 0
        self.hp = self.calcular_hp()
        self.arma = self.classe.arma  # A arma é definida pela classe do personagem
        self.hp_max = self.hp
        self.nivel = nivel
    
    def incrementar_nivel(self):
        self.nivel += 1
        return self.nivel

    def calcular_hp(self):
        return self.str * 3 + self.int * 2 + self.dex * 6 + self.ag * 2

    def distribuir_pontos(self):
        pontos_restantes = 7
        while pontos_restantes > 0:
            print("-"*100)
            print(f" ★ Você tem {pontos_restantes} pontos restantes para distribuir. ★")
            print("-"*100)
            atributo = input("Digite o atributo para adicionar um ponto (STR, INT, DEX, AG): ").lower()
            if atributo in ["str", "int", "dex", "ag"]:
                setattr(self, atributo, getattr(self, atributo) + 1)
                pontos_restantes -= 1
            else:
                print("-"*100)
                print("□ Atributo inválido. Por favor, escolha entre STR, INT, DEX ou AG. □")
                print("-"*100)
        self.hp = self.calcular_hp()  # Recalcular HP após distribuir pontos
        self.hp_max = self.hp  # Atualizar o HP máximo após distribuir pontos

    def mostrar_arma(self):
        print(f" Arma do {self.nome}: {self.arma}")
        print("Estatísticas da arma:")
        for atributo, valor in armas[self.arma].items():
            print(f"{atributo.capitalize()}: {valor}")

    def mostrar_ataques(self):
        print(f"Ataques do {self.nome}:")
        print(f"Ataque Básico: {self.classe.ataque_basico}")
        print(f"Ataque Especial: {self.classe.ataque_especial}")

    def regenerar_hp(self, quantidade):
        self.hp += quantidade
        if self.hp > self.hp_max:
            self.hp = self.hp_max
    
    def adicionar_runa(self, dano_extra):
        armas[self.arma]["dano"] += dano_extra

    def aumentar_atributos(self):
        self.str += 1
        self.int += 1
        self.dex += 1
        self.ag += 1

# Função para definir o combate
def combate(personagem, inimigo):
    print("═"*100)
    print(f"Seu inimigo surgiu\n{personagem.nome} encontrou um {inimigo['nome']}!")
    print("═"*100)
    time.sleep(2)

    # Frases de ataque
    ataques_basicos = [
        "A lâmina gira no ar e atinge o inimigo",
        "Um golpe rápido e preciso corta o ar",
        "Você desferiu um golpe forte"
        "acertou em cheio !!"
    ]
    ataques_especiais = [
        "Você invoca todo o seu poder para um ataque devastador",
        "Uma explosão de energia atinge o inimigo",
        "Seu ataque especial faz o chão tremer"
    ]

    frase_inimigo_derrotado = [
        "Waaarrrhhh",
        "O inimigo cai ao chão com um último suspiro.",
        "Você venceu! O inimigo está derrotado.",
        "Com um grito de desespero, o inimigo é derrotado.",
        "O inimigo se dissolve em uma poça de escuridão.",
        "O inimigo solta um último gemido e desaparece.",
        "Você derrotou o inimigo com maestria!",
        "O inimigo se ajoelha e desmorona.",
        "Com um último grito de dor, o inimigo cai.",
        "O inimigo cai, vencido por sua força."

    ]

    while personagem.hp > 0 and inimigo["hp"] > 0:
        # Turno do personagem
        print("-"*100)
        print(f"\nTurno de {personagem.nome}. Escolha seu ataque:")
        print("═"*100)
        print(f"1. {personagem.classe.ataque_basico}")
        print(f"2. {personagem.classe.ataque_especial}")
        print("═"*100)
        escolha = input("Digite o número do ataque escolhido: ")
        print("-"*100)

        if escolha == "1":
            dano = rolar_dados(8) + armas[personagem.arma]["dano"]+ int(personagem1.str/100) + int(personagem1.int/100)
            frase = random.choice(ataques_basicos)
            print("═"*100)
            print(f"★ {personagem.nome} usou {personagem.classe.ataque_basico}, {frase} seu ataque causou {dano} de dano!")
            print("═"*100)
        elif escolha == "2":
            dano = rolar_dados(8) + armas[personagem.arma]["dano"]+int(personagem1.str/100) + int(personagem1.int/100) * 2
            frase = random.choice(ataques_especiais)
            print("═"*100)
            print(f"╬ {personagem.nome} usou {personagem.classe.ataque_especial}, {frase} seu ataque causou {dano} de dano!")
            print("═"*100)
        else:
            print("-"*100)
            print("Escolha inválida. Você perdeu seu turno.")
            dano = 0
            print("-"*100)

        inimigo["hp"] -= dano
        print("-"*100)
        print(f"{inimigo['nome']} agora tem {inimigo['hp']} HP.")
        print("-"*100)
        time.sleep(2)

        if inimigo["hp"] <= 0:
            frase_inimigo1 = random.choice(frase_inimigo_derrotado)
            print(frase_inimigo1)
            print("═"*100)
            print(f"{personagem.nome} derrotou o {inimigo['nome']}!")
            print("-"*100)
            personagem1.regenerar_hp(3)
            print(f"{personagem1.nome} regenerou 3 pontos de vida. HP atual: {personagem1.hp}/{personagem1.hp_max}")
            personagem1.aumentar_atributos()
            personagem1.incrementar_nivel()
            print("═"*100)
            print(f"{personagem1.nome} ★ você subiu de Nível após a vitória e aumentou seus atributos +1. ★")
            print(f"Nivel atual: ★ {personagem1.nivel} ★")
            print(f"STR: {personagem1.str}, INT: {personagem1.int}, DEX: {personagem1.dex}, AG: {personagem1.ag}")
            print("═"*100)
            break

        # Turno do inimigo
        print("")
        print("═"*100)
        print(f"\nTurno do {inimigo['nome']}.")
        print("═"*100)
        dano_inimigo = (rolar_dados(8) + inimigo["str"]) - (armas[personagem.arma]["defesa"]+int(personagem1.str/100))
        personagem.hp -= dano_inimigo
        print("═"*100)
        print(f" ★ {inimigo['nome']} atacou e causou {dano_inimigo} de dano a {personagem.nome}.")
        print("═"*100)
        print("-"*100)
        print(f"{personagem.nome} agora tem {personagem.hp} HP.")
        print("-"*100)
        time.sleep(2)

        if personagem.hp <= 0:
            print("")
            print("-"*100)
            print(f"{personagem.nome} foi derrotado pelo {inimigo['nome']}.")
            print("="*100)
            print(" ╬ Você sentiu o golpe... suas forças se esvai enquanto você contempla a escuridão... este é seu fim... ╬")
            print("═"*100)
            print("╔════════════════════════════════════════════════════════╗")
            print("║           💀  ★ ★ ★ Game Over ★ ★ ★  💀             ║")
            print("╚════════════════════════════════════════════════════════╝")
            print("╔════════════════════════════════════════════════════════╗")
            print("║        Vejo você em breve, honrado aventureiro.        ║")
            print("╚════════════════════════════════════════════════════════╝")
            sys.exit()
            break

# Introdução do jogo
print("╔" + "═" * 48 + "╗")
print("║ 🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄      ║")
print("║" + " " * 48 + "║")
print("║  Bem-vindo ao mundo mágico de EbnersLand       ║")
print("║ onde muitas aventuras e perigos se             ║")
print("║ encontram e espreitam.                         ║")
print("║ Vamos começar uma aventura...                  ║")
print("║" + " " * 48 + "║")
print("║ 🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄⛰️🌳🍃🍄      ║")
print("╚" + "═" * 48 + "╝")

time.sleep(2)
print("")
print("═"*100)
print("Seu personagem foi capturado pelo exército de Balador e está atualmente nas masmorras. Como último suspiro de vida, seu parceiro, o Elfo da Floresta, Alangmar, o libertou de sua prisão. Agora, você deve honrar seu último sacrifício e fugir desta prisão enfrentando os inimigos e encontrando a saída para avisar ao rei de Aomar.")
print("="*100)
time.sleep(2)
print("-"*100)
print("Mas antes, vamos definir a criação do seu personagem.")
print("-"*100)
print("")
# Pergunta para iniciar o jogo
print("═"*100)
inicio = input(" ★ Deseja iniciar o jogo? (Sim/Não): ★ ")
print("═"*100)

if inicio.lower() == "sim":
    # Criando um objeto da classe personagem
    print("")
    print("╔══════════════════════════════════════╗")
    print("║           Crie Seu Personagem        ║")
    print("╚══════════════════════════════════════╝")
    nome = input("Digite o nome do personagem: ")
    classe_nome = input("Digite a classe do personagem (Cavaleiro, Mago, Arqueiro, Bárbaro): ")
    if classe_nome in classes_personagem:
        classe = classes_personagem[classe_nome]
        personagem1 = Personagem(nome, classe)
    else:
        print("-"*50)
        print("Classe inválida. Por favor, escolha entre Cavaleiro, Mago, Arqueiro ou Bárbaro.")
        print("-"*50)
        sys.exit()
else:
    print("-"*50)
    print("------Vejo você em breve, honrado aventureiro.-------------")
    print("-"*50)
    sys.exit()

# Distribuindo os pontos
personagem1.distribuir_pontos()

# Exibindo os atributos finais do personagem
print("-"*50)
print("⭐️══════════════════════════════════════════════⭐️")
print(f"\nAtributos do seu personagem: {personagem1.nome}:")
print(f"NIvel do personagem: {personagem1.nivel}")
print(f"Classe: {personagem1.classe.nome}")
print(f"Força (STR): {personagem1.str}")
print(f"Inteligência (INT): {personagem1.int}")
print(f"Destreza (DEX): {personagem1.dex}")
print(f"Agilidade (AG): {personagem1.ag}")
print(f"Pontos de vida (HP): {personagem1.hp}")
# Mostrando informações sobre a arma escolhida
personagem1.mostrar_arma()
# Mostrando informações sobre os ataques
personagem1.mostrar_ataques()
print("⭐️══════════════════════════════════════════════⭐️")
print("")
# Início do jogo
time.sleep(2)
print("📜")
print("-"*100)
print(f"Muito bem, {personagem1.classe.nome} {personagem1.nome},este é o momento de provar toda a sua bravura.")
time.sleep(2)
print("")
print(f"Lentamente você avança masmorras adentro buscando a saída, mas sua fuga inevitavelmente chamou a atenção da presença inimiga") 
time.sleep(2)
print("📜")
print("-"*100)
#1ª Ato: Primeiro Ato
print("Pouco a pouco você começa a ouvir os tambores cada vez mais alto, apressadamente acelera seus passos por entre as rochas umidas... quando de repente !!")
time.sleep(1)
print("Seu primeiro inimigo lhe avista de longe e parte para seu encontro. atras das sombras você não consegue ve-lo !! a batalha é inevitavel se quiser sair.... ")
print("📜")
print("-"*100)
# Encontrou seu primeiro Inimigo um inimigo aleatório e iniciar o combate
inimigo_encontrado = inimigos[1]
combate(personagem1, inimigo_encontrado)
print("📜")
print("a batalha foi ardua mas a vitoria era inevitável perante sua força, mas há mais perigos por entre as sombras...")
time.sleep(2)
print("A escuridão domina o ambiente, mais a frente avista uma tocha, ela lhe ajudara em sua jornada...")
time.sleep(1)
print("Oh olhe, ume escadaria !!")
time.sleep(1)
print("Prontamente você inicia sua subida... será a tão sonhada saída ?!")
print("")
print("WHAAAWWWHH !!!")
print("")
print("Oh Não mais um inimigo lhe seguiu por entre as trevas e surgiu ao seu encontro.... vença-o se quiser prosseguir !!!")
time.sleep(2)
print("📜")
# Encontrou seu segundo Inimigo um inimigo aleatório e iniciar o combate
inimigo_encontrado = inimigos[2]
combate(personagem1, inimigo_encontrado)

# 3ª Ato: Terceiro Ato
print("")
print("A exaustão bate, o cansaço agora é nitido, a batalha foi ardua, os inimigos estão ficando mais fortes....")
print("📜")
time.sleep(1)
print("Mas devemos prosseguir, o futuro do reino está em alertar o Alto Rei das forças do exercito inimigo...")
print("")
print(f"Empunhando o(a) {personagem1.arma}, reune suas forças e parte em busca da saida.... ")
print("")
print("passos são ouvidos logo atrás, a proximidade dos inimigos agora é proxima.... eles ja sabem que estou aqui....")
print("")
time.sleep(1)
print("Meus passos agora não são mais sutis preciso correr !!!")
print("")
print("Correndo você chega até um salão ornamentado...")
print("O chão é de rochas desenhadas, os pilares se estendem a 7 metros do chão em forma cilindrica, há um altar e uma passagem logo atrás....")
print("Você sente que o caminho é por ali... então segue...")
print("")
print("Antes que pudesse atravessar...")
time.sleep(3)
print("")
print("uma ameaça surge atrás de você !!")
print("")
print("Quase que por reflexo e suas habilidades, você consegue esquivar do golpe do novo inimigo que quer sua morte !!")
time.sleep(2)
print("Pronto para mais uma batalha !?!")
print("📜")
# Encontrou seu segundo Inimigo um inimigo aleatório e iniciar o combate
inimigo_encontrado = inimigos[3]
combate(personagem1, inimigo_encontrado)
print("📜")
print("A batalha exauriu quase tudo que tinha o caminh é arduo, os ferimentos ja são visiveis, o cansaço inevitável...")
print("")
print("Você avança lentamente se apoiando nas paredes rochosas... mais a frente eis que...")
print("")
print("Dois Caminhos se apresentaram escolha seu destino em um dos caminhos...")
print("")
print("-"*120)
print("1: A esquerda uma escadaria ingrime e tortuosa iluminada por velhos candelabros.")
print("2: A direita um tunel mal construido, escuro, com uma pequena luz de vela mais a frente, chão e rochas e paredes ornamentadas com dizeres rupestres de uma cultura antiga.")
print("-"*120)
print("")
print("="*100)
escolha = input("Escolha o caminho desejado 1 ou 2: ")
print("="*100)
print("")
if escolha == "1":
    print("-"*100)
    print("Você escolheu a escadaria, apoia-se na parede e inicia sua subida, no caminho avista o abismo que o aguarda caso escorregue....")
    print("")
    print("seu caminho será dificil os tambores de batalha se intensificam e gritos de batalha são ouvidos")
    print("")
    print("Flechas voam ao seu alcance...")
    print("")
    print("Acima você adentra uma estreita passagem e avista um tumulo antigo")
    print("")
    print("No canto os restos mortais do que parecia ser um antigo sacerdote...")
    print("")
    print("Os restos do esqueleto pouco ornamentado com vestes rasgadas segura algo em suas mãos parece ser um artefato ")
    print("-"*100)
    artefato = input("Você deseja pegar ?: (Sim/Não):").lower()
    print("-"*100)
    if artefato == "não":
        print("")
        print("Rapidamente você encontra uma entrada a que o Leva a um 'Grande Salão'.")
        print("")
    else:
        print("-"*100)
        print("Você pega o artefato e logo o identifica...")
        print("")
        print("Trata-se de uma runa antiga de força que da ao portador mais poder de força a sua arma... pela luz de Bravanel")
        personagem1.adicionar_runa(8)
        print(f"⭐️ sua(seu) {personagem1.arma}, ganhou + 8 Dano, seu status atual é: ")
        personagem1.mostrar_arma()
        print("")
        print("Com dificuldade você avança e encontra um 'Grande salão'")
else:
    print("")
    print("-"*100)
    print("Você escolheu o tunel, lentamente se esgueira pelo tunel medindo e calculando seus passos...")
    print("")
    print("Passo a passo você caminha tunel adentro, e vai chegando mais proximo a pequena luz")
    print("")
    print("Que revela-se ser uma vela em cima de uma pequena mesa de madeira, há uma entrada para uma pequena salinha dentro da caverna...")
    print("")
    print("La dentro vc avista a vela, a mesinha e uma prateleira.... no outro canto....")
    print("")
    print("Há um pequeno baú")
    print("")
    print("="*100)
    baú = input("Deseja abrir um Baú: (Sim/Não):").lower()
    print("="*100)
    if baú == "não":
        print("-"*100)
        print("você se retira da sala e segue o caminho a diante")

    else:
        print("-"*100)
        print("📜")
        print("Você abre o baú e encontra dentro dele manuscritos antigos mencionando um grande mal um demônio encontrado nas profundesas das cavernas durante as escavações...")
        print("")
        print("Os antigos necromantes o denominaram de 'O Porteiro' aquele que carrega a chave da entrada do abismo...")
        print("")
        print("Um mal criado no inicio dos tempos onde a magia compartilhava lugar com as trevas antigas....")
        print("")
        print("Que ele habita as trevas e lá esta adormecido... aguardando ser desperto...")
        print("")
        print("no outro lado do baú uma poção de vitalidade Nv:5 você rapidamente toma e...")
        print("📜")
        personagem1.regenerar_hp(10)
        print("-"*100)
        print(f"⭐️ {personagem1.nome} regenerou 10 pontos de vida. HP atual: {personagem1.hp}/{personagem1.hp_max} ⭐️")
        print("")
        print("Revigorado e com as feridas parcialmente curadas você avança seu caminho...")
        print("")
        print("Daí em diante mais iluminada você encontra uma passagem e la dentro um grande portão de ferro...")
        print("")
        print("Com dificuldade você avança e encontra um 'Grande salão'")

time.sleep(2)

print("📜")
print("Parece um ambiente ritualistico, um altar no centro e escadarias ao redor... algo foi celebrado ali")
print("")
print("Ruidos são ouvidos ali proximo...")
print("")
print("💬  'Este será seu tumulo...'")
print("")
print("Seu proximo inimígo surgiu... prepare-se para a batalha...")
print("")
print(f"Empunhando seu {personagem1.arma}, prepara-se para uma nova batalha")
# fim do 4 ato.
print("📜")
# inimigo 4 encontrado
inimigo_encontrado = inimigos[4]
combate(personagem1, inimigo_encontrado)
print("-"*100)
print("📜")
print("Os inimigos são muitos, e a cada novo desafio eles vão aparentando mais forte...")
print("")
print(f"A batalhac com o {inimigos[4]["nome"]} foi ardua seus poderes malignos contaminaram voccê mas com sua força e determinação conseguiu vence-lo")
print("")
print("O caminho agora a frente parece livre...")
print("")
print("💥💥  BRRRRRRRUUUUUMMMMMMM !!! CRRAAAAAASHHHH 💥💥")
print("")
print("Um grande estrondo foi ouvido no fundo do abismo atras de você")
print("")
print("O que pode ter causado tal estondoso barulho ?!")
print(f"💬  {inimigos[4]["nome"]} 'Ha ha ha, urhgs.... (mal conseguindo respirar seu ultimo adversário revela) - 'Com a minha morte o ultimo selo foi quebrado.... urgh agora nada mais o deterá")
print("")

falas_personagem_biblioteca = {
    1: "Do que está falando criatura das trevas ?",
    2: "Que mal este abismo ainda esconde, como sairei daqui ?"
}
print("-"*100)
print(f"1:{personagem1.nome} - {falas_personagem_biblioteca[1]}")
print(f"2:{personagem1.nome} - {falas_personagem_biblioteca[2]}")
print("-"*100)
print("="*100)
fala_personagem = input("escolha sua fala: 1 ou 2 ?")
print("="*100)
print("-"*100)
if fala_personagem == "1":
    print("")
    print("-"*100)
    print(f"💬 {personagem1.nome} - '{falas_personagem_biblioteca[1]}'")
    print(f"💬 {inimigos[4]["nome"]} - 'Hah hah hah... acho que você deve saber, sabe que no íntimo da sua alma sente a presença dele o demônio do mundo antigo !! urghs em breve ele chegará a minha morte o libertou o despertou e agora sua morte chegará este será seu tumulo hahahahhahaha aarhhh'")
else:
    print("")
    print("-"*100)
    print(f"💬  {personagem1.nome} - '{falas_personagem_biblioteca[2]}'")
    print(f"💬  {inimigos[4]["nome"]} - 'Saída ?, não ha saída para a escuridão.... a unica forma de sair daqui é derrotando o portador da escuridão, o demônio do mundo antigo... sua magia ainda vive e queima com o fogo do abismo... sinta seu pavor e trema hahahahah !!!!' ")

print("📜")
print("Voce sente uma força maligna se aproximando.... ao lado do corpo morto do seu adversário você encontra uma urna ")
print("")
print("-"*100)
urna = input("Agora é a hora definitiva Deseja abrir a urna: (Sim/Não):").lower()
if urna == "sim":
    print("")
    print("você encontrou 2 relíquias .....")
    print("="*100)
    print("1: Luz de Ahsalohr: (Restaura 7 de HP) ")
    print("2: Runa Mística de Absalom: (aumenta o Dano da arma em +7)")
    print("="*100)
    reliquias = {
        1: "Luz de Ahsalohr 🌟",
        2: "Runa Mística de Absalom 💎"
    }
    print("="*100)
    reliquia_escolha = input("Qual você escolhe ? (1 ou 2)")
        
    if reliquia_escolha == "1":
        personagem1.regenerar_hp(10)
        print("")
        print(f"Você escolheu {reliquias[1]} e lhe foi concedido restauração de HP+7: 🌟✨ {personagem1.hp}/{personagem1.hp_max}.")
    else:
        personagem1.adicionar_runa(8)
        print("")
        print("="*100)
        print(f"Você escolheu {reliquias[2]} e lhe foi agraciado o poder de Absalom sua arma possui DANO+7: 🌟✨ ")
        personagem1.mostrar_arma()

else:
    print("📜")
    print("Rapidamente você se prepara para o que esta por vir....")

print("-"*100)
print(f"Agora preparado você empunha sua(seu) {personagem1.arma}")
print("")
print("O suor escorre do seu rosto... suas feridas demonstram o que enfrentou até ali, sua liberdade dependendos proximos momentos....")
print("Mas sabe que deve estar preparado para a batalha final...")
print("")
print("Quando de repente o estrondo final é ouvido...")
print("")
print(" 💥💥 BRRRLRLLLLLLLSHHRRHAAAAARRKKK !!!! 💥💥")
print("")
print("A muralha que dividia o salão a sua frente é posta ao chão em pedaços.. o inimigo final finalmente se apresentou...")
print("")
print("ele o olha diretamente nos olhos... seus olhos emanam escuridão e maldade, seu corpo é trevas envolto em chamas, seus chifres dão uma volta e se estendem por suas costas, ele mede pelo menos 12 metros de altura, seus dentes podem ser vistos afiados a distancia.... suas garras longas seguram uma lamina negra antiga... este ser de pura maldade precisa ser detido...")
print("")
print("Pronto para a batalha !!!")
print(f"💬  {inimigos[5]["nome"]} - Hashu nah ktar, murak l'nagn tah !!!")
print("")
# inimigo 5 encontrado
inimigo_encontrado = inimigos[5]
combate(personagem1, inimigo_encontrado)

#Final

print("📜")
print("O inimigo final finalmente caiu.... você observa suas chamas se esvairem....")
print("")
print("Tudo começa a ruir aos pontos... ")
print("")
print("Lentamente você reune suas forças afim de encontrar a saida... ")
print("")
print("Com as rochas caindo sua liberdade se revela")
print("")
print("Uma passagem ornamentada com runas elficas se mostra no final do grande salão")
print("")
print("Rapidamente você corre e salta por entre a passagem se desmoronando...")
print("")
print("A caverna desaba logo atras de você")
print("")
print("Você sente a brisa das terras livres suaves sobre seu rosto, por sobre suas feridas...")
print("")
print("Ao levantar a cabeça você avista no horizonte o castelo do Alto rei, e na base da montanha seus amigos lhe esperam...")
print("")
print(f"A batalha foi ardua mas sua vitoria dependeu de sua sabedoria e maestria, parabens {personagem1.classe.nome} {personagem1.nome} há muito a contar ao Alto Rei sobre as forças do maligno... a terra media depende de você")
print("╔═══════════════════════════════════════════════════════╗")
print("║   🌟✨ Parabens você concluiu com êxito 🌟✨        ║")
print("╚═══════════════════════════════════════════════════════╝")
print("Dados finais")

# Exibindo os atributos finais do personagem
print("✨🌟════════════════════════════════════════════🌟✨")
print(f"\nAtributos finais de {personagem1.nome}:")
print(f"Classe: {personagem1.classe.nome}")
print(f"Força (STR): {personagem1.str}")
print(f"Inteligência (INT): {personagem1.int}")
print(f"Destreza (DEX): {personagem1.dex}")
print(f"Agilidade (AG): {personagem1.ag}")
print(f"Pontos de vida (HP): {personagem1.hp}")

# Mostrando informações sobre a arma escolhida
personagem1.mostrar_arma()

# Mostrando informações sobre os ataques
personagem1.mostrar_ataques()
print("✨🌟════════════════════════════════════════════🌟✨")







