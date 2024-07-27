
def main():
    list_input = int(input("INPUT NUMBERS: "))
    main_list = []

    for i in range(1, list_input + 1):
        main_list.append(i)

    print(main_list)
    main_list.reverse()
    print(main_list)

main()