print("=== FITNESS & INVEST CALCULATOR ===\n")

# --- IMC ---
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"\nTu IMC es: {round(imc,2)}")

if imc < 18.5:
    print("Estado: Bajo peso")
elif 18.5 <= imc < 25:
    print("Estado: Normal")
elif 25 <= imc < 30:
    print("Estado: Sobrepeso")
else:
    print("Estado: Obesidad")

# --- Inversión ---
print("\n--- Simulador de Inversión ---")

capital = float(input("Capital inicial: "))
tasa = float(input("Tasa mensual (%): ")) / 100
meses = int(input("Cantidad de meses: "))

resultado = capital * ((1 + tasa) ** meses)

print(f"\nValor futuro estimado: {round(resultado,2)}")
print("\nGracias por usar el sistema 🚀")
print("Nueva versión funcionando")
