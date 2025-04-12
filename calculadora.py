def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
  
def division(a, b):
    return a / b if b != 0 else 'Error: división por cero'


def division(a, b):
    return a / b if b != 0 else 'Error: la división por cero xd'

def mostrar_menu():
    print("\nCalculadora colaborativa")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        if opcion not in ('1', '2', '3', '4'):
            print("Opción no válida. Intente de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Debe ingresar números válidos.")
            continue

        if opcion == '1':
            resultado = suma(num1, num2)
        elif opcion == '2':
            resultado = resta(num1, num2)
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
        elif opcion == '4':
            resultado = division(num1, num2)

        print(f"\nResultado: {resultado}")

if __name__ == "__main__":
    main()
