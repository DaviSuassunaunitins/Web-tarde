num = float(input("Quanto você gastou em compras online: "))
desconto = 0
if num >= 100:
    desconto = num * 0.1
    num = num - desconto
    print("Seu desconto será de: " + str(round(desconto, 2)))
else:
    print("Você não receberá desconto.")
print("Preço final: " + str(round(num, 2)))