from komputer import Komputer
from aplikacja import Aplikacja

mojKomp = Komputer(32)
print(mojKomp.przedstawSie())

minecraft = Aplikacja("Minecraft", 5, 6, 7)
mojKomp.uruchom(minecraft)
print(mojKomp.przedstawSie())
mojKomp.jakaApkaDziala()

#dodaj możliwość przedstawiania się aplikacji
#podmień wyświetlanie nazwy na przedstawianie się aplikacji
#dodaj możliwość zużywania procesora
#dodaj walidację (jeśli aplikacja się nie zmieści - pamięć, dysk itp - to nie uruchamiamy)
#dodaj możliwość wyłączenia aplikacji
#dodaj możliwość restartowania komputera (czyścimy pamięć, dysk itp)
#dodaj możliwość ładowania baterii (zawsze ładujemy do 100%)