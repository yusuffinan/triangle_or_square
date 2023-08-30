question = input("  triangle or square\n")
if question == "triangle":
    print("triangle")

    k1 = int(input("kenar1"))
    k2 = int(input("kenar2"))
    k3 = int(input("kenar3"))
    if abs(k1 + k2) > k3 and abs(k1 + k3) >k2 and abs(k2+k3) >k1:
        if k1 == k2 and k1!=k3:
            print("ikizkenar üçgen")
        elif k1 == k2 and k2==k3:
            print("eşkenar üçgen")
        else:
            print("herhangi bir üçgen")
    else:
        print("üçgen belirtme şartlarına uymuyor") 

elif question == "square":
    print("square")
    k1 = int(input("kenar1"))
    k2 = int(input("kenar2"))
    k3 = int(input("kenar3"))
    k4 = int(input("kenar4"))
    if k1 == k2 and k3==k4 and k2==k3:
        print("bu dörtgen kare")
    elif k1 == k3 and k2==k4 or k2==k1 and k3==k4 or k1 == k4 and k2==k4:
        print("dikdörtgen")
    else:
        print("herhangi bir dörtgen")

else:
    print(" geçersiz değer")
