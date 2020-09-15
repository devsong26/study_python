"""
    Better way 7: map과 filter 대신 리스트 컴프리헨션을 사용하자

    한 리스트에서 다른 리스트를 만들어내는 간결한 문법이 있다.
    이 문법을 사용한 표현식을 리스트 컴프리헨션(comprehension)이라고 한다.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)
"""
    인수가 하나뿐인 함수를 적용하는 상황이 아니면, 간단한 연산에는 리스트 컴프리헨션이
    내장 함수 map보다 명확하다. map을 쓰려면 계산에 필요한 lambda 함수를 생성해야 
    해서 깔끔해 보이지 않는다.
"""
squares = map(lambda x: x ** 2, a)
"""
    map과 달리 리스트 컴프리헨션을 사용하면 입력 리스트에 있는 아이템을 간편하게
    걸러내서 그에 대응하는 출력을 결과에서 삭제할 수 있다.
"""
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)
"""
    내장 함수 filter를 map과 연계해서 사용해도 같은 결과를 얻을 수 있지만 
    훨씬 읽기 어렵다.
"""
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)
"""
    딕셔너리와 세트에도 리스트 컴프리헨션에 해당하는 문법이 있다.
    컴프리헨션 문법을 쓰면 알고리즘을 작성할 때 파생되는 자료 구조를 쉽게 생성할 수 
    있다.
"""
chile_ranks = {'ghost':1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)