import socket
import time

def solve_maze(host, port, team_code, moves):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(s.recv(1024).decode())  

        
        s.sendall((team_code + '\n').encode())
        print(s.recv(1024).decode())  

        
        for move in moves:
            s.sendall((move + '\n').encode())
            response = s.recv(1024).decode()
            print(response)
            
            if "Congratulations" in response or "Connection closed" in response:
                break  

        
        remaining_response = s.recv(1024).decode()
        print(remaining_response)

# Team code and moves
host = "178.128.214.190"
port = 7777
team_code = input("Team Code: ")
moves = [
    'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 
    'R', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 
    'R', 'R', 'R', 'R', 'R', 'R', 'U', 'U', 
    'R', 'R', 'R', 'R', 'U', 'U', 'R', 'R', 
    'U', 'U', 'R', 'R', 'R', 'R', 'U', 'U', 
    'R', 'R', 'R', 'R', 'U', 'U', 'R', 'R', 
    'D', 'D', 'D', 'D', 'R', 'R', 'D', 'D', 
    'R', 'R', 'D', 'D', 'R', 'R', 'D', 'D',
    'R', 'R', 'U', 'U', 'R', 'R', 'D', 'D',
    'D', 'D', 'D', 'D', 'D', 'R'
]  

solve_maze(host, port, team_code, moves)
