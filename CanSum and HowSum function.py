# in this file we make 2 functions we give a target_number and a list_of_numbers

# in first one     CanSum()
# goal is to check if we can sum numbers in list_of_numbers that add up to be target_number 
# for example if input be (10 , (4, 2)) =>output=> True becuse 4+4+2=10   but (10, (3,8))=>False 

# in the other one    HowSum()
# we just want to get which numbers add up to make target_number


def CanSum(target_number, list_of_numbers, memo={}):
    if target_number in memo.keys():
        return memo[target_number]
    elif target_number == 0:
        return True
    elif target_number < 0:
        return False
    for number in list_of_numbers:
        reminder = target_number - number
        if CanSum(reminder, list_of_numbers, memo):
            memo[target_number] = True
            return True
    memo[target_number] = False
    return False

print(CanSum(300, (12, 7, 14)))