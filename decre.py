"""
Crea un programa en Python que inicie con
 un valor inicial de 50. El programa debe reducir este valor en 10 unidades por iteración y mostrar el valor restante después de cada decremento. El proceso continuará hasta que el valor llegue a 0. Al finalizar, el programa debe indicar cuántas iteraciones fueron necesarias para alcanzar el 0.
"""

valor_inicial=50


decremento = 10
iteraciones=0 

while valor_inicial > 0:
    valor_inicial -= decremento
    iteraciones += 1
    print(valor_inicial)
print("cantidad",iteraciones)
