def smart_computer():
    """Let the user pick a number between 0 and 1000,
    user gives clues and application tries to guess in 10 moves.

    :return: guess attempts by a program, ends with 'Victory!' exclamation.
    """
    input("Pomyśl liczbę od 1 do 1000, a ja ją zgadnę w 10 ruchach. Gotowy? ")
    max_num = 1000
    min_num = 0
    while 1 != 0:
        guess = int((max_num - min_num) / 2) + min_num
        print(f"Zgaduję: {guess}")
        response = input()
        if response == "za dużo":
            max_num = guess
        elif response == "za mało":
            min_num = guess
        elif response == "zgadłeś":
            return "Wygrałem!"
        else:
            print("Nie oszukuj! Wprowadź poprawną odpowiedź.")


print(smart_computer())
