def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)

print(silnia(5))

#losujemy 3 liczby od 1 do 23
#gracz podaje 3 liczby
#sprawdzamy ile z wytypowanych przez gracza zadza się z wylosowanymi

#napisz program Quiz:
#przygotuj 5 pytań, na każde powinna być odpowiedź tak/nie
#zadawaj losowe pytania i licz punkty, jeśli gracz odpowie poprawnie
#po zadaniu 3 pytań wyświetl wynik i zakończ grę

#zrób grę MagicBall
#piszesz pytanie, a program odpowiada losowo:
#tak, nie, zdecydowanie tak, zdecydowanie nie, może, nie wiem, spróbuj później

#zrób grę w naukę tabliczki mnożenia
#program losuje 2 liczby od 1 do 10
#zadaje pytanie ile to jest liczba1 * liczba2
#sprawdza odpowiedź
#liczymy punkty, po 10 pytaniach wyświetlamy wynik i kończymy grę