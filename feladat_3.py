import random
szamlalo = 0

for i in range(20):
    veletlen_szam = random.randint(1, 12)
    if veletlen_szam % 3 == 0:
        print(veletlen_szam)
        szamlalo += 1
print("3-mal osztható számok darabja:", szamlalo)