* 문자열 길이

  * len(문자열)

* A =  [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] 

  * for i in A:

    // A안에 있는 요소

* 파일 열기/생성 및 쓰기

  * 파일 객체 이름 = open("파일 경로/파일 이름","파일 열기 모드") 형식으로 생성
  * 파일 경로를 따로 지정하지 않으면 현재 지정된 경로에 파일을 생성한다.

![파일열기모드](D:\Computer_Science\Study\Python\Django_Python\Python\write\Day 6\파일열기모드.png)

###### 사진 주소 : [한 눈에 끝내는 파이썬3 기초](https://edu.goorm.io/lecture/17902/%ED%95%9C-%EB%88%88%EC%97%90-%EC%9D%BD%EB%8A%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC3-%EA%B8%B0%EC%B4%88)

* 읽기 모드
  * f = open("test.txt",'r')
  * f.close()
* 쓰기 모드
  * write("입력할 값(내용)")
    * write 안에 들어가야 할 인자는 문자열만 가능
  * f = open("data/test.txt","w")
  * f.close()



