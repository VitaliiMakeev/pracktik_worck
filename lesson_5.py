# # Задание 1
# def odd_nums(number):
#     for num in range(1, number + 1):
#         if num % 2 != 0:
#             yield num



# Задание 2
def odd_nums(number):
    numbers_gen = (num for num in range(1, number + 1) if num % 2 != 0)
    return numbers_gen


odd_to_15 = odd_nums(4)
print(next(odd_to_15))
print(next(odd_to_15))


