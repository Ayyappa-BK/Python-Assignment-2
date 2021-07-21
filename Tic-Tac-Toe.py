board_format = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
board_keys = []

for key in board_format:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' +board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' +board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' +board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(board_format)
        print("It's your turn, "+turn + ". Move to which place?")
        move = input()

        if board_format[move] == ' ':
            board_format[move] = turn
            count+=1
        else:
            print("That place is already filled.\nMove to which place? ")
            continue

        if count>=5:
            if board_format['7']==board_format['8']==board_format['9']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
            elif board_format['4']==board_format['5']==board_format['6']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
            elif board_format['1']==board_format['2']==board_format['3']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
            elif board_format['1']==board_format['4']==board_format['7']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
            elif board_format['2']==board_format['5']==board_format['8']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
            elif board_format['3']==board_format['6']==board_format['9']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
            elif board_format['7']==board_format['5']==board_format['3']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
            elif board_format['1']==board_format['5']==board_format['9']!=' ':
                printBoard(board_format)
                print("\nGAME OVER.\n")
                print(" **** "+turn+" Won. ****")
                break
        if count==9:
            print("\nGAME OVER.\n")
            print("It's a  Tie!")
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play again? (Y/N)")
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            board_format[key] = " "

        game()

if __name__ == "__main__":
    game()