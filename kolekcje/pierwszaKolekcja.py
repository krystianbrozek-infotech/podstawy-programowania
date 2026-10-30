slowa = []
slowo = None

while slowo != "":
    slowo = input("Podaj słowo: ")
    if slowo != "":
        slowa.append(slowo)
    

nr = 1
for s in slowa:
    print(f"{nr}. {s}")
    nr+=1

print(f"Tyle jest słów: {len(slowa)}")
pierwsze = slowa[0]
ostatnie = slowa[len(slowa)-1]

print(pierwsze, ostatnie)