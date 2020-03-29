matriz = [['# ','# ','# ','# ','# ','# ','# ','# ','# ','# '],
          ['# ','  ','  ','  ','# ','# ','  ','  ','  ','# '],
          ['# ','  ','# ','  ','  ','# ','  ','# ','  ','# '],
          ['# ','  ','# ','# ','  ','# ','  ','# ','  ','# '],
          ['# ','  ','  ','# ','  ','  ','  ','# ','  ','# '],
          ['# ','  ','# ','# ','# ','# ','  ','# ','  ','# '],
          ['# ','  ','# ','  ','  ','  ','  ','# ','  ','# '],
          ['# ','# ','# ','# ','# ','# ','# ','# ','# ','# ']]


def Up(tuple):
    x,y = tuple
    return x - 1,y

def Down(tuple):
    x,y = tuple
    return x + 1,y

def Left(tuple):
    x,y = tuple
    return x,y - 1

def Right(tuple):
    x,y = tuple
    return x,y + 1


def Print(tuple):
    x,y = tuple
    matriz[x][y] = '- '
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                print(matriz[i][j], end='')
                print()
            else:
                print(matriz[i][j], end='')

def Move(ponteiro):
    caminho = ponteiro
    direcionais = [Up,Down,Left,Right]
    Print(caminho)
    for i in direcionais:
        x,y = i(caminho)
        if matriz[x][y] == '  ':
            caminho = i(caminho)
            Move(caminho)
        elif caminho == (6,9):
            print('GAnhou')
            break
        else:
            pass


ponteiro = (1, 1)
Move(ponteiro)