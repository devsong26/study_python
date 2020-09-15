"""
    Better way 4: 복잡한 표현식 대신 헬퍼 함수를 작성하자
"""

from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))
"""
    쿼리 문자열 파라미터에 따라 값이 여러 개 있을 수도 있고 값이 한 개만 있을 수도 있으며,
    파라미터는 존재하지만 값이 비어 있을 수 있고, 파라미터가 아예 빠진 경우도 있다.
    결과 딕셔너리에 get 메서드를 사용하면 각 상황에 따라 다른 값을 반환
"""
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

"""
    빈 문자열, 빈 리스트, 0이 모두 암시적으로 False
"""

# 쿼리 문자열: 'red=5&blue=0&green='
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)
"""
    위의 초기화 표현식은 읽기 어려움
    if/else 조건식(삼항 표현식)을 이용하면 코드를 짧게 유지하면서도 더 명활하게
    표현할 수 있음    
"""
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0 # 삼항 연산자
"""
    이 로직을 풀어쓰면 복잡해 보이며 반복해서 사용해야 할 경우 헬퍼 함수를 만든다.
"""


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


"""
    위의 헬퍼 함수를 쓰면 or를 사용한 복잡한 표현식이나 if/else 조건식을 사용한
    두 줄짜리 버전을 쓸 때보다 호출 코드가 훨씬 더 명확해진다.
"""
green = get_first_int(my_values, 'green')
"""
    표현식이 복잡해지기 시작하면 최대한 빨리 해당 표현식을 작은 조각으로 분할하고
    로직을 헬퍼 함수로 옮기는 방안을 고려하자. 무조건 짧은 코드를 만들기보다는 
    가독성을 선택하는 편이 낫다. 이렇게 이해하기 어려운 복잡한 표현식에는 파이썬의 
    함축적인 문법을 사용하면 안 된다.
"""