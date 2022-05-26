
def merge_one_into_another(first, second):
    i = len(first)-1
    j = len(first)-1
    k = len(second)-1

    while i >= 0 and j >= 0:
        if first[i] <= second[j]:
            second[k] = second[j]
            j -= 1
            k -= 1
        else:
            second[k] = first[i]
            i -= 1
            k -= 1

    while i >= 0:
        second[k] = first[i]
        i -= 1
        k -= 1

    return second


first = [4, 5, 6]
second = [1, 2, 3, 0, 0, 0]
result = merge_one_into_another(first, second)
print(result)
