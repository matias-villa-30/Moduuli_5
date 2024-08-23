import math
alkuluku = int(input("Anna alkuluku numero: "))
on_alkuluku = True

for i in range(2, int(math.sqrt(alkuluku)) + 1):
    if alkuluku % i == 0:
        on_alkuluku = False

if on_alkuluku == True:
    print("on alkuluku")

else:
    print("ei ole alkuluku")