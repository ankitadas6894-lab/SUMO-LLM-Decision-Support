# IntelliRoute: LLM-Driven Traffic Decision Support

An intelligent transportation system that integrates **SUMO (Simulation of Urban Mobility)** with local Large Language Models (**Llama-2** and **Phi-3**) to provide real-time routing advice and traffic reasoning.

## 🚀 Features
* **Traffic Simulation:** Realistic urban vehicle flow using SUMO.
* **LLM Integration:** Utilizes local LLMs via LM Studio/Ollama for decision-making.
* **Dual Model Comparison:** Compare routing logic between Llama-2 and Phi-3.
* **FastAPI Backend:** A robust bridge between the simulation data and the AI models.

## 📁 Project Structure
* `src/`: Python scripts for TraCI data collection and LLM logic.
* `network/`: SUMO configuration files (.net.xml, .rou.xml, .sumocfg).
* `web/`: HTML dashboards for visualizing model results.
* `results/`: Performance graphs and JSON data logs.

## 🛠️ Getting Started
1. **Prerequisites:** - Install [SUMO](https://sumo.dlr.de/docs/Installing/index.html).
   - Install [Python 3.10+](https://www.python.org/).
2. **Setup:**
   ```bash
   pip install -r requirements.txt