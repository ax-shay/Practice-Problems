from timeit import default_timer as timer


def segregate_evens_and_odds(numbers):
    odd_index = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            odd_index = min(i, odd_index)
        else:
            numbers[i], numbers[odd_index] = numbers[odd_index], numbers[i]
            odd_index += 1

    return numbers


def also_segregate_evens_and_odds(numbers):
    swap_index = -1
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            swap_index += 1
            numbers[i], numbers[swap_index] = numbers[swap_index], numbers[i]

    return numbers


numbers = [5, 6, 8, 1, 10, -10, -1]

start = timer()
result = segregate_evens_and_odds(numbers)
end = timer()
print('Result is: {0} and it ran in {1} sec'.format(result, end-start))

start_2 = timer()
result_2 = also_segregate_evens_and_odds(numbers)
end_2 = timer()
print('Result is: {0} and it ran in {1} sec'.format(result_2, end_2-start_2))
