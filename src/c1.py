def add(a,b):
    return a+b

def jianfa(a,b):
    return a-b

f = [1,2]
print(f)

# print("c1's name:-->   ",__name__)
if __name__ == '__main__':
    b = 0

    if b>1:
        c = add(1,2)
        print(c)
    else:
        c = add(10,20)
        print(c)

    print("c1 end")