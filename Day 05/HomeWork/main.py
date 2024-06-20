print("----------- AND -----------")
num = 7  

# Here, we are using the AND operator to check if num is in certain ranges

print(num >= 1 and num <= 10) # True
# True and True, since num is 7 which is within the range 1 to 10

print(num >= 1 and num <= 4) # False
# True and False, since num is 7 which is not within the range 1 to 4

print(num > 5 and num <= 10) # True
# True and True, since num is 7 which is greater than 5 and also less than or equal to 10

print(num > 5 and num > 10) # False
# True and False, since num is 7 which is greater than 5 but not greater than 10

print("----------- OR -----------")

# Here, we are using the OR operator to check if num satisfies at least one of the conditions

print(num >= 1 or num <= 10) # True
# True or True, since num is 7 which satisfies both conditions but we only need one to be True

print(num >= 1 or num <= 4) # True
# True or False, since num is 7 which satisfies the first condition (greater than or equal to 1)

print(num > 5 or num <= 10) # True
# True or True, since num is 7 which satisfies both conditions but we only need one to be True

print(num > 5 or num > 10) # True
# True or False, since num is 7 which satisfies the first condition (greater than 5)
