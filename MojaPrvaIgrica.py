print("Dobrodosli u moju prvu igricu!")
name = input("Koje je tvoje ime? ")
age = int(input("Kolko godina imas? "))

zivota = 10

if age >= 18:
    print("Dovoljno imas godina!")

    wants_to_play = input("Da li zelis igrati? ").lower()
    if wants_to_play == "da":
        print("Ti startujes sa", zivota, "zivota")
        print("Pocni igrati!")

        left_or_right = input("Prvi izbor levo ili desno (levo/desno)? ")
        if left_or_right == "levo":
            ans = input("Bravo sledi stazu i stizes pravo do jezera...Plivam ili idem okolo (plivam/okolo)? ")

            if ans == "okolo":
                print("Otisli ste na drugu stranu i stigli ste na jezero.")
            elif ans == "plivam":
                print("Uspeli ste da predjete preko.. Ali vas je ugrizla riba i izgubi li ste 5 zivota.")
                zivota -= 5

            ans = input("Primecujete kucu i reku...Do koga idete (kuca/reka)? ")
            if ans == "kuca":
                print("Udjete u kucu i izgubite zdravlje oduzima vam se 5 zivota")
                zivota -= 5

                if zivota <= 0:
                    print("Sada imate 0 zivota i izgubili ste igru...")
                else:
                    print("Preziveli ste pobedili ste!")

            else:
                print("Pao si u reku i udavio si se...")


        else:
            print("Pao si i izgubio")

    else:
        print("Vidimo se")
else:
    print("Nemas dovoljno godina da bi igrao igricu!")
