# Import libs 
import pyramid as p
import Archimed as A

# The main function of the project
def main():
    user_choise = int(input("Выберите функцию, которую хотите использовать 1 или 2: "))
    if user_choise == 1:
        base_1 = float(input("Введите площадь нижнего основания "))
        base_2 = float(input("Введите площадь верхнего основания "))
        height = float(input("Введите высоту усечённой пирамиды "))
        print(f"ОбЪём усечённой пирамиды составляет {p.Value(base_1, base_2, height)} кубических единиц")
    elif user_choise == 2:
        mass = float(input("Введите массу: "))
        volume = float(input("Введите объём погружённой части: "))
        density = float(input("Введите плотность: "))
        A.plav(mass, volume, density)
    else:
        print('выберите из 1 или 2')



if __name__ == "__main__":
    main()