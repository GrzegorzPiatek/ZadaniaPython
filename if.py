# Wczytanie z zamiana str na float
number = float(input('number: '))

# Przykladowa instrukcja warunkowa
if number > 100:                # 1. Czy zmienna number większa od 100
    print('Number is BIG')      # Kod wykonany jezeli warunek w 1. jest prawdziwy
elif number > 10:               # 2. Czy zmienna number większa od 10
    print('Number is medium')   # Kod wykonany jezeli warunek w 2. jest prawdziwy 
else:                           # W przeciwnym wypadku
    print('Number is small')    # Kod wykonany jezeli wszytkie powyzsze warunki są falszywe
