def remove_evens(numbers):
    result = []

    for num in numbers:
        if num % 2 != 0:
            result.append(num)

    return result


print(remove_evens([1, 2, 2, 3, 4, 5, 6, 7]))
