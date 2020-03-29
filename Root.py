matriz = [[9,9,9,9,9,9,9,9,9,9],
          [9,0,0,0,9,9,0,0,0,9],
          [9,0,9,0,0,9,0,9,0,9],
          [9,0,9,9,0,9,0,9,0,9],
          [9,0,0,9,0,0,0,9,0,9],
          [9,0,9,9,9,9,0,9,0,9],
          [9,0,9,0,0,0,0,9,0,9],
          [9,9,9,9,9,9,9,9,9,9]]

labels_print= {
    '9': '# ',
    '0': '  ',
    '1': '- ',
    '2': '  '
}

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
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                print(labels_print[f'{matriz[i][j]}'], end='')
                print()
            else:
                print(labels_print[f'{matriz[i][j]}'], end='')


def Move(ponteiro):
    caminho = ponteiro
    direcionais = [Down,Right,Left,Up]
    for i in direcionais:
        x,y = i(caminho)
        if matriz[x][y] == 9:
            pass
        elif matriz[x][y] == 0:
            caminho = x,y
            matriz[x][y] = 1
            if caminho == (6, 8):
                print('Ganhou')
                print(caminho)
                Print(caminho)
                break
            Move(caminho)
            if matriz[x][y] == 1:
                matriz[x][y] = 2

ponteiro = (1, 1)
Move(ponteiro)

