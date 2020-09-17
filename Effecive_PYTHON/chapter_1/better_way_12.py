"""
    Better way 12: for와 while 루프 뒤에는 else 블록을 쓰지 말자

    파이썬은 루프에서 반복되는 내부 블록 바로 다음에 else 블록을 둘 수 있다.
"""
for i in range(3):
    print("Loop %d" % i)
else:
    print("Else block!")
"""
    루프 종료 후에 else가 실행된다.
    break를 사용해야 else 블록을 건너뛸 수 있다.
"""
for i in range(3):
    print('Loop %d' % i)
    if i == 1:
        break
else:
    print("Else block!")
"""
    루프의 조건문이 거짓일 때 else가 바로 실행된다.
    이렇게 동작하는 이유는 루프 다음에 오는 else 블록은 루프로 뭔가를 검색할 때 
    유용하기 때문이다. 아래는 두 숫자가 
    서로소(공약수가 1밖에 없는 둘 이상의 수)인지를 판별한다.
"""
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print("Not coprime")
        break
else:
    print('Coprime')
"""
    위의 방식은 안 좋은 코드이며 아래와 같이 개선해야 한다.
"""


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


"""
    다른 방식으로는 아래와 같다.
"""


def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime


"""
    루프 뒤에 else 블록을 붙이면 코드 해석이 난해하므로 절대 사용하면 안된다.
"""