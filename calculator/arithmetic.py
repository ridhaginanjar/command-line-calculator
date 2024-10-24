def get_numbers():
    numbers = input("MASUKAN ANGKA => Masukan angka dengan spasi sebagai pemisahnya (gunakan titik '.' jika ingin "
                    "menggunakan decimal): ")

    # Split and convert numbers into float
    try:
        number_list = [float(numbers) for numbers in numbers.split()]
    except ValueError:
        raise ValueError("Masukan angka dengan spasi sebagai pemisah dan gunakan '.' ketika menggunakan decimal.")

    # Handling input number less than one
    if len(number_list) <= 1:
        raise ValueError("Harap masukan Angka lebih dari satu!")

    return number_list


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