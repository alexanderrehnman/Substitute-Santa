def main():

    öppna_skapa= int(input("Ifall du vill skapa önskelista tryck 1. Ifall du vill öppna önskelista tryck 2: "))

    if öppna_skapa==1:
        önskelista = input("vad ska önskelistan heta?: ")
        namn = input("Vad heter personen?: ")
        antal = int(input("Hur många grejer vill du skriva in?: "))

        for saker in antal[0,antal]:



         with open("önskelista.txt", "w", encoding="utf8") as önskelista:
             önsk= önskelista.readlines()

main()