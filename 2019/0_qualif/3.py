from math import gcd, sqrt

N = int(input())

for case_id in range(1, N + 1):
    max_prime, nb_of_pairs = map(int, input().split())
    prime_pairs = [*map(int, input().split())]

    primes = []

    for prime_pair_index in range(len(prime_pairs) - 1):
        left_pair, right_pair = prime_pairs[prime_pair_index:][:2]

        common_prime_number = gcd(left_pair, right_pair) if left_pair != right_pair else int(sqrt(left_pair))
        primes.append(common_prime_number)

        if prime_pair_index == 0:
            primes.insert(0, left_pair // common_prime_number)
        if prime_pair_index == len(prime_pairs) - 2:
            primes.append(right_pair // common_prime_number)

    translation_dict = {
        prime: chr(ord('A') + prime_index)
        for prime_index, prime
        in enumerate(sorted(set(primes)))
    }
    decoded_string = ''.join(map(translation_dict.get, primes))

    print('Case #{}: {}'.format(case_id, decoded_string))
