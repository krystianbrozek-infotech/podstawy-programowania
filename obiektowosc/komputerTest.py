from komputer import Komputer
from aplikacja import Aplikacja

mojKomp = Komputer(32)
print(mojKomp.przedstawSie())

minecraft = Aplikacja("Minecraft", 5, 6, 7)
mojKomp.uruchom(minecraft)
print(mojKomp.przedstawSie())
mojKomp.jakaApkaDziala()