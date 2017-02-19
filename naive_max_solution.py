from functools import reduce
def sort_servers_into_pools(server_list, num_pools):
    large_servers_first = list(reversed(sorted(server_list)))
    pools = []
    for i in range(num_pools):
        pools.append([])
    for i in range(len(large_servers_first)):
        pools[i % num_pools].append(large_servers_first[i])
    return pools

# def pools_empty(pools):
#     return reduce(lambda cum, x: cum and len(x)==0, pools, true)
#
# def allocate_servers_to_rows(pools, rows):
#
#     last_pool_used = 0
# while not pools_empty(pools):
#
#
# print(sort_servers_into_pools([1,6,6,4,8,0,1,8,7,5,8,8,6,18,20,13,4], 3))
