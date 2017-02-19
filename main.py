def parse_file(file_path):
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
        header = lines[0]
        [rows, slots, unavailable_slots, pools, servers] = [int(x) for x in header.split(' ')]
        print('rows {}, slots {}, unavailable_slots {}, pools {}, servers {}'.format(
            rows, slots, unavailable_slots, pools, servers
        ))
        unavailable_slots_lines = lines[1:(1 + unavailable_slots)]
        parsed_unavailable_slots = []
        for line in unavailable_slots_lines:
            (row, slot) = [int(x) for x in line.split(' ')]
            parsed_unavailable_slots.append({'row': row, 'slot': slot})
        print('parsed unavailable slots', parsed_unavailable_slots)

        parsed_rows = []
        for _ in range(rows):
            # [1, 2, 3, 4, 5]
            parsed_rows.append([x for x in range(slots)])

        for unavailable_slot in parsed_unavailable_slots:
            # [1, False, 3, 4, 5]
            parsed_rows[unavailable_slot['row']][unavailable_slot['slot']] = False

        grouped_rows = []
        for row in parsed_rows:
            # [4, 1]
            new_row = []
            current = 0
            for slot in row:
                if slot is False and current > 0:
                    new_row.append(current)
                    current = 0
                elif slot is not False:
                    current += 1
            if current > 0:
                new_row.append(current)
            grouped_rows.append(new_row)
        print('grouped rows', grouped_rows)

        servers_to_be_allocated_lines = lines[(1 + unavailable_slots):]
        parsed_servers_to_be_allocated = []
        server_index = 0
        for line in servers_to_be_allocated_lines:
            server_index += 1
            (size, capacity) = ([int(x) for x in line.split(' ')])
            parsed_servers_to_be_allocated.append({
                'size': size,
                'capacity': capacity,
                'index': server_index
            })
        print('parsed servers', parsed_servers_to_be_allocated)
        return {
            'rows': grouped_rows,
            'slots': slots,
            'unavailable_slots': parsed_unavailable_slots,
            'pools': pools,
            'servers': parsed_servers_to_be_allocated
        }
    
def server_does_not_exist(server, list):
    result = [s for s in list if s['index'] == server['index']]
    return len(result) == 0

def score (row_allocation, pools):
    row_shutdown_result = []
    for row in row_allocation:
        pools_capacity = []
        for pool in pools:
            pool_with_outages = [server for server in pool if server_does_not_exist(server, row)]
            pool_capacity = sum([server['capacity'] for server in pool_with_outages])
            pools_capacity.append(pool_capacity)
        row_shutdown_result.append(pool_capacity)
    return row_shutdown_result

print('score', score(
    [
        [
            {'size': 1, 'capacity': 5, 'index': 2},
            {'size': 2, 'capacity': 2, 'index': 4}
        ],
        [
            {'size': 2, 'capacity': 4, 'index': 1},
            {'size': 2, 'capacity': 4, 'index': 3},
        ]
    ],
    [
        [
            {'size': 1, 'capacity': 5, 'index': 2},
            {'size': 2, 'capacity': 4, 'index': 3}
        ],
        [
            {'size': 2, 'capacity': 4, 'index': 1},
            {'size': 2, 'capacity': 2, 'index': 4}
        ]
    ]
))

def __main__():
    print('HASHCODE 2015\n')
    parsed_data_structure = parse_file('./testfile')
    print('parsed file', parsed_data_structure)


__main__()
