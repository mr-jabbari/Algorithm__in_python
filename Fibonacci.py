# most people try this algorithm like following

# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# actully this is not wrong but if you want numbers more than 40 it will take a lot of time.
# but in following function we save evey fib algorithm that calculated to save time.
# big O of first function is O(n**2) and following one is O(n)



def fib(n, memo = {}):
    if n <= 2:
        return 1
    elif n in memo.keys():
        return memo[n]
    else:
        memo[n] = fib(n - 1) + fib(n - 2)
    return fib(n - 1) + fib(n - 2)

print(fib(2))
print(fib(7))
print(fib(8))
print(fib(6))
print(fib(1005))


# whit this function I could calculate to fib(1005) which is 211 long.
# I don't know it's related to python or my divice.
# I will write if I find why
