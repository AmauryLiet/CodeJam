from math import sqrt

N = int(input())

for case_id in range(1, N + 1):
    A = float(input())
    cos_theta = (A + sqrt(6 - 2*A**2))/3
    sin_theta = sqrt(1 - cos_theta**2)
    
    print('Case #{}:'.format(case_id))
    print('{} {} {}'.format((1 + cos_theta)/4, (1 - cos_theta)/4, -sqrt(2)/4*sin_theta))
    print('{} {} {}'.format((1 - cos_theta)/4, (1 + cos_theta)/4, sqrt(2)/4*sin_theta))
    print('{} {} {}'.format(sqrt(2)/4*sin_theta, -sqrt(2)/4*sin_theta, cos_theta/2))
