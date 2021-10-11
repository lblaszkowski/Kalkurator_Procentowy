print(
      'Menu Kalkulatora procentowego -- co chesz zrobić:  ', '\n'
      '1 - Ile wynosi liczba A % z liczby B', '\n'
      '2 - Jakim procentem liczby A jest liczbie B', '\n'
      '3 - O ile procent liczby A różni się od liczby B', '\n'
      '4 - Liczbę A powiększ o (dodaj) liczbe B', '\n'
      '5 - Liczbę A pomniejsz o (odejmij) liczbe B', '\n'
      )

wyborOpcji = float(input('Podaj liczbe z menu: '))
liczba_a = float(input('Podaj pierwszą liczbę: '))
liczba_b = float(input('Podaj drugą liczbę: '))

if wyborOpcji == 1:
    suma = (liczba_a / 100) * liczba_b
elif wyborOpcji == 2:
    suma = (liczba_a / liczba_b) * 100
elif wyborOpcji == 3:
    suma = ((liczba_b - liczba_a) / liczba_a) * 100
elif wyborOpcji == 4:
    suma = liczba_a * (1 + liczba_b / 100)
else:
    suma = liczba_a * (1 - liczba_b / 100)
print(suma)
