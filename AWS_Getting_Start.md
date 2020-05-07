# AWS 시작해보기.


## 1. 인스턴스 생성 
### 먼저 django 가 돌아갈 EC2 인스턴스를 할당받아야 한다.
  * 서울리전 -> EC2 인스턴스 생성. (가난한 개발자이므로 프리티어를 사용함.)
  * OS 환경은 ubuntu로 설정.
  * 키체인을 다운로드 받고 ** 반드시 안전학 기억날만한 장소에 보관한다.** (github에 public으로 올렸다간 어마어마한 과금이 될수 있으므로 **주의!!** 
  * 키체인을 user만 읽기 전용으로 권한을 설정한다. chmod 400 keychain.pem (이때, keychain은 본인이 다운받은 keychain의 이름으로 한다.)
  * sudo ssh -i path/kechain.pem username@public_dns로 연결(Mac)

### 이렇게 인스턴스를 먼저 생성한다. ** 인스턴스 생성시 본인이 선택한 옵션이 프리티어에 해당하는지 꼭 꼭 확인하자. **

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
  **color.ui=auto**
  ```
  #### 잘 설정된것 같다.
  
  



