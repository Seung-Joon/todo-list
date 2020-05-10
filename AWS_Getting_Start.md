# AWS 시작해보기.


## 1. 인스턴스 생성 
### 먼저 django 가 돌아갈 EC2 인스턴스를 할당받아야 한다.
  * 서울리전 -> EC2 인스턴스 생성. (가난한 개발자이므로 프리티어를 사용함.)
  * OS 환경은 ubuntu로 설정.
  * 키체인을 다운로드 받고 **반드시 안전하고, 기억날만한 장소에 보관한다.** (github에 public으로 올렸다간 어마어마한 과금이 될수 있으므로 **주의!!** 
  * 키체인을 user만 읽기 전용으로 권한을 설정한다. chmod 400 keychain.pem (이때, keychain은 본인이 다운받은 keychain의 이름으로 한다.)
  * sudo ssh -i path/kechain.pem username@public_dns로 연결(Mac)

#### 이렇게 인스턴스를 먼저 생성한다. **인스턴스 생성시 본인이 선택한 옵션이 프리티어에 해당하는지 꼭 꼭 확인하자.**

## 2. Github Setup (ubuntu 기준)
  * sudo apt-get install git                                        -> Git으 설치한다. 근데 대부분 깔려있더라.
  * git config --global user.name "Seung-Joon"                      -> user name도 설정해주고.
  * git config --global user.email "tmdwns02556@gmail.com"          -> email도 설정해준다.
  * git config --list                                               -> 설정된 정보를 확인해 볼까?
  ```
  user.name=Seung-Joon
  user.email=tmdwns02556@gmail.com
  ```
  #### 이런식으로 나온다. 음..설정이 잘 되었군.
  
  * git config --global color.ui "auto"                             -> 파일의 상태를 쉽게 알 수 있도록 색이 자동으로 표시되도록 설정하자.
  ```
  user.name=Seung-Joon
  user.email=tmdwns02556@gmail.com
  color.ui=auto
  ```
  #### 잘 설정되었다.
  
## 3. Github에 있는 파일 가져오기.
 * mkdir sever                                                      -> 적당한 디렉터리를 하나 만든다.
 * cd sever                                                         -> 이동하고
 * git init                                                         ->
 * git clone https://github.com/Seung-Joon/todo-list.git            -> 깃허브 레포지토리에 있는 파일을 다운로드한다.
 
## 4. Python 환경 셋팅
 #### django와 django_rest_framework를 사용할건데 먼저 패키지를 설치를 해야한다.
 * pip3 --version
 ```
 (대충 pip 모듈이 없다는 내용)
 ```
 #### 엇...pip를 썻 모듈을 설치해야하는데..pip 모듈이 없다. 설치를 해보자.
 * sudo apt-get update
 * sudo apt-get upgrade            -> 먼저 업그레이드를 해주자 **업그레이드 안하고 했더니 에러떴음.**
 * sudo apt install python3-pip    -> 나는 python 3.x.x 버전을 사용할것익 때문에 python3 용 pip 모듈을 설치하였다.
 
 * pip3 --version
 ```
 (대충 pip 모듈이 있고 버전이 몇이라는 내용)
 ```
 
 #### 이제 정상적으로 설치가 됐으니 필요한 모듈들을 깔아보자.
 * python3 -m pip install django                   -> 기본적인 장고 모듈이다.
 * python3 -m pip install djangorestframework      -> 나는 장고로 rest-api를 만들껀데 편하게 만들고싶으니까 해당 프래임워크를 사용할꺼다.
 
 #### 근데 자꾸 python3를 쳐야만 python3 버전이 열린다. 3숫자 치기 싫으니까 환경변수 설정을 바꿔볼꺼다.
 * python -V
 ```
 Python 2.7.17
 ```
 #### 현재 python 환경 변수가 2.7로 설정되어있는것을 확인할 수 있다.
 
 * python3 -V
 ```
 Python 3.6.9
 ```
 #### 현재 설치되어 있는 python3 버전은 3.6.9가 설치되있다.
 
 * alias python='/usr/bin/python3.6'
 #### 이거 하나만 쳐주면 python -> python3.6으로 매칭된다. 와!!!!
 
 
 
 
 
 
  



