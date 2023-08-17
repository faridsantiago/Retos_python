def calcular_costo_estacionamiento(dia_semana, tiempo_estacionado):
    # Validar el día de la semana
    dias_validos = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    if dia_semana.lower() not in dias_validos:
        return "Día de la semana inválido. Por favor, ingrese un día válido."

    # Validar el tiempo de estacionamiento
    if tiempo_estacionado <= 0:
        return "Tiempo de estacionamiento inválido. Debe ser mayor que 0."

    # Definir tarifas por día
    tarifas = {'lunes': 2.00, 'martes': 2.00, 'miércoles': 2.00, 'jueves': 2.50, 'viernes': 2.50, 'sábado': 3.00, 'domingo': 3.00}

    # Calcular el costo
    costo_por_hora = tarifas[dia_semana.lower()]
    horas_enteras = int(tiempo_estacionado)
    fraccion = tiempo_estacionado - horas_enteras
    if fraccion > 0.0833:  # 5 minutos en horas
        horas_enteras += 1

    costo_total = costo_por_hora * horas_enteras
    return f"El costo de estacionamiento para el día {dia_semana} es: ${costo_total:.2f}"

# Ingreso de datos
dia = input("Ingrese el día de la semana: ")
tiempo = float(input("Ingrese el tiempo de estacionamiento en horas: "))

resultado = calcular_costo_estacionamiento(dia, tiempo)
print(resultado)
