def check_winner(board, abhinav_choice, anjali_choice):
    n = 3
    
    for i in range(n):
        if all (board[i][j] == abhinav_choice for j in range(n)):
            return "Abhinav Wins"
        if all(board[i][j] == anjali_choice for  j in range(n)):
            return "Anjali Wins"
            
        if all (board[j][i] == abhinav_choice for j in range(n)):
            return "Abhinav Wins"
        if all(board[j][i] == anjali_choice for  j in range(n)):
            return "Anjali Wins"
            
    if all (board[i][i] == abhinav_choice for i in range(n)):
            return "Abhinav Wins"
    if all(board[i][i] == anjali_choice for  i in range(n)):
            return "Anjali Wins"
            
    
    if all (board[i][n - 1 - i] == abhinav_choice for i in range(n)):
            return "Abhinav Wins"
    if all(board[i][n - 1 - i] == anjali_choice for  i in range(n)):
            return "Anjali Wins"
            
    return "Tie"
    
   
board = []
    
for i in range(3):
    row = input().strip().split()
    board.append(row)
                
         
abhinav_choice = "O"
anjali_choice = "X"
        
print(check_winner(board, abhinav_choice, anjali_choice))
