def check_stock(material_name, material_quantity):
    stock = {}
    stock_list = open('stock_list.txt', 'r')

    for line in stock_list:
        item, quantity = line.strip().split(',')
        stock[item] = int(quantity)

    stock_list.close()

    if material_name in stock:
        if stock[material_name] >= material_quantity:
            return f"Stok {material_name} yang tersedia cukup."
        else:
            return f"Stok {material_name} yang tersedia tidak cukup."
    else:
        return f"Material {material_name} tidak ada dalam daftar."


def add_material(material_name, material_quantity):
    stock = {}
    stock_list = open('stock_list.txt', 'r')

    for line in stock_list:
        item, quantity = line.strip().split(',')
        stock[item] = int(quantity)

    stock_list.close()

    if material_name in stock:
        stock[material_name] += material_quantity
    else:
        stock[material_name] = material_quantity

    with open('stock_list.txt', 'w') as stock_list:
        for item, quantity in stock.items():
            stock_list.write(f"{item},{quantity}\n")

    return f"{material_quantity} {material_name} berhasil ditambahkan."


def main():
    print("1. Cek Stok")
    print("2. Tambah Material")
    print("3. Keluar")

    choice = int(input("Pilih Opsi: "))

    while choice != 3:
        if choice == 1:
            material_name = input("Masukkan nama material: ")
            material_quantity = int(input("Masukkan jumlah material: "))
            print(check_stock(material_name, material_quantity))

        elif choice == 2:
            material_name = input("Masukkan nama material: ")
            material_quantity = int(input("Masukkan jumlah material: "))
            print(add_material(material_name, material_quantity))

        choice = int(input("Pilih Opsi: "))

    print("Keluar dari program.")


if __name__ == "__main__":
    main()
