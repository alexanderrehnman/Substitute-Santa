def main():

    öppna_skapa= int(input("Ifall du vill skapa önskelista tryck 1. Ifall du vill öppna önskelista tryck 2: "))
    
    global önskelista


    if öppna_skapa==1:
        önskelista = input("vad ska önskelistan heta?: ")
        with open( önskelista +".txt", "w", encoding="utf8") as önskelista:
            print("mata in din önskelista")
            namn = input("Vad heter personen?: ")

            while True:
        
                present = input("skriv in dina presenter. avsluta genom att trycka h: ")
                if "h" in present:
                    break
                    
                else:
                    önskelista.write(f"{present}\n")


main()