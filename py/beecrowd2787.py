chess_rows = int(input())
chess_columns = int(input())


if ((chess_columns%2) == 0 and (chess_rows%2) == 0):
    print("1")
elif ((chess_columns%2) == 1 and (chess_rows%2) == 1):
    print("1")
else:
    print("0")
