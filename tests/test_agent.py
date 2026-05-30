# tests/test_agent.py

from agente_ucv.agent import calcular_promedio

def test_promedio():
    resultado = calcular_promedio([10,20,30])
    assert resultado["promedio"] == 20