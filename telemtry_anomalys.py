import csv
import random
from datetime import datetime, timedelta

def calcular_energia(voltage, capacity, soc):
    return (voltage * capacity * (soc / 100)) / 1000

def decidir(temp_int, temp_ext, soc, pressure, structural, modules, telemetry):
    if (18 <= temp_int <= 35 and
        -5 <= temp_ext <= 30 and
        soc >= 60 and
        95 <= pressure <= 145 and
        structural == 1 and
        modules == 1 and
        telemetry == 1):
        return "READY"
    else:
        return "ABORT"

with open("telemetria_anomalias.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

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
        "launch_decision",
        "anomalia_inserida"
    ])

    tempo = datetime.now()

    for i in range(500):
        # valores normais
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

        structural = 1
        modules = 1
        telemetry = 1

        anomalia = "nao"

        # 3% de chance de anomalia
        if random.random() < 0.03:
            anomalia = "sim"
            tipo = random.choice(["temp", "bateria", "pressao", "estrutura", "modulos", "telemetria"])

            if tipo == "temp":
                internal_temp = random.randint(45, 70)

            elif tipo == "bateria":
                soc = random.randint(5, 25)

            elif tipo == "pressao":
                if random.random() < 0.5:
                    pressure = random.uniform(40, 80)
                else:
                    pressure = random.uniform(160, 220)

            elif tipo == "estrutura":
                structural = 0

            elif tipo == "modulos":
                modules = 0

            elif tipo == "telemetria":
                telemetry = 0

        # recalcular energia
        energy_available = calcular_energia(voltage, capacity, soc)

        # recalcular decisão
        decision = decidir(internal_temp, external_temp, soc, pressure, structural, modules, telemetry)

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
            decision,
            anomalia
        ])

        tempo += timedelta(minutes=1)

print("Dataset com anomalias gerado: telemetria_anomalias.csv 😈")