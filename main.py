from colorama import Fore, init

init(autoreset=True)

def win(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == a2 == a3 == user:
            return True
        return False

    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
                check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        cell = ' '.join(f[i])
        for player in ['X', 'O']:
            cell = cell.replace(player, Fore.RED + player) if player == 'X' else cell.replace(player, Fore.BLUE + player)
        print(str(i) + ' ' + cell)

def user_input(f):
    while True:
        place = input("Введите координаты: ").split()
        if len(place) != 2:
            print("Введите две координаты")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Введите два числа")
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Неверный диапазон")
            continue
        if f[x][y] != '-':
            print("Клетка занята")
            continue
        break
    return x, y

field = [['-' for _ in range(3)] for _ in range(3)]
count = 0

while True:
    if count % 2 == 0:
        user = 'X'
    else:
        user = 'O'
    show_field(field)
    x, y = user_input(field)
    field[x][y] = user
    count += 1

    if win(field, user):
        show_field(field)
        print(Fore.RED + f"Игрок {user} выиграл!")
        break
    elif count == 9:
        show_field(field)
        print("Ничья!")
        break