tempin = int(input("digite qual a temperatura interna: "))
tempex = int(input("digite qual a temperatura externa: "))
energia = int(input("qual o nivel de energia: "))
integridade = int(input("qual o nivel de integridade: "))
pressao = int(input("qual o nivel de pressão: "))

erros = 0
falhas = []

if tempin < 15 or tempin > 35:
    falhas.append("temperatura interna fora da faixa")
    erros += 1

if tempex < -20 or tempex > 45:
    falhas.append("temperatura externa fora da faixa")
    erros += 1

if energia < 60:
    falhas.append("energia insuficiente")
    erros += 1

if integridade == 0:
    falhas.append("falha estrutural")
    erros += 1

if pressao < 4 or pressao > 6:
    falhas.append("pressão incorreta")
    erros += 1


print("\n--- RELATÓRIO ---")

if erros == 0:
    print("PRONTO PARA DECOLAR 🚀")
else:
    print("DECOLAGEM ABORTADA")
    print("Quantidade de falhas:", erros)
    
    for falha in falhas:
        print("-", falha)