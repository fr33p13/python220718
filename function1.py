#fucntion1.py
#함수정의

def time(a,b):
    return a+b, a*b

#함수호출
result = time(3,4)
print(result)

#함수정의
def setValue(newValue):
    x = newValue
    print("내부 함수: ", x)

#호출
result = setValue(5)
print(result)

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM","SPAM"))
