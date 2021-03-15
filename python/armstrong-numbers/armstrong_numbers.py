def is_armstrong_number(number):
    num_list = str(number)
    armstrong = 0
    for digit in num_list:
        armstrong += pow(int(digit), len(num_list))
    return armstrong == number
