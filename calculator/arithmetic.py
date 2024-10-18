def get_numbers():
    numbers = input("Masukan angka dengan spasi sebagai pemisahnya (gunakan titik '.' jika ingin menggunakan decimal): ")
    return [float(numbers) for numbers in numbers.split()]

def addition(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number
    return round(result, 2)

def subtraction(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return round(result, 2)

def multiplication(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return round(result, 2)

def division(numbers):
    result = numbers[0]
    try:
        for number in numbers[1:]:
            result /= number
    except ZeroDivisionError:
        return "Angka 0 ditemukan! Anda tidak bisa membagi bilangan dengan angka 0."

    return round(result, 2)