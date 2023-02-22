def find_dividers_count(number):
    i = 1
    count = 0

    while i ** 2 <= number:
        if number % i == 0 and i * i != number:
            count += 2
        elif number % i == 0 and i * i == number:
            count += 1
        i += 1

    return count


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1

        while j >= 0 and find_dividers_count(temp) < find_dividers_count(array[j]):
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = temp


arr = [1, 5, 77, 3, 7, 99, 1, 4, 6, 3]
arr.sort(key=find_dividers_count)
print(arr)

arr = [1, 5, 77, 3, 7, 99, 1, 4, 6, 3]
insertion_sort(arr)
print(arr)
