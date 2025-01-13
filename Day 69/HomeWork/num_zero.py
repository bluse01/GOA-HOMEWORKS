def transform_num(num):
    num_str = str(num)
    return int(str(int(num_str[0]) + 1) + "0" * (len(num_str) - 1))

print(transform_num(7895))