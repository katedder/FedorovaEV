# A tic-Tac-Toe board by Fedorova E.V. PDEV_60


size = 3
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    print('_' * 4 * size)
    for i in range(size):
        print((' ' * 3 + '|')*3)
        print('', board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print(('_'*3+'|')*3)
    pass

def game_step(index, char):
    if(index>9 or index<1 or board[index-1] in ('X', 'O')):
        return False
    board[index-1]=char
    return True
    pass

def winner_check():
    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for position in win_combination:
        if (board[position[0]] == board[position[1]] and board[position[1]] == board[position[2]] and board[position[1]] in ('X','O')):
            win = board[position[0]]
    return win

def start_game():
    current_player = 'X'
    step = 1
    draw_board()
    while (step < 9) and (winner_check() == False):
        index = input('Ходит ' + current_player + '. Введите номер поля (для выхода нажмите E):')
        if(index == 'E'):
            break

        if(game_step(int(index), current_player)):
            print('Ход выполнен')

            if (current_player =='X'):
                current_player = '0'
            else:
                current_player = 'X'


            draw_board()
            step += 1

        else:
            print('Неверный номер! Повторите ход!')
    if (step == 9):
        print('Ничья')
    else:
        print('Победа '+ winner_check())

print('Старт игры')
start_game()





