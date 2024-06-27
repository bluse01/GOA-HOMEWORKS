
def main():
    nums = input("INPUT NUMBER: ")

    result = 0
    for i in range(0, len(nums)):
        result += int(nums[i])

    print(result)

main()
