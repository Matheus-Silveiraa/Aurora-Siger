import csv
import random
from datetime import datetime, timedelta

# Função para calcular energia disponível
def calcular_energia(voltage, capacity, soc):
    return (voltage * capacity * (soc / 100)) / 1000

# Função para decidir se pode decolar
def decidir(temp_int, temp_ext, soc, pressure):
    if (18 <= temp_int <= 35 and
        -5 <= temp_ext <= 30 and
        soc >= 60 and
        95 <= pressure <= 145):
        return "READY"
    else:
        return "ABORT"

# Criando arquivo CSV
with open("telemetria.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Cabeçalho
    writer.writerow([
        "timestamp",
        "internal_temp_c",
        "external_temp_c",
        "battery_voltage_v",
        "battery_current_a",
        "battery_soc_percent",
        "battery_capacity_ah",
        "energy_available_kwh",
        "power_load_kw",
        "energy_loss_percent",
        "tank_pressure_bar",
        "structural_integrity",
        "critical_modules_status",
        "telemetry_link_status",
        "estimated_autonomy_min",
        "launch_decision"
    ])

    # Tempo inicial
    tempo = datetime.now()

    # Gerar 500 linhas
    for i in range(500):
        internal_temp = random.randint(18, 35)
        external_temp = random.randint(-5, 30)
        voltage = random.uniform(46, 52)
        current = random.uniform(20, 120)
        soc = random.randint(60, 100)
        capacity = random.randint(80, 120)
        power_load = random.uniform(5, 25)
        energy_loss = random.uniform(2, 8)
        pressure = random.uniform(95, 145)
        autonomy = random.randint(45, 180)

        # Estados fixos
        structural = 1
        modules = 1
        telemetry = 1

        # Cálculo
        energy_available = calcular_energia(voltage, capacity, soc)

        # Decisão
        decision = decidir(internal_temp, external_temp, soc, pressure)

        # Escrever linha
        writer.writerow([
            tempo.strftime("%Y-%m-%d %H:%M:%S"),
            round(internal_temp, 2),
            round(external_temp, 2),
            round(voltage, 2),
            round(current, 2),
            soc,
            capacity,
            round(energy_available, 2),
            round(power_load, 2),
            round(energy_loss, 2),
            round(pressure, 2),
            structural,
            modules,
            telemetry,
            autonomy,
            decision
        ])

        # Incrementa tempo (1 minuto)
        tempo += timedelta(minutes=1)

print("Dataset gerado com sucesso: telemetria.csv 🚀")