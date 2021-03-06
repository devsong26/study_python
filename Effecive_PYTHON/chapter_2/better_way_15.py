"""
    Better way 15: 클로저가 변수 스코프와 상호 작용하는 방법을 알자

    숫자 리스트를 정렬할 때 특정 그룹의 숫자들이 먼저 오도록 우선순위를 매기려고
    한다고 하자. 이런 패턴은 상용자 인터페이스를 표현하거나, 다른 것보다 중요한
    메시지나 예외 이벤트를 먼저 보여줘야 할 때 유용하다.

    이렇게 만드는 일반적인 방법은 리스트의 sort 메서드에 헬퍼 함수를 key 인수로
    넘기는 것이다. 헬퍼의 반환 값을 리스트에 있는 각 아이템을 정렬하는 값으로
    사용된다. 헬퍼는 주어진 아이템이 중요한 그룹에 있는지 확인하고 그에 따라
    정렬 키를 다르게 할 수 있다.
"""


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

"""
    파이썬은 클로저를 지원한다. 클로저란 자신이 정의된 스코프에 있는 변수를 
    참조하는 함수다. 바로 이 점 덕분에 helper 함수가 sort_priority의 
    group 인수에 접근할 수 있다.
    
    함수는 파이썬에서 일급 객체다. 이 말은 함수를 직접 참조하고, 변수에 할당하고,
    다른 함수의 인수로 전달하고, 표현식과 if 문등에서 비교할 수 있다는 의미다.
    따라서 sort 메서드에서 클로저 함수를 key 인수로 받을 수 있다.
    
    파이썬에는 튜플을 비교하는 특정한 규칙이 있다. 먼저 인덱스 0으로 아이템을 
    비교하고 그 다음으로 인덱스 1, 다음은 인덱스 2와 같이 진행한다. 
    helper 클로저의 반환 값이 정렬 순서를 분리된 두 그룹으로 나뉘게 한 건 이 
    규칙 때문이다.
    
    함수에서 우선순위가 높은 아이템을 발견했는지 여부를 반환해서 사용자 인터페이스 
    코드가 그에 따라 동작하게 하면 좋을 것이다. 이런 동작을 추가하는 코로나 
"""