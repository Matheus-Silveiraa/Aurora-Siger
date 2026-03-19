# 🚀 Projeto: Sistema de Verificação de Telemetria – Missão Aurora Siger

## 📌 Descrição

Este projeto simula um sistema de verificação de telemetria para pré-decolagem de uma nave espacial.
O objetivo é analisar dados críticos e decidir automaticamente se a nave está **PRONTA PARA DECOLAR** ou se a **DECOLAGEM DEVE SER ABORTADA**.

O sistema foi desenvolvido em Python e utiliza datasets sintéticos para simular cenários reais de operação.

---

## 🧠 Funcionalidades

* Geração de dataset de telemetria (500 registros)
* Simulação de condições normais de operação
* Simulação de anomalias (falhas críticas em 3% dos dados)
* Verificação automática de:

  * Temperatura interna e externa
  * Nível de energia
  * Integridade estrutural
  * Pressão dos tanques
  * Status dos módulos críticos
  * Status da comunicação (telemetria)
* Classificação automática:

  * ✅ READY (pronto para decolar)
  * ❌ ABORT (falha detectada)
* Análise estatística:

  * Total de registros
  * Quantidade de abortos
  * Total de falhas detectadas
  * Média de falhas por ocorrência
  * Classificação dos tipos de erro

---

## 📊 Estrutura dos Datasets

### 1. `telemetria.csv`

Dataset com condições ideais (sem falhas).

### 2. `telemetria_anomalias.csv`

Dataset com inserção de anomalias em 3% dos registros.

#### Tipos de anomalias simuladas:

* Temperatura interna fora da faixa (45–70°C)
* Nível de bateria crítico (5–25%)
* Pressão fora do padrão (40–80 ou 160–220)
* Falha estrutural (`structural_integrity = 0`)
* Falha em módulos críticos (`critical_modules_status = 0`)
* Falha na comunicação (`telemetry_link_status = 0`)

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Biblioteca padrão:

  * `csv`
  * `random`
  * `datetime`

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/Matheus-Silveiraa/Aurora-Siger
```

2. Acesse a pasta:

```bash
cd Aurora-Siger
```

3. Execute o script de geração dos dados:

```bash
python telemetry.py
python telemetry_anomalys.py
```

4. Execute o analisador:

```bash
python relatorio.py
```

---

## 📈 Exemplo de Saída

```
===== telemetria.csv =====
Total de registros: 500
Prontos para decolar: 500
Abortados: 0

===== telemetria_anomalias.csv =====
Total de registros: 500
Prontos para decolar: 485
Abortados: 15
Total de falhas detectadas: 22

--- TIPOS DE FALHAS DETECTADAS ---
pressao: 5
energia: 3
temp_interna: 4
estrutura: 1
modulos: 1
telemetria: 1
```

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido como parte de uma atividade integradora com foco em:

* Lógica booleana
* Algoritmos
* Automação em Python
* Simulação de sistemas embarcados
* Análise de dados
* Detecção de anomalias

---

## 🧩 Conclusão

Através da simulação de cenários ideais e críticos, foi possível validar a eficiência do algoritmo na tomada de decisão, além de identificar os principais tipos de falhas que impactam a segurança da decolagem.

---

## 👨‍💻 Autor

Desenvolvido por **Matheus Silveira, Filipe Augusto Chaves, Marcos Henrique Xavier Nascimento**

---
