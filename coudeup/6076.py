# range(n) 은 0, 1, 2, ... , n-2, n-1 까지의 수열을 의미한다.
# 예를 들어 range(3) 은 0, 1, 2 인 수열을 의미한다.

# for i in range(n) :    #range(n)에 들어있는(in) 각각의 수에 대해서(for) 순서대로 i에 저장해 가면서...
# 이때의 for는 각각의 값에 대하여... 라는 for each 의 의미를 가진다고 생각할 수 있다.

# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)
# 형태로 수열을 표현할 수 있다. 시작 수는 포함이고, 끝 수는 포함되지 않는다. [시작, 끝)
# 증감할 수를 작성하지 않으면 +1이 된다.

# 반복 실행구조에 반복 횟수를 기록/저장하는 변수로 i를 자주 사용하는데,
# i 는 반복자(iterator)를 나타내는 i라고 생각할 수 있다. i, j, k ... 알파벳 순으로 사용하기도 한다.


n = int(input())
for i in range(0, n+1):
    print(i)
