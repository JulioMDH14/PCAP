filas = []
sudoku_ok = False
for i in range(9):
    linea = input('Linea ' + str(i) + ': ')
    if len(linea) == 9 and linea.isnumeric() and sorted(linea) == list("123456789"):
        sudoku_ok = True
        filas.append(linea)

if sudoku_ok:
    print('Sudoku SÍ es válido')
else:
    print('Sudoku NO es válido')