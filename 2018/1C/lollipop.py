from math import sqrt

N = int(input())

for case_id in range(1, N + 1):
    nb_lollipop = int(input())
    available_flavours = set(range(nb_lollipop))
    flavour_occurrences = {flavour: 0 for flavour in range(nb_lollipop)}
    
    for customer_index in range(nb_lollipop):
        nb_flavour_liked, *flavours_liked = map(int, input().split())
        flavours_liked = set(flavours_liked)
        
        for liked_flavour in flavours_liked:
            flavour_occurrences[liked_flavour] += 1
        
        available_flavours_liked = flavours_liked.intersection(available_flavours)
        
        if len(available_flavours_liked) == 0:
            print(-1)
        else:
            sold_flavour = min(available_flavours_liked, key=lambda flavour: flavour_occurrences[flavour])
            print(sold_flavour)
            available_flavours.remove(sold_flavour)
