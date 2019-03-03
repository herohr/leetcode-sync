a = [1,3,4,5,2,1,21,2,1,4,15,1,23,123,12,24,11,25,15,12,51,256,1,6,16,2,61,261,2614]


def func(a, sum):
    if a:
        sum += a[0]
        return func(a[1:], sum)
    return sum


print(func(a,0))
