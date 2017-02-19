from functools import reduce, zip
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



while not pools_empty(pools):

print(sort_servers_into_pools([1,6,6,4,8,0,1,8,7,5,8,8,6,18,20,13,4], 3))
