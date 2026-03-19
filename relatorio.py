import csv

def analisar_arquivo(nome_arquivo):
    total = 0
    abortados = 0
    prontos = 0
    total_falhas = 0

    # contador de tipos de erro
    tipos_falhas = {
        "temp_interna": 0,
        "temp_externa": 0,
        "energia": 0,
        "estrutura": 0,
        "pressao": 0,
        "modulos": 0,
        "telemetria": 0
    }

    with open(nome_arquivo, "r") as file:
        reader = csv.DictReader(file)

        for linha in reader:
            total += 1

            tempin = float(linha["internal_temp_c"])
            tempex = float(linha["external_temp_c"])
            energia = float(linha["battery_soc_percent"])
            integridade = int(linha["structural_integrity"])
            pressao = float(linha["tank_pressure_bar"])
            modulos = int(linha["critical_modules_status"])
            telemetria = int(linha["telemetry_link_status"])

            erros = 0

            if tempin < 18 or tempin > 35:
                erros += 1
                tipos_falhas["temp_interna"] += 1

            if tempex < -5 or tempex > 30:
                erros += 1
                tipos_falhas["temp_externa"] += 1

            if energia < 60:
                erros += 1
                tipos_falhas["energia"] += 1

            if integridade == 0:
                erros += 1
                tipos_falhas["estrutura"] += 1

            if pressao < 95 or pressao > 145:
                erros += 1
                tipos_falhas["pressao"] += 1

            if modulos == 0:
                erros += 1
                tipos_falhas["modulos"] += 1

            if telemetria == 0:
                erros += 1
                tipos_falhas["telemetria"] += 1

            if erros == 0:
                prontos += 1
            else:
                abortados += 1
                total_falhas += erros

    print(f"\n===== {nome_arquivo} =====")
    print("Total de registros:", total)
    print("Prontos para decolar:", prontos)
    print("Abortados:", abortados)
    print("Total de falhas detectadas:", total_falhas)

    if abortados > 0:
        print("Média de falhas por erro:", round(total_falhas / abortados, 2))

    # 🔥 MOSTRAR DETALHE DAS FALHAS (SÓ PRA ANOMALIA)
    if "anomalias" in nome_arquivo:
        print("\n--- TIPOS DE FALHAS DETECTADAS ---")
        for tipo, qtd in tipos_falhas.items():
            print(f"{tipo}: {qtd}")


# 🔹 EXECUÇÃO
analisar_arquivo("telemetria.csv")
analisar_arquivo("telemetria_anomalias.csv")