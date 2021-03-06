"""
    Better way 9: 컴프리헨션이 클 때는 제너레이터 표현식을 고려하자

    리스트 컴프리헨션의 문제점은 입력 시퀀스에 있는 각 값별로 아이템을 하나씩
    담은 새 리스트를 통째로 생성한다는 점이다. 입력이 적을 때는 괜찮지만 클 때는
    메모리를 많이 소모해서 프로그램을 망가뜨리는 원인이 되기도 한다.
"""
try:
    value = [len(x) for x in open('/tmp/my_file.txt')]
    print(value)
except FileNotFoundError:
    print("그런 파일 없음")

"""
    이 문제를 해결하려고 리스트 컴프리헨션과 제너레이터를 일반화한 제너레이터 표현식을 
    제공한다. 제너레이터 표현식은 실행될 때 출력 시퀀스를 
    모두 구체화(여기서는 메모리에 로딩)하지 않는다. 대신에 표현식에서 한 번에 
    한 아이템을 내주는 이터레이터로 평가된다.
    제너레이터 표현식은 () 문자 사이에 리스트 컴프리헨션과 비슷한 문법을 사용하여 
    생성한다. 
    위의 로직을 아래 제너레이터 표현식으로 작성한 예다. 하지만 제너레이터 표현식은
    즉시 이터레이터로 평가되므로 더는 진행되지 않는다. 
"""
try:
    it = (len(x) for x in open('/tmp/my_file.txt'))
    print(it)
except FileNotFoundError:
    print("파일 없음")
"""
    제너레이터 표현식에서 다음 출력을 생성하려면 내장 함수 next로 반환받은 
    이터레이터를 한 번에 전진시키면 된다. 코드에서는 메모리 사용량을 걱정하지 
    않고 제너레이터 표현식을 사용하면 된다.
    제너레이터 표현식의 또 다른 강력한 결과는 다른 제너레이터 표현식과 함께 
    사용할 수 있다는 점이다. 
"""

values = [1, 2, 3, 4, 5, 6, 7]
it = (x for x in values)
roots = ((x, x**0.5) for x in it)
"""
    이 이터레이터를 전진시킬 때마다 루프의 도미노 효과로 내부 이터레이터도 
    전진시키고 조건 표현식을 계산해서 입력과 출력을 처리한다.
"""
print(next(roots))
"""
    제너레이터를 연결하면 파이썬에서 매우 빠르게 실행할 수 있다.
    큰 입력 스트림에 동작하는 기능을 결합하는 방법을 찾을 때는 제너레이터 표현식이 
    최선의 도구다. 단, 제너레이터 표현식이 반환한 이터레이터에는 상태가 있으므로
    이터레이터를 한 번 넘게 사용하지 않도록 주의해야 한다.
"""