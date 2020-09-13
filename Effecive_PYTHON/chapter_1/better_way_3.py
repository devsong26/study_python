"""
    Better way 3: bytes, str, unicode의 차이점을 알자

    파이썬3의 문자 시퀀스를 나타내는 타입: bytes, str
    bytes 인스턴스는 raw 8비트 값을 저장한다.
    str 인스턴스는 유니코드 문자를 저장한다.

    파이썬2의 문자 시퀀스를 나타내는 타입: str, unicode
    str 인스턴스는 raw 8비트 값을 저장한다.
    unicode 인스턴스는 유니코드 문자를 저장

    파이썬3의 str 인스턴스와 파이썬 2의 unicode 인스턴스는 연관된
    바이너리 인코딩 없음
            (encode)                (decode)
    유니코드 --------> 바이너리 -------->  유니코드

    문자 타입이 분리되어 있는 탓에 파이썬 코드에서 일반적으로 다음 두 가지 상황에
    부딪힌다.
    - UTF-8(혹은 다른 인코딩)으로 인코드된 문자인 rqw 8비트 값을 처리하려는 상황
    - 인코딩이 없는 유니코드 문자를 처리하려는 상황
    이 두 경우 사이에서 변환하고 코드에서 원하는 타입과 입력값의 타입이 정확히 일치하게
    하려면 헬퍼 함수 두 개가 필요하다.
"""


# 파이썬 3, str이나 bytes를 입력으로 받고 str을 반환하는 메서드가 필요
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf=8")
    else:
        value = bytes_or_str
    return value # str 인스턴스


# str이나 bytes를 받고 bytes를 반환하는 메서드로 필요하다.
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return bytes_or_str # bytes 인스턴스


"""
    파이썬에서 로 8비트 값과 유니코드 문자를 처리할 때는 중대한 이슈 두 개를 알아야 함
    파이썬 2에서 str이 7비트 아스키 문자만 포함하고 있다면 unicode와 str 인스턴스가 
    같은 타입처럼 보인다는 점이다.
    - 이런 str과 unicode를 + 연산자로 묶을 수 있다.
    - 같은(equality)과 같지 않음(inequality) 연산자로 이런 str과 unicode를 
    비교 가능
    - '%S' 같은 포맷 문자열에 unicode 인스턴스를 사용할 수 있다.
    
    파이썬 3에서는 bytes와 str 인스턴스는 심지어 빈 문자열이라도 절대 같지 않음
    
    두 번째 이슈는 파이썬 3에서 내장 함수 open이 반환하는 파일 핸들을 사용하는 연산은
    기본으로 UTF-8 인코딩을 사용한다.
    파이썬 2에서 파일 연산은 기본으로 바이너리 인코딩을 사용한다.
    파이썬 3에서 open에 새 encoding 인수가 추가되었으며 기본값은 utf-8이다.
    따라서 파일 핸들을 사용하는 read나 write 연산은 바이너리 데이터를 담은 
    bytes 인스턴스가 아니라 유니코드 문자를 담은 str 인스턴스를 기대한다.
    
    단, 바이너리를 쓰게하려면 바이너리 쓰기 모드인 ('wb')로 오픈하면 된다.
    
    파일 읽기도 동일하다.
"""