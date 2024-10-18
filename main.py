from calculator import get_numbers, addition, subtraction, multiplication, division
import sys

def main():
    while True:
        operations = {
            "1": ("Penjumlahan", addition),
            "2": ("Pengurangan", subtraction),
            "3": ("Perkalian", multiplication),
            "4": ("Pembagian", division)
        }
        print("==========================")
        print("Aplikasi Kalkulator")
        print("==========================")
        print("Pilih operasi aritmatika!")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("==========================")

        print("Masukan selain angka di atas jika ingin keluar program!")
        choice = input("Masukan Pilihan Anda: ")
        if choice not in operations.keys():
            print("Keluar Program!")
            break

        try:
            numbers = get_numbers()
            if len(numbers) <= 1:
                sys.exit("Anda harus memasukan minimal 2 angka")

            operation_name, function_name = operations[choice]
            result = function_name(numbers)
            print(f"Hasil: {result}")
        except ValueError:
            print("Terjadi kesalahan! Pastikan Anda memasukan angka dengan spasi sebagai pemisahnya")
        except Exception as e:
            print(f"Terjadi kesalahan {e}")


if __name__ == "__main__":
    main()