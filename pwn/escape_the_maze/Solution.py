import socket
import time

escape_path = [
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

def main():
    server_ip = '127.0.0.1'  
    server_port = 7777

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        
        team_code = "demo_team_code"
        s.sendall(team_code.encode())  

        start_time = time.time()
        time_limit = 30  

        index = 0  
        path_string = ""  

        while True:
            response = s.recv(4096).decode()
            print(response)
            if "Congratulations" in response or "Time's up" in response:
                break
            
            if time.time() - start_time < time_limit:
                if index < len(escape_path):
                    move = escape_path[index]
                    path_string += move  
                    print(f"\nMoving: {move} (Path: {path_string})")
                    s.sendall(move.encode())
                    index += 1  
                    time.sleep(0.2)  
                else:
                    print("No more moves in the escape path.")
                    break
            else:
                print("Time's up!")
                break

if __name__ == "__main__":
    main()
