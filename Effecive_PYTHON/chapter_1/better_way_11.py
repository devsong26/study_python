"""
    Better way 11: 이터레이터를 병렬로 처리하려면 zip을 사용하자.

    리스트 컴프리헨션을 사용하면 소스 리스트에 표현식을 적용하여 파생 리스트를 쉽게
    얻을 수 있다.
"""
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)

"""
    파생 리스트의 아이템과 소스 리스트의 아이템은 서로의 인덱스로 연관되어 있다.
    따라서 두 리스트를 병렬로 순회하려면 소스 리스트인 names의 길이만큼 순회하면 
    된다.
"""
longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)
"""
    위의 코드를 enumerate를 사용하면 아래와 같다.
"""
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

"""
    파이썬은 위의 코드를 좀 더 명료하게 하는 내장 함수 zip을 제공한다.
    파이썬 3에서 zip은 지연 제너레이터로 이터레이터 두 개 이상을 감싼다.
    zip 제너레이터는 각 이터레이터로부터 다음 값을 담은 튜플을 얻어온다.
    zip 제너레이터를 사용한 코드는 다중 리스트에서 인덱스로 접근하는 코드보다
    훨씬 명료하다.
"""
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
"""
    zip은 두 가지의 문제점이 있다.
    1. 파이썬 2와 관련되므로 생략
    2. 입력 이터레이터들의 길이가 다르면 zip이 이상하게 동작한다는 점이다.
    아래 코드에서 Rosalind가 출력되지 않는다.
    zip을 사용할 때는 동일한 길이의 리스트(파생, 소스)를 사용하자.
    zip으로 실행할 리스트의 길이가 같다고 확신할 수 없다면 대신 내장 모듈 
    itertools의 zip_longest를 사용하는 방안을 고려해보자.
"""
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)