"""
    Better way 13: try/except/else/finally에서 각 블록의 장점을 이용하자

    파이썬에는 예외 처리 과정에서 동작을 널을 수 있는 네 번의 구분되는 시점이 있다.
    try, except, else, finally

    finally 블록
    예외가 발생해도 정리 코드를 실행하고 싶을 때 사용한다.(ex, 파일 핸들러 등등을 종료)
"""

handle = open('/tmp/random_data.txt')  # IOError가 일어날 수 있음
try:
    data = handle.read()  # UnicodeDecodeError가 일어날 수 있음
finally:
    handle.close()  # 이후에 항상 실행됨

"""
    else 블록
    코드에서 어떤 예외를 처리하고 어떤 예외를 전달하지를 명확하게 하려면 
    try/except/else를 사용해야 한다. try 블록이 예외를 일으키지 않으면 else 블록이
    실행된다. else 블록을 사용하면 try 블록의 코드를 최소로 줄이고 가독성을 
    높일 수 있다.
"""


def load_json_key(data, key):
    import json
    try:
        result_dict = json.loads(data)  # ValueError가 일어날 수 있음
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]  # KeyError가 일어날 수 있음


"""
    else 절은 try/except 다음에 나오는 처리를 시각적으로 except 블록과 
    구분해준다. 그래서 예외 전달 행위를 명확하게 한다.
    
    try: 예외가 발생할 수 있는 로직을 감싼다.
    except: 예외가 발생하면 예외를 처리한다.
    else: except 블록과 구분되며 예외전달을 명확하게 한다.
    finally: try에서 사용한 종료가 필요한 객체들을 종료한다.
    
    아래는 예시 
"""
UNDEFINED = object()


def divide_json(path):
    import json
    handle = open(path, 'r+')   # IOError가 일어날 수 있음
    try:
        data = handle.read()    # UnicodeDecodeError가 일어날 수 있음
        op = json.loads(data)   # ValueError가 일어날 수 있음
        value = (
            op['numerator'] /
            op['denominator'])  # ZeroDivisionError가 일어날 수 있음
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()
