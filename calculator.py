a = float(input("operador a: "))
b = float(input("operador b: "))
op = input("operación: ")

match op:
    case "+":
        print(f"Suma: {a+b}")
    case "-":
        print(f"Resta: {a-b}")
    case "*":
        print(f"Multiplicación: {a*b}")
    case "/":
        print(f"División: {a/b}")
