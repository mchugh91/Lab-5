__author__ = 'Ciaran'

def toFahrenheit(celsius):
    return celsius * (9/5) + 32

def toKelvin(celsius):
    return celsius + 273.15

def toRakine(celsius):
    return (celsius + 273.15)*(9/5)


def main():
    c = float(input("Enter degrees in celsius:"))
    fahr = toFahrenheit(c)

    if c >= -30 and c <= -20:
        print("Arctic", fahr)
    elif c >= -19 and c <= -10:
        print("Baltic", fahr)
    elif c >= -9 and fahr <= 2:
        print("Freezing", fahr)
    elif c >= 3 and c <= 10:
        print("Chilly", fahr)
    elif c >= 11 and c <= 20:
        print("Not bad", fahr)
    elif c >= 21:
        print("Great", fahr, " degrees Fahrenheit")

    #for c in range(-30, 60, 10):
     #   print("Fahrenheit: ", toFahrenheit(c), "Kelvin: ", toKelvin(c), "Rakine: ", toRakine(c))

main()
