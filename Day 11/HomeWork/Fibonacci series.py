
def main():
    num_term = int(input("How many terms? "))

    stp1, stp2 = 0, 1
    prev_num = 0   

    while num_term > prev_num:
        result = stp1 + stp2
        print(result)

        stp1 = stp2
        stp2 = result

        prev_num += 1


main()