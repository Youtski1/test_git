
primer = input("Введи пример1:")


def calculator(primer: str) -> int:
    result = eval(f"{primer}")
    return result

print(f"Ответ: {calculator(primer)}")