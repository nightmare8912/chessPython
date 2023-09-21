def myfn(i):
    if (i == 2):
        i = 10
        print(i)
    else:
        myfn(i + 1)
        print(i)

myfn(0)