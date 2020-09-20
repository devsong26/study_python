"""
    Better way 14: None을 반환하기보다는 예외를 일으키자
"""


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None


"""
    위의 코드는 반환 값을 다음과 같이 해석한다.
"""
result = divide(0, 1)
if result is None:
    print("Invalid inputs")
"""
    이 때, 분자가 0이 되면 반환값도 0이 되어버린다.
    그러면 if 문과 같은 조건에서 결과를 평가할 때 문제가 될 수 있다.
    오류인지 알아내려고 None 대신 실수로 False에 해당하는 값을 검사할 수도 있다.
"""
x, y = 0, 5
result = divide(x, y)
if not result:
    print("Invalid inputs")  # 잘못됨!

"""
    이 예는 None에 특별한 의미가 있을 때 파이썬 코드에서 흔히 하는 실수다.
    바로 이 점이 함수에서 None을 반환하면 오류가 일어나기 쉬운 이유다.
    이런 오류가 일어나는 상황을 줄이는 방법은 두 가지다.
    
    첫 번째 방법은 반환 값을 두 개로 나눠서 튜플에 담는 것이다.
    튜플의 첫 번째 부분은 작업이 성공했는지 실패했는지를 알려준다.
    두 번째 부분은 계산된 실제 결과다.
"""


def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


"""
    이 함수를 호출하는 쪽에서는 튜플을 풀어야 한다. 따라서 나눗셈의 결과만 
    얻을 게 아니라 튜플에 들어 있는 상태 부분까지 고려애햐 한다.    
"""
success, result = divide(x, y)
if not success:
    print("Invalid inputs")


"""
    문제는 호출자가 튜플의 첫 번째 부분을 쉽게 무시할 수 있다는 점이다.
    얼핏 보기에는 이렇게 작성한 코드가 잘못된 것 같지 않다. 하지만 결과는 
    그냥 None을 반환하는 것만큼이나 나쁘다.
"""

_, result = divide(x, y)
if not result:
    print("Invalid inputs")
"""
    이런 오류를 줄이기에 더 좋은 두 번째 방법은 절대로 None을 반환하지 않는 것이다.
    대신에 호출하는 쪽에 예외를 일으켜서 호출하는 쪽에서 그 예외를 처리하게 하는 
    것이다. 여기서는 호출하는 쪽에 입력값이 잘못됐음을 알리려고 
    ZeroDivisionError를 ValueError로 변경했다.
"""


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


"""
    이제 호출하는 쪽에서는 잘못된 입력에 대한 예외를 처리해야 한다.
    호출하는 쪽에서 더는 함수의 반환 값을 조건식으로 검사할 필요가 없다.
    함수가 예외를 일으키지 않았다면 반환 값은 문제가 없다. 예외를 처리하는 코드도 
    깔끔해진다.
"""
x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print("Result is %.1f" % result)
