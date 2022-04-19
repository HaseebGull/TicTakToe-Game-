# create board using dictionf

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_key = []

for key in theBoard:
    board_key.append(key)
 #
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#main functionallity of game
def game():
    try:


        turn = 'X'
        count = 0

        for i in range(10):
            printBoard(theBoard)
            print("It's your turn," + turn + ".Move to which place?" )

            move = input()

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count +=1
            else:
                print("the plce is already fill choose another one")
                continue

            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                    print("\n game over")
                    print("****" + turn + "won the game")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard ['6'] != ' ':
                    print("\n game over")
                    print("***" +turn+ " won the game")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    print("\n game over")
                    print("***" + turn + " won the game")
                    break
                elif theBoard['7'] == theBoard['4'] == theBoard['1'] !=' ':
                    print("\n game over")
                    print("***" +turn+ " wont the game")
                    break
                elif theBoard['8'] == theBoard['5'] == theBoard ['2'] !=' ':
                    print("\n game over")
                    print("***" +turn+ " won the game")
                    break
                elif theBoard['9'] == theBoard['6'] == theBoard['3'] !=' ':
                    print("\n game over")
                    print("***" +turn+ " won the game ")
                    break
                elif theBoard['7']== theBoard['5'] == theBoard['3'] !=' ':
                    print("\n game over")
                    print("***" +turn+ "won the game")
                    break
                elif theBoard['9'] == theBoard['5'] == theBoard["1"] !=' ':
                    print("\n game over")
                    print("***" +turn+ " won the game")
                    break

            if count == 9:
                print("\n game over")
                print("the game is tied")

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
    except Exception as e:
        print("wrong input ")
        game()

if __name__ == '__main__':

    game()


