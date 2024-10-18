from calculator import get_numbers, addition, subtraction, multiplication, division
import sys

def main():
    while True:
        print("==========================")
        print("Aplikasi Kalkulator")
        print("==========================")
        print("Pilih operasi aritmatika!")
        print("1.Penjumlahan")
        print("2.Pengurangan")
        print("3.Perkalian")
        print("4.Pembagian")
        print("==========================")

        print("Masukan selain angka di atas jika ingin keluar program!")
        choice = input("Masukan Pilihan Anda: ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("Keluar Program!")
            break

        try:
            numbers = get_numbers()
            if len(numbers) <= 1:
                sys.exit("Anda harus memasukan minimal 2 angka")
            else:
                if choice == "1":
                    print(f"Hasil: {addition(numbers)}")
                    break
                if choice == "2":
                    print(f"Hasil: {subtraction(numbers)}")
                    break
                if choice == "3":
                    print(f"Hasil: {multiplication(numbers)}")
                    break
                if choice == "4":
                    print(f"Hasil: {division(numbers)}")
                    break
        except ValueError as e:
            print("Terjadi kesalahan! Pastikan Anda memasukan angka dengan spasi sebagai pemisahnya")
            break


if __name__ == "__main__":
    main()