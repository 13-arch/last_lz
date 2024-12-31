


import math as m



sred = lambda L1,L2: m.sqrt(L1/L2)


def main():
    L1 = float(input("Введите болометрический показатель звезды: "))
    L2 = float(input("Введите болометрический показатель солнца:  "))
    print("средний радиус обитаемой зоны равнен",sred(L1,L2))

if __name__ == "__main__":
    main()