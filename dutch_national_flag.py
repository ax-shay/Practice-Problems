def dutch_flag_sort(balls):

    low = 0
    high = len(balls)-1
    i = 0
    pivot = 'G'

    while i <= high:
        if ord(balls[i]) > ord(pivot):
            balls[low], balls[i] = balls[i], balls[low]
            low += 1
            i += 1
        elif ord(balls[i]) < ord(pivot):
            balls[high], balls[i] = balls[i], balls[high]
            high -= 1
            i -= 1
        else:
            i += 1

    return balls


balls = ["G", "B", "G", "G", "R", "B", "R", "G"]
result = dutch_flag_sort(balls)
print(result)



