# for this problem simple answer is following function which is slow and take a lots of time for grids bigger than (15,15)



# def GridTraveler(m, n):
#     if m == n == 1:
#         return 1
#     elif m == 0 or n == 0:
#         return 0
#     else:
#         return GridTraveler(m-1, n) + GridTraveler(m, n-1)


# Better solution is like following



def GridTraveler(m, n, memo={}):
    if m == n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    elif (m, n) in memo.keys():
        return memo[(m, n)]
    elif (n, m) in memo.keys():
        return memo[(n, m)]
    else:
        memo[m, n] = GridTraveler(m-1, n) + GridTraveler(m, n-1)
    return GridTraveler(m-1, n) + GridTraveler(m, n-1)

print(GridTraveler(1, 1))
print(GridTraveler(1, 2))
print(GridTraveler(2, 2))
print(GridTraveler(3, 3))
print(GridTraveler(4, 4))
print(GridTraveler(400, 400))