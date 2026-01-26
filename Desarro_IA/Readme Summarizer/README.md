# 📝 README Summarizer - AI Project

Este proyecto es una aplicación web de Inteligencia Artificial que permite resumir textos técnicos (como archivos README o documentación de software) de forma automática en ingles. Utiliza una arquitectura moderna con **FastAPI** en el Backend y un modelo de lenguaje preentrenado de **Hugging Face**.

## 🚀 Características Técnicas

- **IA Modelo:** `sshleifer/distilbart-cnn-12-6` (una versión optimizada y ligera de BART).
- **Backend:** FastAPI con validación de datos mediante **Pydantic**.
- **Frontend:** Interfaz limpia en modo oscuro (HTML/CSS/JS) con estados de carga.
- **Optimización:** Implementa truncado de texto (1024 tokens) para evitar errores de desbordamiento de memoria.

## 🛠️ Requisitos e Instalación

### 1. Entorno Virtual
Se recomienda utilizar Python 3.12+. Para crear e instalar las dependencias:

```bash
# Con uv (recomendado)
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Con venv tradicional
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt