def prmatrix_Rows(mat):
    for r_index ,r in enumerate(mat):
        for v_index ,v in enumerate(r):
            print(f"Row index: {v_index} | Value: {v}")
        print()
        
def prmatrix_Columns(mat):
    col_index = 0
    for i in range(0, len(mat)):
        print(f"Col index {i}:", end=" ")
        for j in range(0, len(mat)):
            print(f"{mat[j][col_index]}", end=" ")
        print()
        col_index += 1 
        
def prmatrix_Diagonals(mat):
    print("Dia index:", end="")
    for i in range(0, len(mat)):
        print(f" {mat[i][i]}", end=" ")
        
    print()
    print("Dia rev index:", end="")
    for i in range(0, len(mat)):
        print(f" {mat[i][len(mat) - i - 1]}", end=" ")

matrix_arr =[    
            [1,2,3],
            [4,5,6],
            [7,8,9], 
        ]
u_input = int(input("INPUT: "))
match u_input:
    case 1:
        prmatrix_Rows(matrix_arr)
    case 2:
        prmatrix_Columns(matrix_arr)
    case 3:
        prmatrix_Diagonals(matrix_arr)
    case _:
        print("No matching case found.")