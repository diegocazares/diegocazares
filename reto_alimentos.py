# Función para calcular un prestamo hipotecario
def hipotecario(riesgo, tasa_interes, plazo):
    # Calcular el interés compuesto
    calcular_riesgo_prestamo(monto_prestamo,tasa_interes,plazo)
  tasa_interes, plazo_prestamo):
if tasa_interes <= 5  and plazo_prestamo <=5:
      return "Bajo riesgo" 
elif tasa_interes > 5 or plazo_prestamo>5:
    return "Riesgo moderado"
else:
    return "Alto riesgo"
  
# Solicita al usuario los datos del prestamo
monto_prestamo = float(input("Ingrese el monto del prestamo: "))
tasa_interes = float(input("Ingrese la tasa de interés: "))
plazo_prestamo = int(input("Ingrese el plazo del prestamo (en meses): "))

# Calcular el nivel de riesgo del prestamo
nivel_riesgo = hipotecario(monto_prestamo, tasa_interes, plazo_prestamo)

# Muestra el resultado
print("El nivel de riesgo del prestamo es:", nivel_riesgo)- 👋 
--->
