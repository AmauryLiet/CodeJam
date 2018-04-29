
N = int(input())

for case_id in range(1, N + 1):
    nb_people, nb_language = map(int, input().split())
    proportions = [*map(int, input().split())]
    
    print('Case #{}: {} {}'.format(
        case_id,
        sum(map(lambda p: round(p*100/nb_people), proportions)),
        round((nb_people - sum(proportions))*100/nb_people)
    ))
