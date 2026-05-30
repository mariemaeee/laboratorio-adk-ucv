from google.adk.agents import Agent

def explicar_concepto(concepto: str):

    if not concepto or not concepto.strip():
        return {
            "status": "error",
            "mensaje": "Debe ingresar un concepto"
        }

    conceptos = {
        "api": "Una API permite la comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia ordenada de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "ciberseguridad": "Protección de sistemas, redes y datos.",
        "firewall": "Sistema que controla el tráfico de red.",
        "machine learning": "Permite que una máquina aprenda de datos.",
        "cloud computing": "Uso de recursos informáticos a través de Internet.",
        "criptografia": "Protege información mediante técnicas de cifrado."
    }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado."
    }


def calcular_promedio(notas: list):

    if not isinstance(notas, list):
        return {
            "status": "error",
            "mensaje": "Debe enviar una lista."
        }

    if len(notas) == 0:
        return {
            "status": "error",
            "mensaje": "La lista está vacía."
        }

    promedio = sum(notas) / len(notas)

    return {
        "status": "success",
        "promedio": promedio
    }


root_agent = Agent(
    name="agente_ucv",
    model="gemini-2.0-flash",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    """,
    tools=[
        explicar_concepto,
        calcular_promedio
    ]
)