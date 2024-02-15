# get number and return list of divisor from 2 to number --> number= 12, divisor_list = [2,3,4,6,12]
def divisors_of_numbers(num: int):
    divisor_list = []
    for divisor in range(2, num + 1):
        if num % divisor == 0:
            divisor_list.append(divisor)
    return divisor_list


# get divisors_list and return dictionary of number and number of prime_number --> divisor_list = [2,3,4,6,12]
# output: {'number':12, 'number_of_primes':2}
def count_primes_in_list(divisors_list: list):
    dict_number_and_number_of_primes = {}
    primes_list = []
    number = int(divisors_list[-1])
    # number = int(number)

    for num in divisors_list:
        for i in range(2, num // 2 + 1):
            if num % i == 0:  # number is not prime
                break
        else:
            primes_list.append(int(num))
            dict_number_and_number_of_primes['number'] = number
            dict_number_and_number_of_primes['number_of_primes'] = len(primes_list)

    return dict_number_and_number_of_primes


def sort_dict(data: list):
    sort_dict = sorted(all_number_list, key=lambda d: (d['number_of_primes'], d['number']), reverse=True)
    return sort_dict


all_number_list = []
for i in range(10):
    n = int(input())
    divisor_list = divisors_of_numbers(n)
    divisor_dict = count_primes_in_list(divisor_list)
    all_number_list.append(divisor_dict)


sort_all_number = sort_dict(all_number_list)
high_number_of_primes = sort_all_number[0]
for key in high_number_of_primes:
    print(high_number_of_primes[key], end=' ')
