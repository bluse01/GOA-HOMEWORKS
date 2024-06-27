
def main():
    nums = int(input("MAKE A LIST: "))
    main_list = []

    for i in range(1 , nums + 1):
        main_list.append(i)

    print(main_list)
    print("Lagers num in the list: " + str(main_list[-1]))

main()