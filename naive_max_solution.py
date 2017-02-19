from functools import reduce
import random
from main import parse_file

def sort_servers_into_pools(server_list, num_pools):
    large_servers_first = list(reversed(sorted(server_list)))
    pools = []
    for i in range(num_pools):
        pools.append([])
    for i in range(len(large_servers_first)):
        pools[i % num_pools].append(large_servers_first[i])
    return pools


def allocate_servers_to_rows(pools, rows):
    num_rows = len(rows)
    current_row = 0
    for i in len(pools):
        for j in len(pools[i]):
            gaps_by_size = list(reversed(sorted(zip(rows[current_row], range(len(rows[current_row]))))))
            for gap in gaps_by_size:
                smallest_server = None
                for server in pools[i]:
                    if server[0] <= gap_size:
                        smallest_server = server
                        pools[i].remove(server)
                if smallest_server:
                    break


def sum_capacity(pool):
    return sum([s['capacity'] for s in pool])


def update_pools_by_count(pools):
    pools = sorted(pools, key=lambda p: len(p), reverse=True)
    pool1 = pools[0]
    pool2 = pools[-1]
    min_server = min(pool1, key=lambda s: s['capacity'])
    pool2 += [min_server] 
    pool1.remove(min_server)
    return pools


def update_pools_by_capacity(pools):
    pools = sorted(pools, key=lambda p: sum_capacity(p), reverse=True)
    pool1 = pools[0]
    pool2 = pools[-1]
    min_server = min(pool1, key=lambda s: s['capacity'])
    pool2 += [min_server]
    pool1.remove(min_server)
    return pools


def sort_servers_into_pools_greedy(server_list, num_pools):
    random.shuffle(server_list)
    pools = [[] for i in range(num_pools)]
    for i in range(len(server_list)):
        pools[i % num_pools].append(server_list[i])
    i = 0
    while i < 10:
        pools = update_pools_by_capacity(pools)
        pools = update_pools_by_count(pools)
        i += 1
    return pools

data_struct = parse_file('./testfile')
sort_servers_into_pools_2(data_struct['servers'], data_struct['pools'])