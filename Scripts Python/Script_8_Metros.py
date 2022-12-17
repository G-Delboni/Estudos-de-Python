metros = float(input('Digite a medida em metros '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
cent = metros * 100
mili = metros * 1000

print(f'{metros} metros é equivalente a:\n{km} km\n{hm} hm \n{dam} dam \n{cent:.0f} cm \n{mili:.0f} mm')