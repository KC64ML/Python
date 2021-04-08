# '한 눈에 끝내는 파이썬3 기초' 정리 #

# 프로그래밍이란?
- 프로그램이란 특정 목적을 위해 컴퓨터에 내리는 명령의 집합
- 프로그램을 만드는 행위를 프로그래밍, 간단한 개발
- 코딩은 컴퓨터 언어로 작성하는 논리적인 글인 '코드'를 작성하는 과정
- 컴퓨터 언어에 대한 이해와 기계의 사고방식(처리 방식)에 대한 이해가 필수

# 파이썬이란?

* 파이썬의 빠른 개발 속도와 생산성을 두고 개발자들 사이에서 유행처럼 퍼진 말
* 높은 생산성을 가지고 있다.
* Django 오픈 소스 기반의 웹 프레임워크 사용가능 (반복적인 작업을 줄여주는 뼈대 코드)
* 빅 데이터 분석
  * 인터프리터: 소스 코드를 바로 실행하는 컴퓨터 프로그램 혹은 그러한 환경(실시간 통역)
    * 별도 실행 파일이 존재하지 않음, 수정 쉬움, 실행 속도가 느림
    * 대표 언어 : Python, Javascript
  * 컴파일러(C, JAVA가 해당) : 특정 프로그래밍 언어를 다른 프로그래밍 언어로 번역하는 프로그램
    * 실행 가능한 프로그램 생성, 생성된 프로그램은 목적프로그램 또는 바이너리 파일이라고 부름, 실행 속도 매우 빠름
    * 대표 언어 : C, C++
* 인덴트(띄어쓰기, 공백)에 매우 민감한 언어이다.
  * IndetationError : unexpected indent 발생
    * 공백에 관한 에러, 띄어쓰기 관련 에러

# 콘솔 입력의 기본

* input() : 사용자가 콘솔 창에 직접 입력한 값을 변수에 할당(=저장)
  * ex) a = input("값을 입력하세요 : ")
    * print(a)
* input() : 입력한 값을 '문자열'로 저장
* 정수형 변환 : int(input())
* 변수의 자료형 확인 : type()
* 숫자형
  * 정수(int) : 1, 2, 3, 4
  * 실수(float) : 3.15, -23.1
  * 복소수(complex) : j, 2j, 3 + 2j, 1 + 2j
    * 실수 부 : 변수.real, 허수부 : 변수.imag, 켤레복소수 : 변수.conjugate()
  * 16진수 : 0xDA
  * 2진수 : 0b110101
* 정수 + 실수 : 실수형, 정수 + 복소수 : 복소수



# bool 형

* True, False 앞 글자는 반드시 대문자 입력
  * if (a) : #만약 (a)가 참이라면
  * else : # 아니면
* 주어진 조건에 대한 참/거짓 뿐만 아니라 값의 존재 여부에 따라서 또한 판별한다.
  * 존재하면 참, 존재하지 않으면 거짓
  * "Goorm", "hello"등 어떤 문자열 : True
  * "" : false
  * [1,2,3] : True
  * [], (), {} : False
  * 1 : True
  * 0, None : False
* a = "Hello"
  * if(a == True)  # false



# 수식연산자

* 수식 연산자 : 두 개의 피연산자를 요구하는 이항 연산자(binary operator)
  * ** : 왼쪽 값을 오른쪽 값만큼 제곱한다. (정수, 실수, 복소수)
  * // : 왼쪽 값을 오른 쪽 값으로 나눈 몫을 반환한다. (정수, 실수)
* 문자열 + 숫자는 불가능, 두 개의 자료형이 같거나 숫자이면 자유롭게 연산가능



# 논리연산자

* and : 두 값이 모두 True일 때만 True
  * True and True = True
  * True and False = False
* or : 두 값 중 하나라도 True이면 True를 반환한다.
  * True or True = True
  * True or False = True
* not : False 이면 True를, True이면 False 반환한다.
  * not True = False
  * not False = True



# 비트연산자

* 컴퓨터는 1과 0으로 이루어진 2진수 비트(bit)만 이해할 수 있기 때문에 모든 데이터를 2진수로 변환하여 저장한 뒤 연산한다.
  * & : 두 값을 비트 단위로 AND 연산한다.
  * | : 두 값을 비트 단위로 OR 연산한다.
  * ^ : 두 값을 비트 단위로 XOR 연산한다.
  * ~ : 비트를 보수연산한다.
  * or : 하나 이상의 입력값이 1이면 1을 출력
  * xor : 입력 값이 같지 않으면 1을 출력
  * &= : 값에 AND 비트 연산 후 대입
  * |= : 값에 OR 비트 연산 후 대입
  * ^= : 값에 XOR 비트 연산 후 대입



# 문자열 자료형

* 따옴표로 감싸진 문자열에 문자가 특별하게 인식되는 경우

  1. 따옴표 안에 같은 종류의 따옴표를 사용한 경우
     * ' 큰 "따옴표 출력" '
     * """ 큰 "따옴표" 출력"""
     * " ' 작은 따옴표 출력 ' "
     * \\" : 큰따옴표
     * \\' : 작은 따옴표 처리
     * \\\ : 백슬래시
     * 이스케이프 시퀀스(escape sequence) : 백슬래쉬(\\)로 표현
     * \b : 백스페이스(글자 하나를 지움)
     * \t : 탭
  2. 이스케이프 시퀀스(Escape sequence)를 사용한 경우
  3. 문자열 포매팅을 한 경우

  

# 문자열 연산

* Concatenation : 문자열을 덧셈 부호를 이용해 연결한 것
  * 문자열 곱셈 : 문자열 * 정수
    * ex) str = "Hello"; num = 5
    * print(str * num)
    * 결과 : Hello Hello Hello Hello Hello



# 인덱싱과 슬라이싱

* ASCII CODE : 영문 키보드를 사용해 입력할 수 있는 모든 문자에 숫자를 매칭시킨 표준 체계
  * 아스키코드 출력 : print(ord("A"))


![ascii code](https://user-images.githubusercontent.com/72541544/111650369-91cbaf80-8848-11eb-9fb9-a15fa103b45c.png)
###### 사진 주소 : [인덱싱과 슬라이싱 - 한 눈에 끝내는 파이썬3 기초 (goorm.io)](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* 인덱싱
  * 문자열은 하나로 보일지라도 문자마다 인덱싱이 가능하다.
  * 인덱싱은 문자열에 포함된 각 문자에 대해 순차적으로 번호를 매기는 것을 뜻한다.
    * ex) APPLE => 0, 1, 2, 3, 4
    * str[0] = A
  * 변수 이름[인덱스 값]
  * 배열 뒤에서 접근할 때 : -1부터 시작
  * 문자열 자료형은 Immutable 타입으로 한 번 초기화하면 사용자 임의로 값을 바꿀 수 없다.
* 슬라이싱
  * 지정 범위만큼 데이터 요소를 잘라내는 기능
    * 변수명[첫 인덱스 번호:마지막 인덱스 번호]
      * 첫 인덱스 번호 ~ 마지막 인덱스 번호 - 1
      * 첫 인덱스 번호 생략할 시 : 0번부터 범위를 지정
      * 뒤 인덱스 번호 생략할 시 : 마지막까지 범위를 지정
  * -를 붙임으로써 뒤 요소부터 접근 가능
    * a = "Hello goorm!"
    * a[0:-5] => Hello
    * a[7:-11] => 빈칸이 반환된다. (첫 인덱스 값보다 마지막 인덱스 값이 작으면 빈칸 반환)



# 문자열 포매팅

* 문자열 포매팅 : 사용자가 문자열의 포맷을 지정하는 것
  * ex) 서울의 12일 화요일 기온은 26도입니다. 라는 문자열을 출력한다고 가정할 때
    * 도시 이름, 날짜, 요일, 온도는 충분히 바뀔 수 있다.
  * 문자열에 포함된 변수 값이 계속 변경된 코드 가독성이 떨어지지만
  * 포매팅을 이용하면 좀 더 가독성을 높일 수 있다.

![포맷 코드](https://user-images.githubusercontent.com/72541544/111650328-88424780-8848-11eb-9d5b-2e3d10e6b226.png)
###### 사진 주소 : [문자열 포매팅1 - 한 눈에 끝내는 파이썬3 기초 (goorm.io)](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* %d, %s와 같은 포맷 코드를 입력한 뒤 문자열 뒤에 %를 시작으로 변숫값을 작성한다.
  * city = "seoul"
  * today = 12
  * announcement = "%s의 %d일" %(city, today)
  * print(announcement)
* 문자열은 숫자형으로 포맷 코드를 사용하여 표현할 수 없다. 
  * 숫자형은 문자열 포맷코드를 사용가능
* 정수형은 실수형으로, 실수형을 정수형으로 포매팅 가능하다.
  * 실수형을 정수형으로 표현하면 소수점 첫째 자리에서 내림 처리한다.
* 출력할 때 출력 폭을 지정할 수 있다.
  * %(폭)d 형식으로 입력하면 자동으로 오른쪽 정렬되고 왼쪽에는 공백으로 채워진다.
  * 이때 만약 포매팅하고 싶은 요소가 숫자라면 (폭) 앞에 0을 입력하여 빈 곳을 0으로 채울 수 있다.
  * 왼쪽으로 정렬하고 싶다면 %-(폭)d 형식으로 입력한다.

* % 문자열 포매팅은 문자열 안에서 사용한 포맷 코드와 뒤에 입력한 변수가 1대1 대응
* format() : %d 같은 포맷 대신에 "{인덱스 값}"을 사용하여 format() 함수 안의 값을 순서 상관없이 사용할 수 있다.
  * name1 = "김구름" name2 = "박에듀" age = 25 height = 181.123 print("저의 이름은 {2}입니다. 그리고 나이는 {1}살이고 키는 {0}cm입니다.".format(height, age, name1)) print("{1}의 나이:{0}, {2}의 나이: {0}".format(age, name1, name2))
  * 문자열.format(요소1, 요소2, ...) format함수를 이용한 포매팅 사용형식
* format() 함수 내에서 변수를 선언하고 초기화하면 그 값을 "{변수명}" 형식으로 바로 받아올 수 있다.
  * print("저의 이름은 {1}입니다. 그리고 나이는 {age}살이고 키는 {0}cm입니다. 제 가장 친한 친구는 {name}입니다.".format(181.12, "김구름",height = 181.123, age = 25, name = "박에듀"))
* format() 을 이용하여 포맷 코드에 특정 값을 추가하여 출력 폭을 지정할 수 있다.
  * "{인덱스값 or 변수:(출력형식)}".format(요소) 형식으로 입력

![폭](https://user-images.githubusercontent.com/72541544/111650397-98f2bd80-8848-11eb-9442-2b5c5662b1c7.png)
###### 사진 주소 : [문자열 포매팅2 - 한 눈에 끝내는 파이썬3 기초 (goorm.io)](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* f 문자열 포매팅 : 3.6버전에서 새로 사용할 수 있게 된 포매팅 방식
* format() 함수처럼 포맷 코드는 그대로 '{}'를 사용하고 문자열 앞에 f만 붙여 쉽게 사용 가능

# 문자열 함수

* 매우 유용하고 직관적인 내장 함수
* 함수는 특정 기능을 수행하기 위해 제작된 명령 묶음
* 함수명 옆의 괄호 안에 들어가는 값을 전달 인자

![function](https://user-images.githubusercontent.com/72541544/111740155-971c0f00-88c7-11eb-86c6-ca2258af9640.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* 변수 이름(혹은 문자열 자체).함수() 형태로 작성하여 사용
  * len(변수 혹은 자체) : 자료형 길이



# 리스트

* 값의 집합: 리스트
  * list : 값의 집합
  * 리스트 이름 = [요소1, 요소2, ...]
  * 비어있는 리스트를 선언 : 리스트 이름 = list()
    * 리스트는 꼭 같은 자료형끼리 묶지 않아도 사용할 수 있다.
    * 리스트안에 리스트가 들어가는 것도 가능하다.
* 인덱싱과 슬라이싱
  * 문자열 인덱싱과 마찬가지로 가장 앞에 있는 요소부터 0, 1, 2, ~ 순차적으로 번호 인덱스를 부여받는다.
  * 인덱싱한 값끼리 연산 또한 가능하다.
* 리스트 연산과 수정
  * 리스트에서는 문자열 수정 가능하다.
    * 요소를 수정하려면 "리스트 이름[인덱스 값] = 수정값" 형식으로 코딩해야 한다.
    * 리스트의 요솟값을 인덱싱을 이용해 수정할 때 1대1 대응
    * numbers[4:5] = [80] : 슬라이싱으로 값을 수정할 때는 단일 값이 아닌 리스트로 대입해야한다.
    * number[2:6] = "hello" : 슬라이싱으로 값을 대입할 때 슬라이싱한 범위에 문자열의 문자를 순차적으로 하나씩 대입한다.
    * number[2:3] = ['a', 'b', 'c'] 와 같이 슬라이싱한 범위에 리스트를 넣으면 대입할 리스트의 구성 요소들이 numbers에 완전히 포함된다.
    * number[8] = ['a', 'b', 'c'] 는 리스트 내 리스트 형태로 수정된다.
* 리스트 삭제
  * 리스트에서 요소만 삭제하려면 인덱싱과 슬라이싱으로 기존 요소를 빈칸으로 수정한다.
    * 공백 처리 : 인덱싱 : a[4] = "", 슬라이싱 : a[1:3] = []
    * del 키워드 : 객체 자체를 삭제한다.

* 리스트 함수
  * 추가하는 함수

![listfunction](https://user-images.githubusercontent.com/72541544/111740157-97b4a580-88c7-11eb-8813-9628650ac438.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)


* insert : 하나의 값만 넣을 수 있다. (하나의 값에는 리스트 또한 가능하다.)
* append : 리스트값을 넣으면 리스트 또한 하나의 값으로 처리된다.
* extend : 리스트값을 넣으면 리스트 괄호가 풀리고 그 리스트 안에 포함되었던 요소의 개수만큼 값이 입력된다.
  * 삭제하는 함수

![deletefunction](https://user-images.githubusercontent.com/72541544/111740125-8c617a00-88c7-11eb-8a1b-a37eb2986ff5.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* 리스트 요소들이 순서대로 정리
  * 요소들을 정렬하고 순서를 바꾸는 함수

![selectchangefunction](https://user-images.githubusercontent.com/72541544/111740162-984d3c00-88c7-11eb-8b96-ce78e654f3cb.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* sort() : 오름차순 정렬, reverse() : 내림차순 정렬
  * 리스트의 정보를 알아내는 함수

![listinformationfunction](https://user-images.githubusercontent.com/72541544/111740158-984d3c00-88c7-11eb-8cb0-c0e1661e832c.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)
 
* 파이썬 함수들은 다른 언어에 비해 굉장히 직관적이고 간결하다.
* 리스트는 파이썬 프로그래밍을 할 때 자주 쓰이므로 리스트 함수를 많이 연습해야 한다.
  * len() : 값의 길이(개수)


* 리스트의 심화 개념 : 값 할당
  * 파이썬은 사람의 직관에 조금 더 친화적인 언어
  * 빈 리스트를 먼저 생성하고 값을 초기화하면 안된다.
  * 리스트 값의 개수와 값을 초기화하지 않고 빈 리스트만 선언했다면 공간을 마련하고 값을 하나씩 추가해야한다.
    * append() 함수를 사용하여 공간을 마련하고, 값을 출력한다.
    * extend() 함수를 사용하면 여러 값을 한 번에 추가가 가능하다.
  * list에서 0, 1, 2, 3에서 2를 삭제하면 => 0, 1, 2로 된다.
  * del 키워드는 칸 자체를 삭제한다.
    * del drawer[3] 을 했을 때 3은 삭제되고 4에 있던 것이 3으로 내려온다.
    * drawer[3] = "" => 인덱스 3에 빈칸을 할당 (칸 자체 삭제가 아니다.)
* 인덱스는 사용자가 임의로 지정하는 것이 아니라 차곡차곡 쌓여있는 서랍처럼 차례대로 값이 부여되는 것
  * 없는 서랍에 물건을 넣는 실수는 하지 않아야 한다.



# 딕셔너리(Dictionary)

* 딕셔너리에는 순서가 존재하지 않는다.
* 딕셔너리는 "key : value"의 형태로 값을 저장한다.
* 중괄호를 이용해 딕셔너리 자료형을 사용하려면 key 와 value 모두 사용자가 지정해야한다.
  * "딕셔너리 이름 = {key:value1, key2:value2, ...}"
  * "딕셔너리 이름 = dict(key1=value1, key2=value2, ...)"
* 딕셔너리는 빈 딕셔너리({})를 초기화해도 함수 사용 없이 "변수이름[key] = value" 코드로 값을 추가할 수 있다.
* del 키워드로 간단하게 삭제할 수 있다.
* key와 value를 다룰 때 주의해야 할 점
  * key는 value를 찾기 위한 유일한 값
  * key에 리스트는 사용할 수 없다.
  * value에는 어떤 값이든 상관 없이 올 수 있다.



* 딕셔너리 함수

![딕셔너리함수](https://user-images.githubusercontent.com/72541544/111740152-971c0f00-88c7-11eb-996b-95701c222877.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)


1. x.key()가 실행되면 dic_keys라는 객체를 반환한다.
   * 리스트 형태로 변형 : list(x.keys())
2. clear 함수를 사용하면 빅 디셔너리로 바뀐다.
3. key가 존재하지 않으면 'None'을 반환한다.
   * 다른 값을 출력하고 싶다면 "x.get(key, 출력하고 싶은 값)"으로 작성한다.
4. key 값이 존재하면 True, 존재하지 않으면 False를 반환한다.

ex) mem = {"김구름": 25, "박에듀": 23, "온라인": 24}

names = list(mem.keys()) => 새로운 리스트 변수에 초기화

print(mem.values()) => dict_values([25, 23, 24])

print(list(mem.values())) => [25, 23, 24]

print(mem.items()) => dict_items([('김구름', 25), ('박에듀', 23), ('온라인', 24)])

print(mem.get("정판교", "없습니다"), mem.get("온라인", "없습니다")) => 없습니다 24

exist = '한바로' in mem;	print(exist) =>  false

mem.clear()	print(mem) => {}

* D['C'] = 3
  * 딕셔너리에 'C' = 3 을 추가할 때 코드
* del D['C']
  * 딕셔너리에서 'C':3을 삭제



# 튜플(Tuple)과 집합(Set)

* Tuple : lmmutable 타입의 리스트
* 집합 : 중복과 순서가 없는 자료형

* 변하지 않는 Tuple

![변하지않는 튜플](https://user-images.githubusercontent.com/72541544/111896500-67067480-8a5d-11eb-9f6c-a6356f90e49f.png)
###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

  * Immutable 형식으로 값을 수정할 수 없다.
  * 리스트와 딕셔너리는 Mutable형식으로 값을 언제든지 추가 및 수정할 수 있다.
  * 데이터 처리할 때는 리스트와 딕셔너리를 주로 사용한다.
  * Immutable 자료형이 필요할 때 : 값을 언제든 수정하고 삭제할 수 있는 것은 굉장히 유용하지만, 데이터 관리에 취약할 수 있다.

* Tuple

  * Tuple은 값을 수정할 수 없는 것과 선언 방법을 제외하고는 list와 거의 유사하다.

  * list는 대괄호([])를 사용해 선언하는 반면에 Tuple은 소괄호(())를 사용해 선언한다.

    * t1 = ('a', 'b', 'c', 1, 2, 3)

  * Tuple을 사용한다면 괄호를 사용하지 않아도 튜플로 초기화된다.

    * t3 = "goorm", 'b', "hello", 1, 2, 3 

  * 한 개의 요소만 초기화할 때는 요소 뒤에 콤마를 꼭 입력해야한다.

    * t2 = ("hello",)

  * 어느 자료형이든 요소로 저장할 수 있다. (list, dictionary, Tuple, 집합 저장 가능)

    * t4 = ([1, 2, 3], {"사과":"apple", "포도":"grape"}, ('a', 'b', 'c'), s1)

  * Tuple 안에 있는 Mutable한 값은 수정 가능하다.

    * Tuple 자체의 요소는 데이터 초기화와 동시에 정해진 값이기에 수정할 수 없다.

    * Mutable하다면 요소의 요소를 수정할 수 있다.

      * 서랍장이 개수와 내용물까지 채워져 있는데 서랍 안에 칸을 조정할 수 있는 조그만 수납 칸이 있다면 그 조그만 칸은 수정할 수 있다.

    * s1 = list(set([1,2,3]))   =>   다음에 배우게 될 집합 Mutable 타입

    * t4[3] [2] = "edit"  =>  중요: 튜플 요소가 Mutable하면 수정할 수 있음

      t4[1] ["사과"]= "edit"

      t4[0] [2]= "edit"

  * Tuple은 저장되어있는 값을 수정하지 않는 선에서 list의 기능을 모두 지원한다.

    * 대표적으로 인덱싱과 슬라이싱
    * Tuple에서는 list에서 사용하는 함수 중 값을 변경하지 않는 함수가 사용 가능하다.
      * t = (13, 6, 9)
      * print(t.index(13)) => 0

  * Python에서는 중간에 띄어쓰기 넣을 때 print(a + " " +b) 와 같이 사용한다.

* 배열 안 ()와 {}의 차이는?

* 문자열 길이

  * len(문자열)

* A =  [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] 

  * for i in A:

    // A안에 있는 요소

* 파일 열기/생성 및 쓰기

  * 파일 객체 이름 = open("파일 경로/파일 이름","파일 열기 모드") 형식으로 생성
  * 파일 경로를 따로 지정하지 않으면 현재 지정된 경로에 파일을 생성한다.

![파일열기모드](https://user-images.githubusercontent.com/72541544/111650369-91cbaf80-8848-11eb-9fb9-a15fa103b45c.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* 읽기 모드
  * f = open("test.txt",'r')
  * f.close()
* 쓰기 모드
  * write("입력할 값(내용)")
    * write 안에 들어가야 할 인자는 문자열만 가능
  * f = open("data/test.txt","w")
  * f.close()





# 중복과 순서가 없는 집합

* 집합을 사용할 때 : 중괄호 {} 를 이용하여 바로 선언 및 초기화하여 생성할 수 있다.
  * s1 = {3, 2, 5, 1, 8, 4, 3}
  * print(s1, type(s1))
* 이미 존재하는 다른 묶음 자료형을 집합으로 변경할 수 있다.
  * set(묶음 자료형)
    * 요소의 순서가 없다.
    * 중복되는 값은 한 개만 저장한다.
    * 딕셔너리는 key만 저장한다.
  * 묶음 자료형 : 전달 인자로 문자열, 리스트, 딕셔너리, 튜플등을 입력하면 그 값들의 집합으로 변경된다.
  * 집합에는 순서와 중복이 없다.
  * 집합은 리스트 혹은 튜플에 속한 요소의 중복을 제거하기 위한 필터로 사용
  * 인덱싱과 슬라이싱을 사용할 수 없다.
    * 사용하고 싶으면 리스트 혹은 튜플로 변환해야한다.
  * set() : 다른 자료형을 집합으로 변환
  * list() : 다른 자료형을 리스트로 변환
  * tuple() : 다른 자료형을 튜플로 변환
* 집합과 사용할 수 있는 함수

![집합 함수](https://user-images.githubusercontent.com/72541544/112588553-ef608d00-8e42-11eb-8f2e-2cd8e3b41af6.png)

사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* 집합의 요소를 다루는 다양한 함수

 ![집합 요소와 다양한 함수](https://user-images.githubusercontent.com/72541544/112588551-eec7f680-8e42-11eb-84b7-92c3df64857b.png)
 
사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* * 튜플은 한개의 원소로 사용할 수 있지만 리스트와 집합 자체는 집합의 원소로 사용할 수 없다.
  * update는 여러 값으로 인지해 각각 한 개의 원소로 저장한다.
  * add는 입력된 값을 한 개의 원소로 저장한다.



# 반복문

* while문
  * 조건이 참인 동안에 while 범위 안에 있는 코드를 반복
  * 범위 안에 포함된 내용을 반복해서 실행하는 기능
  * 조건문 아래 들여쓰기(tab) 코드
  * while 조건식 :
    * 조건식이 True일 때 종속된 코드 반복 실행
    * 무한 루프가 실행되었을 때 ctrl + c를 눌러 빠져나오기
* for문
  * 주어진 조건이 True일 때 포함된 내용을 반복하는 문법
  * for 변수 in range() :
    * range() 함수를 사용할 때 범위 내 변화 간격은 생략 가능
    * 생략하면 변화 간격으로 1로 자동 설정
    * for 변수 in range() : 를 사용할 때 리스트를 바로 for의 범위로 사용하면 in 다음에 리스트가 바로 오지만
    * 숫자로 범위를 지정하면 range(숫자)로 작성해야한다. 
* for문은 정해진 횟수나 인덱스에 접근할 때, while문은 특정 조건을 만족할 때 반복을 멈추는 흐름에서 많이 쓰인다.
* for문에서 집합 자료형의 요소에 접근할 때는
  * for in 값의 집합자료형 :
  * print()함수 안에서 end = ' '를 작성하면 end 키워드인 공백을 삽입한 뒤 데이터를 이어서 출력한다.
  * end = ',' 를 이용하여 한 줄에 표현할 수 있다.
  * 데이터를 한 줄에 표현하고자 한다면 end 용법을 사용한다.
  * 조건식의 변수를 여러 개 사용 가능하다.
  * 딕셔너리에 사용할 때는 Items라는 객체로 접근해야 한다.
* for문 활용
  * for in 값의 집합자료형
  * dic = {"human":"사람", "dog":"강아지"}
  * oddnums = (1, 3, 5, 7, 9)
  * evennums = [6, 8, 10, 22]
  * str = "Hello goorm!"
  * for i in oddnums:
  * print(i, end = ' ')
  * print()
  * for i in evennums:
  * print(i, end = ' ')
  * print()
  * for i in str :
  * print(i, end = ' ')
  * for key, val in dic.items():
  * print(key, value, end = ' ')
  *  
  * for num in [1,2,3,4,5,6,7] :    
  * print(num)    
  * 1
  * 2
  * ~
  * 7
  * for num in [1,2,3,4,5,6,7] :    
  * print(num, end = ',')
  * 1, 2, 3, 4, 5, 6, 7
  * 
  * num1 = [[1,2,3],[4,5,6]]
  * for i, j, k in num1:
  * print(i, j, k)  
  * => 1 2 3
  * => 4 5 6
  * => a b c
  *  
  * fruits = {"apple" : "red", "banana" : "yellow", "grape" : "purple", "melon" : "green"} 
  * for color in fruits.values():    
  * print(color, end = ' ')  => red yellow purple green
  * print() 
  * for fruit in fruits.keys():  
  * print(fruit, end = ' ')    => apple banana grape melon
  * print() 
  * for fruit, color in fruits.items():    
  * print("%s의 색은 %s" %(fruit, color), end = ', ')
  * => apple의 색은 red, banana의 색은 yellow, grape의 색은 purple, melon의 색은 green

# 조건문과 제어문

* 조건문
  * if문, elif문, else문
    * ex) if num == 4 :
  * 따옴표 혹은 괄호 안에 공백이거나 숫자 0이 입력되어 있으면 false로 처리한다.
    * if "" :   if 0 :     => false
    * if " " :  if 1 :     => true
* 비교 연산자
  * and, or, not
* 요소 in
  * in 키워드를 통해 리스트, 튜플, 문자열에 요소가 있으면 True, 없으면 False
  * not in : 요소가 존재할 때 False, 존재하지 않으면 True

* 제어문
  * break, continue



# 함수

* 함수의 대표 역할
  * 지정 기능을 실행하는 단위
  * 코드의 가독성과 프로그램의 효율성 증대
* <u>함수 정의</u> : 특정 기능을 위해 만든 여러 문장을 묶어서 실행하는 코드 블록 단위
* def 함수 이름 (매개변수 1, 매개변수 2, ...) :
  * 실행 구문
  * ~
  * return 반환 값
* 함수 호출
  * 함수 이름(전달인자1, 전달인자2, ...)
* def : 함수를 정의하는 키워드
  * ex) def inputnums() :
  *    a = 0; b = 0
  *  return a, b
  * n1, n2 = inputnums() // 반환 값이 두 개이니 두 변수에 초기화

## 매우 중요함(함수에서 처음 알게 된 부분)

* 함수에서 전역변수를 사용할 때

  * 함수안에서 전역변수 사용 알림으로 global 전역변수를 입력한다.

  * ex)

  * sum = 0

    def myfunc():

      global sum

      for num in range(0,5):

    ​    value = int(input())

    ​    sum += value

      print(sum)

    

    myfunc()



# 매개변수

* 가변 인자 함수 
  * 동일한 기능을 수행하지만 매개변수만 다른 함수
  * def 함수 이름(*매개변수)
  * 가변 인자는 튜플 형식으로 저장된다.
  * 함수에서 매개변수는 가변 인자와 일반 매개변수를 같이 사용할 수 있다.
  * 일반 매개변수는 가변 인자 앞에 입력해서 사용한다.
* 키워드 매개변수
  * 함수 매개변수 앞에 **를 입력하면 함수를 호출할 때 전달 인자를
  * key1 = value1, key2 = value2, key3 = value3 형식으로 입력해 딕셔너리 형태로 선언할 수 있다.
  * 출력시 key:value 값으로 분류된다.
  * key는 따옴표로 감싸지 않고 변수처럼 입력하여 사용해야 한다.
    * key에는 숫자 및 따옴표로 감싼 문자열은 입력할 수 없다. (변수처럼 입력하여 사용)
    * key는 값 자체 문자열로 저장, value는 변수, 숫자 가능
      * ex) func(1, 3, 5, 7, apple = "사과", a = num, num = 4)
      * def func (*nums, **kwargs) :
        * nums : 1, 3, 5, 7
        * kwargs : apple = "사과", a = num, num = 4
  * 순서 : 가변인자, 키워드 매개변수 (이 두개 순서 바꿀 수 없다.)
* 반환 값
  * 파이썬은 매개변수 이름만 입력하면 어떤 자료형을 입력하든 그대로 전달하는 편리함을 가지고 있다.
  * 반환 값 자체를 함수에 명시하지 않고 return 뒤에 반환할 값을 입력만 하면 된다.
  * 최소한 반환 값에 맞게 함수를 호출하면서 같은 개수의 변수를 할당해야 규칙
  * 반환 값들이 여러 개일 경우, 하나의 리스트나 튜플로 묶어 하나의 변수로 반환해준다.
  * 파이썬은 반환 값이 여러 개일때 자동으로 튜플로 반환한다.
  * return : 함수를 종료함과 동시에 값을 반환하는 키워드



# 전역변수와 지역변수

* 전역변수 : 코드 전체에서 사용할 수 있는 변수
  * 어디서든 참조가 가능하다.
  * 함수안에서 전역변수에 새로운 값을 '대입'하는 것은 불가능하다.



* * 전역변수 단점

    * 메모리를 비효율적으로 사용할 수 있다.
    * 값에 쉽게 접근할 수 있는 만큼 코드의 흐름을 파악하는데 방해될 수 있다.
    * 보통 전역변수는 변하지 않고 여러 기능에서 참조해야 하는 값으로 사용한다.

  * 전역변수 수정

    * global
      * 불가피하게 전역변수를 수정해야 하는 일이 발생한다면 global 키워드를 사용한다.

![global](https://user-images.githubusercontent.com/72541544/112588534-e7a0e880-8e42-11eb-9a93-607ec5134ab2.png)
사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

    * ex) def plusNum(n) :
          return n + num

      num = 3
      print(plusNum(17))

    * 결과 : 2

    * num을 수정한대로 변경된다.

    * global은 외부와 소통하는 흐름을 깨기 때문에 반환 값을 이용하여 전역 변수를 수정하는 것을 추천한다.

    * ex) num = 1 #전역변수 선언 

      def plusNum(a) : 

      a += 1 

      print(a)  

      return a 

      num = plusNum(num) 

      print(num)

      * 함수의 실행 결과를 누적, 가급적이면 global를 사용하지 않도록 한다.

* 지역변수 : 정해진 범위에서만 사용 가능한 변수

  * ex)  def plusNum(n) :
        return n + num

    num = 3
    print(plusNum(17))

  * num : 전역변수, n : 지역변수

* 문자열 길이

  * len(문자열)

* A =  [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] 

  * for i in A:

    // A안에 있는 요소


# 파일 열기/생성 및 쓰기

  * 파일 객체 이름 = open("파일 경로/파일 이름","파일 열기 모드") 형식으로 생성
  * 파일 경로를 따로 지정하지 않으면 현재 지정된 경로에 파일을 생성한다.

![파일열기모드](https://user-images.githubusercontent.com/72541544/113254361-6f826900-9301-11eb-9add-1d9352e6b046.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* 읽기 모드
  * f = open("test.txt",'r')
  * f.close()
* 쓰기 모드
  * write("입력할 값(내용)")
    * write 안에 들어가야 할 인자는 문자열만 가능
  * f = open("data/test.txt","w")
  * f.close()
* 파일 읽기 및 내용 추가

* ![파일 읽기](https://user-images.githubusercontent.com/72541544/113278267-b03bab80-931c-11eb-9970-a8ed3aa7b417.png)

* 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

  * 파일 함수를 사용한 후 close()함수로 파일을 닫기
  * 파일이 총 몇 줄인지 확인할 수 없는 경우 while문으로 모든 줄을 읽고 내용이 없으면 break문으로 빠져나오기
    * a = open("test.txt",'r')
    * while 1 :
      * line = a.readline()
      * if not line : break // line이 None이 되면 (=false) 반복문 탈출

* 개수 제한 없이 값을 입력받을 때 사용 되는 소스

  * list = []
  * while 1 :
    * data = input("빈칸을 입력하면 종료합니다.")
    * if not data : break
    * list.append(data)
  * print(list)

* 파일에 내용 추가하기

  * 파일을 쓰기 모드('w')로 열면 기존 내용이 삭제되고 새롭게 쓰인다.

* 추가 모드('a')': 기존 파일에 값을 이어 입력

* with문 : open() 과 close()를 합함

  * with문은 as와 함께 파일 객체 이름을 지정하고 블록을 만든다.
  * 블록 안의 코드들을 다 실행하고 블록을 벗어나면 자동으로 파일이 닫힌다.
  * with open("test.txt","w") as f:
    * for i in range(1, 4) :
      * data = "%d번째 줄입니다.\n" %i
      * f.write(data)
  * with open("test.txt",'r') as f:
    * lines = f.read()

* 파이썬은 tab과 space를 조심해야한다. (파이썬에서는 space를 사용 tab x)

  * 파일 입력 후 출력

  * A = []

    F = open("test.txt",'r')   // open("test.txt")

    for i in F.readlines() :

      temp = int(i) 

      A.append(temp)

    print(A)

    F.close()

    

  * f = open("data/add.txt",'w')   //open("data/add.txt")

    name = input("당신의 이름은 무엇입니까?\n")

    f.write(str(name))

    f.close()

    a = open("data/add.txt",'r')

    for x in a:

      print(x)

    a.close()



# 클래스

  * 인스턴스 : 생성된 객체는 클래스의 인스턴스

* class Triangle :

  * 클래스의 다양한 기능들도 클래스 안에서 수행되기 때문에 :를 사용해 범위를 명시해야한다.
  * pass는 실행할 내용이 없을 때 지나치라는 명시적 역할을 한다.
  * 객체 이름 = 클래스() 형식 : 클래스 객체 생성

* 클래스 변수, 인스턴스 변수

  * 클래스 변수

    * 클래스 안에서 선언된 변수
    * 같은 클래스로 만들어진 인스턴스끼리 공유하고 접근이 가능한 변수
    * 객체에서 클래스 변수 값을 변경하더라도 클래스에는 영향이 가지 않는다.

  * 인스턴스 변수

    * 메소드 : 클래스 안에서 어떠한 기능을 수행하는 함수, 이를 이용해 객체 정보를 지정할 수 있다.

    * 메소드와 일반함수 차이점

      * 메소드는 클래스 안에서 쓰이는 함수
      * 메소드는 사용자가 전달 인자를 입력하지 않는 매개변수 self를 사용
      * self는 실제 메소드를 사용할 때 사용자에게 전달 인자를 입력받지 않고 객체를 받는다.
      * ![self](https://user-images.githubusercontent.com/72541544/113278290-b893e680-931c-11eb-9816-6ef0a6e4535c.png)
      * 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)
      * 인스턴스 변수 : self.변수이름 형태로 사용하는 변수
        * 인스턴스 변수는 각 객체의 고윳값 (객체 클래스에 self라는 변수가 있다.)
        * 각기 다른 객체끼리 공유하지 않으며, 클래스 또한 인스턴스 변수에 접근하고자 할 때 self 없이 변수 이름만으로 접근할 수 없다.
      * 클래스 변수는 모든 객체가 공유하기 때문에 tri1.cal_count 형식으로 접근 가능

* 생성자와 메소드
  * 생성자(Constructor) : 객체 생성과 동시에 초깃값을 설정하는 메소드
    * ![생성자](https://user-images.githubusercontent.com/72541544/113296427-6b237380-9334-11eb-9a88-b497bc7245ef.png)
    * 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)
    * 생성자 사용할 때
      * ______init______ : 메소드 이름을 언더바 양쪽 2개로 설정하면 생성자로 인식된다.
  * 메소드
    * 인스턴스 메소드 : self로 인스턴스의 영역에 접근하는 메소드
    * 정적 메소드 : self 매개변수를 갖지 않는 메소드
      * 정적 메소드를 사용할 때 메소드 선언 윗줄에 @staticmethod라고 표시해야 한다.
      * 인스턴스 영역에 접근할 수 없다. (표시하지 않으면 인스턴스 메소드로 인식된다.)
    * 클래스 메소드 : 클래스 변수에 접근할 때 사용, cls로 클래스 변수를 전달 받는다.
      * 클래스 변수에 접근해야 할 때 클래스 메소드로 접근하는 것이 더용이하다.
      * 클래스 메소드를 사용할 때 메소드 선언 윗줄에 @classmethod라고 표시해야 한다.
      * 클래스로 직접 접근 가능하다.
      * self 같이 cls를 사용한다.
* 클래스 상속
  * 클래스 상속 선언 방법
    * class 부모클래스 :
    * ~
    * class 자식클래스(부모클래스):
  * 클래스에서 상속은 필수 기능이다.
  * 상속을 받는 자식 클래스는 부모 클래스의 메소드와 변수를 가져와 사용할 수 있다.
  * 메소드를 재정의(오버로딩)할 수도 있다.
  * 인스턴스의 영역에 찾고자 하는 변수가 없을때 
    * 클래스 영역으로 이동하여 해당 변수를 찾는다.
    * 클래스 영역에서도 없다면 부모 클래스로 이동해 변수를 찾는다.
  * 1. 클래스 메소드의 클래스 변수 접근 범위
       * 부모 클래스에서 선언된 클래스 메소드는 자식 클래스의 인스턴스의 클래스 변수를 참조한다.
       * 클래스 메소드는 부모 클래스에서 클래스 메소드를 실행
       * 자식 클래스 변수에 접근할 때 사용
    2. 인스턴스의 메소드 접근 범위
       * 자식 클래스로 생성한 인스턴스는 부모 클래스의 메소드에 접근할 수 있다.
       * 부모 클래스로 생성한 메소드는 자식 클래스의 메소드에 접근할 수 없다.
    3. 같은 이름으로 자식 클래스에서 재정의한 메소드
       * 메소드 오버라이딩(Method Overriding) : 자식 클래스에서 부모 클래스의 메소드를 재정의하는 것
  * print + print 는 두 줄로 출력된다.

# 클래스의 심화 개념

* 같은 정보를 공유하는 인스턴스는 다향성을 가진다.
* 다중상속
  * 파이썬에서는 부모 클래스를 여러 개 상속할 수 있다.
  * MRO(Method Resolution Order, 메소드 탐색 순서)에 따른다.
    * 파이썬은 다중 상속을 하면 상속을 명시한 클래스 목록 중 왼쪽에서 오른쪽 순서로 메소드를 찾는다.
      * class Third(First, Second):
        * First 클래스의 메소드를 실행
    * 클래스 변수의 이름이 같다면 클래스 메소드의 위치와 상관없이 왼쪽에 있는 클래스의 클래스 변수에 접근한다.
      * Third(First, Second) 일 때
      * third.printName()
        * printName : Second에 있다.
        * 이럴 경우, 실행은 Second에서 하지만 정적 클래스 변수는 First 클래스의 변수를 출력한다. (79page)
* 파이썬에서는 오버로딩을 지원하지 않는다.
  * 같은 이름의 메소드가 여러 번 선언되어 있다면 마지막 메소드가 실행된다.
* 파이썬은 다른 언어와 다르게 자료형에 대해 굉장히 유연하다.
* 빈 함수
  * def empty():
  * pass

# 모듈

* 효율성, 매우 복잡하고 긴 코드를 작성할 때 사용 용도에 따라 파일로 구분한 뒤, 다른 파일에서 해당 클래스나 함수가 필요할 때 가져와서 사용할 수 있다.
* 타인이 만들어 놓은 코드를 자신의 코드에 활용할 수 있다.
  * ex) 
  * import random
  * a = random.random()
  * b = random.randrange(1, 10)
  * c = ['a', 'b', 'c', 'd']
  * d = random.choice(c)
* import 모듈 이름
  * .py를 제외한 파일명만 가능
  * 포함하려는 파일이 현재 파일과 같은 디렉터리에 있어야 한다.
* import : 다른 파일에 있는 함수를 현재 사용 중인 파일에 포함하기 위한 함수
  * ex)
  * calculator.py
  * def add(a, b):
    * return(a+b)
  * def sub(a, b):
    * return(a-b)
  * main.py
  * import calculator
  * add_result = calculator.add(10,2)
  * sub_result = calculator.sub(10,2)
  * => main.py에서는 calculator.py 내에 있는 add, sub 함수를 빌려서 이용
  * => 이를 '모듈을 import 했다'라고 한다.
  * 만약 두 파일이 같은 경로에 있지 않다면 import 할 파일의 경로를 함께 적어주면 된다.
* from 모듈 이름 import 모듈 함수
  * ex)
  * my_module.py
  * def three_times(a):
  * return a * 3
  * main.py
  * from my_module import three times
  * print(three_times(10)) => 30
* from A import B를 사용할 경우, 해당 함수 앞에 모듈 이름을 붙이지 않고도 사용할 수 있다.
* from 모듈 이름 import * : 모듈 안에 있는 모든 함수를 사용



# 예외처리

* 프로그램 실행 중 특정 상황에 발생할 수 있는 예외의 경우를 미리 생각해서 그것을 처리할 수 있는 코드를 삽입하는 것

* 오류의 종류
  * SyntaxError : 잘못된 문법이나 표현을 사용해 주었을 때 발생
  * ![SyntaxError](https://user-images.githubusercontent.com/72541544/113961341-ddc6ae80-9860-11eb-9fc6-cfa3010b2d2e.png)
  * IndentationError : 들여쓰기가 잘못되었을 때 발생
  * ![IndentationError](https://user-images.githubusercontent.com/72541544/113961343-def7db80-9860-11eb-97fe-252674b65c87.png)
  * ZeroDivisionError : 0으로 다른 숫자를 나누려 했을 때 발생
  * ![ZeroDivisionError](https://user-images.githubusercontent.com/72541544/113961348-e0290880-9860-11eb-96ad-100e68eabf58.png)
  * 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)
* 오류 예외 처리하기
  * try:
  * 실행할 코드
  * except 에러이름 as 메세지변수:
  * 에러 발생시 실행할 코드
* finally : try문 종결된 후 무조건 실행되는 문
* except 문에 pass를 사용하면 아무 일도 없었던 것처럼 회피 가능
* 오류를 발생시키는 방법
  * try:
  * raise NameError     // 의도적으로 오류 발생시킴, raise 명령어
  * except NameError:
  * print("NameError occurred")
* 오류를 예외처리하기 위한 방법
  * try ~ except, try ~ else, try ~ finally
  * try :
  * 10 / 0
  * except ZeroDivisionError as e:
  * print(e)
  * else :
  * print("Success")
  * finally :
  * print("ZeroDivisionError Check")
