from typing import Union, List

N = int(input())


def get_connection_index(index1: int, index2: int, connections: List[List[int]]) -> Union[int, None]:
    try:
        return connections.index(sorted([index1, index2]))
    except:
        return None


def get_any_connection_index(index1: int, indexes: List[int], connections: List[List[int]]) -> int:
    for possible_index in indexes:
        connection_index = get_connection_index(index1, possible_index, connections)
        if connection_index is not None:
            return connection_index
    # return None


DEFAULT_LATENCY = 10 ** 6

for case_id in range(1, N + 1):
    nb_computers, nb_connections = map(int, input().split())
    update_infos = [0, *map(int, input().split())]
    connections = [[*map(lambda nb_str: int(nb_str) - 1, input().split())] for _ in range(nb_connections)]

    if any(map(lambda nb: nb > 0, update_infos)):
        print('Case #{}: NOT HANDLED'.format(case_id))

    delay_by_connection = [DEFAULT_LATENCY
                           for connection_index in range(nb_connections)]

    seen_computers_index = [0]
    for rank in range(1, nb_computers):
        computers_for_rank = []
        for computer_index in range(nb_computers):
            if update_infos[computer_index] != -rank:
                continue
            computers_for_rank.append(computer_index)

            used_connection_index = get_any_connection_index(computer_index, seen_computers_index, connections)
            used_connection = connections[ used_connection_index]
            connected_computer_index = used_connection[1 - used_connection.index(computer_index)]

            delay_by_connection[used_connection_index] = -update_infos[computer_index] - (-update_infos[connected_computer_index])

        seen_computers_index.extend(computers_for_rank)

    print('Case #{}: {}'.format(case_id, ' '.join(map(str, delay_by_connection))))
