
#find the volume of the truncated pyramid
import math as m

# Finding lambda function
Value = lambda osn_1, osn_2, height: height / 3 * (osn_1 + osn_2 + m.sqrt(osn_1 * osn_2))


# Main function
def main():
    osn_1 = float(input("Введите площадь нижнего основания "))
    osn_2 = float(input("Введите площадь верхнего основания "))
    height = float(input("Введите высоту усечённой пирамиды "))
    print(f"ОбЪём усечённой пирамиды составляет {Value(osn_1, osn_2, height)} кубических единиц")

if __name__ == "__main__":
    main()