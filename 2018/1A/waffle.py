N = int(input())

from itertools import accumulate as acc

for case_id in range(1, N + 1):
    r, c, h, v = map(int, input().split())
    rows = [input() for _ in range(r)]
    columns = [''.join(row[col_index] for row in rows) for col_index in range(c)]
    
    acc_rows_choco_nb = [*acc(row.count('@') for row in rows)]
    
    total_choco_nb = acc_rows_choco_nb[-1]
    
    possible = True
    
    if total_choco_nb%((h + 1)*(v + 1)):
        possible = False
    else:
        h_cut_indexes = []
        nb_choco_per_h_cut = total_choco_nb//(h + 1)
        for cut_h in range(h):
            if nb_choco_per_h_cut*(cut_h + 1) not in acc_rows_choco_nb:
                possible = False
                break
            h_cut_indexes.append(acc_rows_choco_nb.index(nb_choco_per_h_cut*(cut_h + 1)))
        else:
            # rows
            
            # @.@. (-1, 0)
            #
            # .@.@ (0, 2)
            # .@..
            #
            # .@.. (2, 3)
            
            # acc_columns_choco_nb_by_column
            
            # [
            #   (1,0,0)
            #   (1,2,1)
            #   (2,2,1)
            #   (2,3,1)
            # ]
            
            columns_choco_nb_by_double_cut = [
                tuple(
                    columns[col_index][slice_start_exc + 1:slice_stop_inc + 1].count('@')
                    for (slice_start_exc, slice_stop_inc) in zip([-1] + h_cut_indexes, h_cut_indexes + [r - 1])
                )
                for col_index in range(c)
            ]
            
            acc_columns_choco_nb_by_v_slice = [
                [*acc(columns_choco_nb_by_double_cut[col_index][h_cut_nb] for col_index in range(c))]
                for h_cut_nb in range(h + 1)
            ]
            
            acc_columns_choco_nb_by_column = [
                tuple(
                    acc_columns_choco_nb_by_v_slice[h_cut][col_index]
                    for h_cut in range(h + 1)
                )
                for col_index in range(c)
            ]
            
            nb_choco_per_double_cut = total_choco_nb//(h + 1)//(v + 1)
            for cut_v in range(v):
                if (nb_choco_per_double_cut*(cut_v + 1),)*(v + 1) not in acc_columns_choco_nb_by_column:
                    possible = False
                    break
    
    print('Case #{}: {}'.format(case_id, 'POSSIBLE' if possible else 'IMPOSSIBLE'))
