# Take mass, volume and density and return is object floats in the water

# Finding function
def plav(m, V, po):
    if po > 1:
        print("предмет не является плавучим")
    elif po == 1:
        print("предмет является частично плавучим")
    else:
        print("предмет является плавучим")


# Main function
def main():
    mass = float(input("Введите массу: "))
    volume = float(input("Введите объём погружённой части: "))
    density = float(input("Введите плотность: "))
    plav(mass, volume, density)

if __name__ == "__main__":
    main()