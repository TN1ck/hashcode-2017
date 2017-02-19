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
            (x, y) = [int(x) for x in line.split(' ')]
            parsed_unavailable_slots.append({'x': x, 'y': y})
        print('parsed unavailable slots', parsed_unavailable_slots)

        servers_to_be_allocated_lines = lines[(1 + unavailable_slots):]
        parsed_servers_to_be_allocated = []
        for line in servers_to_be_allocated_lines:
            (size, capacity) = ([int(x) for x in line.split(' ')])
            parsed_servers_to_be_allocated.append({'size': size, 'capacity': capacity})
        print('parsed servers', parsed_servers_to_be_allocated)
        return {
            'rows': rows,
            'slots': slots,
            'unavailable_slots': parsed_unavailable_slots,
            'pools': pools,
            'servers': parsed_servers_to_be_allocated
        }


def __main__():
    print('HASHCODE 2015\n')
    parsed_data_structure = parse_file('./testfile')
    print('parsed file', parsed_data_structure)


__main__()
