class calcu:
    
    def suma(self, num1, num2) -> str:
        return "la suma es: {}".format(num1 + num2)
    
    def resta(self, num1, num2) -> str:
        return "la resta es: {}".format(num1 - num2)
    
    def multi(self, num1, num2) -> str:
        return "la multiplicacion es: {}".format(num1 * num2)
    
    def div(self, num1, num2) -> str:
        return "la division es: {}".format(num1 / num2)

def main():
    calc = calcu()
    opt = -1
    
    while opt != 0:
        print(" -OperaBass- \nEscriba una opcion:\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n0.-Salir")
        opt = int(input('Accion: '))
        match opt:
            case 1:
                num1 = int(input('Num1: '))
                num2 = int(input('Num2: '))
                print(calc.suma(num1, num2))
            case 2:
                num1 = int(input('Num1: '))
                num2 = int(input('Num2: '))
                print(calc.resta(num1, num2))
            case 3:
                num1 = int(input('Num1: '))
                num2 = int(input('Num2: '))
                print(calc.multi(num1, num2))
            case 4:
                num1 = int(input('Num1: '))
                num2 = int(input('Num2: '))
                print(calc.div(num1, num2))
            case 0:
                print("Gracias por utilizarme!")
                break
            case _:
                print("No Invalida")

if __name__ == '_main_':
    main()