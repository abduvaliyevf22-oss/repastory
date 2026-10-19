
while True:
    print("---------- MENYU ----------")
    print("1. Ma'lumotni o'zgartirish")
    print("2. Ma'lumotni ko'rish")
    print("3. Yoshni hisoblash")
    print("4. Dasturdan chiqish")
    print("-"*27)

    tanlov = int(input("Tanlovni kiriting: "))
    print("-"*27)

    if tanlov == 1:
        ism2 = input("Ismni kiriting: ")
        yosh2 = int(input("Yoshingizni kiriting: "))
        print("-"*27)
    elif tanlov == 2:
        print("Ism:", ism2)
        print("Yosh:", yosh2)
        print("-"*27)
    elif tanlov == 3:
        print("Ikki yoshning o'rtachasi:", (yosh2 + yosh2) / 2)
        print("-"*27)
    elif tanlov == 4:
        print("Dastur yakunlandi")
        print("-"*27)
        break

    else:
        print("Noto'g'ri tanlov!")
        print("-"*27)


