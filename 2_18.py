def count_friends(start, temp, r, c, y, x, value):
    if y < 0 or x < 0 or x == c or y == r or temp[y][x] > 0 or start[y][x] != value:
        return 0

    temp[y][x] = 1
    result = 1

    result += count_friends(start, temp, r, c, y - 1, x, value)
    result += count_friends(start, temp, r, c, y, x - 1, value)
    result += count_friends(start, temp, r, c, y + 1, x, value)
    result += count_friends(start, temp, r, c, y, x + 1, value)
    return result


def fill_arr(start, temp, final, r, c, y, x, value, fill_value):
    if y < 0 or x < 0 or x == c or y == r or temp[y][x] == 2 or start[y][x] != value:
        return

    temp[y][x] = 2
    final[y][x] = fill_value

    fill_arr(start, temp, final, r, c, y - 1, x, value, fill_value)
    fill_arr(start, temp, final, r, c, y, x - 1, value, fill_value)
    fill_arr(start, temp, final, r, c, y + 1, x, value, fill_value)
    fill_arr(start, temp, final, r, c, y, x + 1, value, fill_value)


start_arr = [[1, 2, 3, 9, 9], [2, 2, 2, 9, 2], [1, 1, 2, 2, 4]]
arr_count = len(start_arr)
arr_len = len(start_arr[0])
temp_arr = [[0] * arr_len for j in range(arr_count)]
final_arr = [[0] * arr_len for i in range(arr_count)]

for y in range(arr_count):
    for x in range(arr_len):
        if temp_arr[y][x] == 0:
            count = count_friends(start_arr, temp_arr, arr_count, arr_len, y, x, start_arr[y][x])
            fill_arr(start_arr, temp_arr, final_arr, arr_count, arr_len, y, x, start_arr[y][x], count - 1)

# вывод
center = len(start_arr) / 2 - 1 if len(start_arr) % 2 == 0 else (len(start_arr) - 1) / 2
for i in range(len(start_arr)):
    print(start_arr[i], " -> " if i == center else "    ", final_arr[i])
