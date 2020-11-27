#计算器
print('请输入您要进行的运算')
s = input()
if s=='加法':
    print('请输入第一个数')
    y = int(input())
    print('请输入第二个数')
    w = int(input())
    try:
        b = y+w
        print(b)

    except:
        print('出错了')

if s=='减法':
    print('请输入第一个数')
    y = int(input())
    print('请输入第二个数')
    w = int(input())
    try:
        b = y-w
        print(b)

    except:
        print('出错了')

if s=='乘法':
    print('请输入第一个数')
    y = int(input())
    print('请输入第二个数')
    w = int(input())
    try:
        b = y*w
        print(b)

    except:
        print('出错了')

if s=='除法':
    print('请输入第一个数')
    y = int(input())
    print('请输入第二个数')
    w = int(input()) 
    if w==0:
        print('除数等于0')
    try:
        b = y/w
        print(b)

    except:
        print('出错了')
