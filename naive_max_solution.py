#!/usr/bin/env python3
from functools import reduce
def sort_servers_into_pools(server_list, num_pools):
    print("number of servers", len(server_list))
    large_servers_first = list(reversed(sorted(server_list)))
    pools = []
    for i in range(num_pools):
        pools.append([])
    for i in range(len(large_servers_first)):
        pools[i % num_pools].append(large_servers_first[i])
    for i in range(num_pools):
        for j in range(len(pools[i])):
            pools[i][j].append(i)
            pools[i][j] = tuple(pools[i][j])
    return pools



def allocate_servers_to_rows(pools, rows):
    num_rows = len(rows)
    allocation = []
    for i in range(len(rows)):
        allocation.append([])
        for j in range(len(rows[i])):
            allocation[i].append([])

    # print("empty allocation", allocation)

    current_row = 0
    for i in range(len(pools)):
        # print("Using pool", i)
        for j in range(len(pools[i])):
            gaps_by_size = list(reversed(sorted(zip(rows[current_row], range(len(rows[current_row]))))))
            # print("row", current_row, "Using item", pools[i][j], "gaps_by_size", gaps_by_size)
            for gap in gaps_by_size:
                # print("Using gap", gap)
                smallest_server = None
                # print("pools[i]", pools[i])
                for server in pools[i]:
                    if server[0] <= gap[0]:
                        smallest_server = server
                        # pools[i].remove(server)
                        break

                if smallest_server:
                    # print("Found smallest server for gap", smallest_server)
                    rows[current_row][gap[1]] = gap[0] - smallest_server[0]
                    allocation[current_row][gap[1]].append(smallest_server)
                    break
            current_row = (current_row+1)%num_rows
            # print("allocation", allocation)
    return allocation



pools = sort_servers_into_pools([[1,1],[6,1],[6,1],[4,1],[8,1],[1,1],[8,1],[7,1],[5,1],[8,1],[8,1],[6,1],[18,1],[20,1],[13,1],[4,1]], 3)
print("pools", pools)
rows = [
        [20],
        [10,10],
        [8,6,3],
        [3,10],
        [18]
    ]

allocation = allocate_servers_to_rows(pools, rows)
num_all_servers = 0
for i in range(len(allocation)):
    for j in range(len(allocation[i])):
        num_all_servers += len(allocation[i][j])
print("allocated items", num_all_servers, "allocation", allocation)
