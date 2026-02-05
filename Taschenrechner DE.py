# Taschenrechner
# Erstellt von Klaus Barth Rochol

def taschenrechner():
    while True:
        # Eingaben
        num1 = float(input("Gib die erste Zahl ein: "))
        oper = input("Welche Rechenoperation? (+, -, /, *): ")
        num2 = float(input("Gib die zweite Zahl ein: "))
        
        # Berechnung
        if oper == "+":
            ergebnis = num1 + num2
        elif oper == "-":
            ergebnis = num1 - num2
        elif oper == "/":
            if num2 == 0:
                print("Fehler: Division durch 0 ist nicht möglich!")
                continue
            ergebnis = num1 / num2
        elif oper == "*":
            ergebnis = num1 * num2
        else:
            print("Ungültige Operation!")
            continue
        
        # Ausgabe
        print(f"Deine Rechnung: {num1} {oper} {num2}")
        print(f"Ergebnis: {ergebnis}")
        
        # Weitermachen?
        weiter = input("\nWillst du weiter rechnen? (ja/nein): ").lower()
        if weiter != "ja":
            print("Bis bald!")
            break

# Programm starten
taschenrechner()