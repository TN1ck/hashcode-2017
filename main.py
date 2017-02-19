import naive_max_solution

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

def get_solution(parsed_data_structure):
    max_servers = []
    for server in parsed_data_structure['servers']:
        max_servers.append([server['size'], server['capacity']])
    pool_allocation = naive_max_solution.sort_servers_into_pools(max_servers, parsed_data_structure['pools'])
    row_allocation = naive_max_solution.allocate_servers_to_rows(pool_allocation, parsed_data_structure['rows'])
    return row_allocation

def __main__():
    print('HASHCODE 2015\n')
    parsed_data_structure = parse_file('./testfile')
    print('parsed file', parsed_data_structure)
    final_allocation = get_solution(parsed_data_structure)
    print("final_allocation", final_allocation)




__main__()
