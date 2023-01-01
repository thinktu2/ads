# import os
# import random
from sim_file import sim_file
from server import sim_server
from cache import sim_cache


if __name__ == "__main__":
    number = input()
    number = number.split()
    op_number = int(number[0])
    client_number = int(number[1])

    server = sim_server()
    client_list = []
    for i in range(client_number):
        temp_cache = sim_cache(server)
        client_list.append(temp_cache)

    for i in range(op_number):
        op = input()
        op = op.split()
        if op[0] == 'read' :
            print(client_list[int(op[1])].read(op[2]))
        else:
            client_list[int(op[1])].write(op[2],op[3])
    
