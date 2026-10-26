DEFAULT_MIN_LENGTH = 12
SPECIAL_CHARS = set("!@#$%^&*")

# Przypadki testowe: nazwa przypadku -> hasło
TEST_CASES = {
    "puste hasło": "",
    "hasło za krótkie": "admin",
    "brak wielkiej litery": "password123!",
    "brak cyfry": "PasswordTest!",
    "brak znaku specjalnego": "Password1234",
    "spacje na brzegach": " Password123! ",
    "hasło poprawne": "VeryStrongPassword2026!",
}


def validate_password(password, min_length):
    problems = []

    # Sprawdzenie czy hasło jest puste
    if password == "":
        problems.append("hasło nie może być puste")
        return False, problems

    # Sprawdzenie minimalnej długości hasła
    if len(password) < min_length:
        problems.append(f"hasło jest za krótkie (minimum {min_length} znaków)")

    # Sprawdzenie czy hasło zaczyna się lub kończy spacją
    if password.startswith(" ") or password.endswith(" "):
        problems.append("wykryto spację na początku lub na końcu hasła")

    # Zmienne logiczne opisujące znalezione typy znaków
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    #Przejście po wszystkich znakach hasła i sprawdzenie ich typów
    for char in password:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char in SPECIAL_CHARS:
            has_special = True

    if not has_lower:
        problems.append("brak małej litery")
    if not has_upper:
        problems.append("brak wielkiej litery")
    if not has_digit:
        problems.append("brak cyfry")
    if not has_special:
        problems.append("brak znaku specjalnego (!@#$%^&*)")

    #Hasło jest poprawne, jeśli nie znaleziono żadnych problemów i zwracamy wynik oraz listę problemów
    is_valid = len(problems) == 0
    return is_valid, problems

#Funkcja do prezentacji wyniku walidacji hasła. Celowo nie przyjmuje hasła, więc nie może go wypisać.
def print_result(is_valid, problems, test_name=None):
    """Prezentacja wyniku. Celowo nie przyjmuje hasła, więc nie może go wypisać."""
    if test_name is not None:
        print(f"\nPrzypadek testowy: {test_name}")

    if is_valid:
        print("Wynik: PASS - hasło spełnia politykę.")
    else:
        print("Wynik: FAIL - hasło nie spełnia polityki.")
        print("Znalezione problemy:")
        for problem in problems:
            print("-", problem)

#Funkcja do pobrania minimalnej długości hasła od użytkownika. Zwraca liczbę albo N
def get_min_length():
    """Pobiera minimalną długość. Zwraca liczbę albo None przy błędnej konfiguracji."""
    value = input(f"Podaj minimalną długość hasła (Enter = {DEFAULT_MIN_LENGTH}): ")

    if value == "":
        return DEFAULT_MIN_LENGTH

    try:
        min_length = int(value)
        if min_length < 1:
            raise ValueError
    except ValueError:
        print("Błąd konfiguracji: minimalna długość musi być dodatnią liczbą całkowitą.")
        return None

    return min_length


def run_test_cases(min_length):
    for test_name, test_password in TEST_CASES.items():
        is_valid, problems = validate_password(test_password, min_length)
        print_result(is_valid, problems, test_name)


def main():
    min_length = get_min_length()
    if min_length is None:
        return  # błędna konfiguracja - nie kontynuujemy

    # Trzeba odkomentować, żeby uruchomić przypadki testowe (punkt 8):
    # run_test_cases(min_length)
    # return

    #Pobranie hasła
    password = input("Podaj hasło: ")

    #Sprawdzenie hasła
    is_valid, problems = validate_password(password, min_length)
    print_result(is_valid, problems)


if __name__ == "__main__":
    main()