from random import shuffle, random
from time import time


def init_arrays(arr_length):
    arr1 = list(range(arr_length))
    arr2 = list(range(arr_length))

    count = 0

    for i in range(arr_length):
        if random() > 0.5:
            arr1[i] = i + 1
            arr2[i] = i + 1
            count += 1
        else:
            arr1[i] = i + 1
            arr2[i] = -1 * (i + 1)

    return arr1, arr2, count


def count_common_entries(arr1, arr2):
    # generate set from arr1
    tags = set(arr1)

    # check common entries
    common = 0
    for val in arr2:
        if val in tags:
            common += 1

    return common


def find_tags(arr_length):
    arr1, arr2, count = init_arrays(arr_length)

    shuffle(arr1)
    shuffle(arr2)

    tic = time()
    check = count_common_entries(arr1, arr2)
    toc = time()

    assert check == count

    # return in `ms`
    return (toc - tic) * 1000


if __name__ == "__main__":
    print(find_tags(2 ** 20))
