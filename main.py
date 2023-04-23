win_state = False
playing_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
positionX = []
positionO =[]
counter=0
win_coord = ((1,2,3), (1,5,9), (1,4,7), (2,5,8), (4,5,6), (7,8,9), (3,6,9), (3,5,7))
player=''
while win_state == False:
    valid = True
    if counter % 2 == 0:
        player = 'O'
        print('ход игрока О:')
        for field in range (len(playing_field)):
            if field == 0:
                print(' | ', end='')
            if field == 3 or field == 6:
                print ('\n', '| ' , end='')
            print(playing_field[field], '| ', end='')
        position = int(input("""
Куда поставить O?"""))
        if playing_field[position-1] == 'X' or playing_field[position-1] == 'O':
            print('Клетка занята! Попробуй другую!')
            valid == False
            while valid == False:
                position = int(input("""
Куда поставить O?"""))
        else:
            valid == True
            counter +=1
            playing_field[position-1]= player
            positionO.append(position)
    else:
            player= 'X' 
            print('ход игрока X:')
            for field in range (len(playing_field)):
                if field == 0:
                    print(' | ', end='')
                if field == 3 or field == 6:
                    print ('\n', '| ' , end='')
                print(playing_field[field], '| ', end='')
            position = int(input("""
Куда поставить X?"""))
            if playing_field[position-1] == 'X' or playing_field[position-1] == 'O':
                print('Клетка занята! Попробуй другую!')
                valid == False
                while valid == False:
                    position = int(input("""
Куда поставить X?"""))
            else:
                valid == True
                counter +=1
                playing_field[position-1]= player
                positionX.append(position)
    if counter > 4:
        if tuple(positionO) in win_coord:
            print ('O победил!')
            win_state = True
        elif tuple(positionX) in win_coord:
            print('Х победил!')
            win_state = True
        elif counter >= 9:
             print('Ничья!')
             break
