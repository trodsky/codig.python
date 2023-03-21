exercicios = {
    "peito": ["supino reto", "supino inclinado", "supino declinado", "peck deck"],
    "costas": ["barra fixa", "remada baixa", "puxada alta", "pull-up"],
    "ombro": ["elevação frontal", "elevação lateral", "desenvolvimento com halteres", "desenvolvimento militar"],
    "perna": ["agachamento livre", "leg press", "cálice", "extensão de pernas"],
    "bíceps": ["rosca direta com barra", "rosca concentrada", "martelo", "barra fixa"],
    "tríceps": ["supino fechado", "tríceps no pulley", "francês", "barra paralela"]
}

# Esse é um exemplo, pode ser usado alguma outra lista ou dicionario contendo as informações da academia e cada exercício estar em um arquivo ou banco de dados

def criar_rotina(usuario):
  rotina = {}
  
  for i in range(3):
    musculo_1 = input("Digite o primeiro grupo muscular a ser treinado: ")
    exercicio_1 = input("Digite o exercício para o grupo muscular " + musculo_1 + ": ")
    
    musculo_2 = input("Digite o segundo grupo muscular a ser treinado: ")
    exercicio_2 = input("Digite o exercício para o grupo muscular " + musculo_2 + ": ")
    
    rotina[i] = {
        "musculo_1": musculo_1,
        "exercicio_1": exercicio_1,
        "musculo_2": musculo_2,
        "exercicio_2": exercicio_2
    }
    
  return rotina

# Aqui definimos a rotina do usuário em etapas

def exibir_rotina(rotina):
  for i in range(len(rotina)):
    print("Etapa " + str(i+1))
    print("Grupo muscular 1: " + rotina[i]["musculo_1"] + ", Exercício 1: " + rotina[i]["exercicio_1"])
    print("Grupo muscular 2: " + rotina[i]["musculo_2"] + ", Exercício 2: " + rotina[i]["exercicio_2"])
    print("\n")
    
# Aqui exibimos a rotina do usuário em etapas para ele

usuario = "joao"
rotina = criar_rotina(usuario)
exibir_rotina(rotina)
