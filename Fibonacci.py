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