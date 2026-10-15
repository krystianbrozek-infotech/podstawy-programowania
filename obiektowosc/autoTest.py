from auto import Auto

mojaTojotka = Auto()
mojaTojotka.stanBaku()
#mojaTojotka.zatankuj(21)
if mojaTojotka.jedz(150):
    print("To była wspaniała wycieczka!")
else:
    print("Ale bieda! Zatankuj najpierw!!!")
mojaTojotka.stanBaku()