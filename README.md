
### 유리 재활용 및 재사용 목적 프로젝트 유리온 라즈베리파이 기능 및 개발 과정

#### 개발 환경
- vscode, VNC viewer, python, RaspberryPi 4 이용

#### 기능

- 특정 횟수 이상 문이 열리면 AWS로 MQTT pub
- rfid MQTT sub
- servo motor pub
- 웹캠을 이용해 사진 찍고, 찍은 사진 S3로 저장
- AI 모델 이용
- 결과값에 맞는 음성 출력

#### 서버 기동 방법
$ python mainserver.py

![스크린샷(83)](https://user-images.githubusercontent.com/50413112/103846563-bdf8e080-50e1-11eb-837d-3cd8effb5952.png)
![스크린샷(84)](https://user-images.githubusercontent.com/50413112/103846570-c18c6780-50e1-11eb-8a02-d51cee56face.png)
![스크린샷(85)](https://user-images.githubusercontent.com/50413112/103846576-c3eec180-50e1-11eb-90e6-1ed5e22e42d2.png)
![스크린샷(86)](https://user-images.githubusercontent.com/50413112/103847778-4f695200-50e4-11eb-907f-cfa7083ddaef.png)

융합 프로젝트 5조 이리온 원종아 해야 할 일, 진척도



#### 11/27 해야 할 일

- 하드웨어 도안 완성 (정면, 측면, 위)(길이)(아두이노, 라즈베리파이 어디에 둘 것인지)
- 부품, 재료 제안서 작성
- 라즈베리파이 - 아두이노 이슈 찾아보기
- 라즈베리파이 카메라 -> 사진 -> 서버로 보내는 방법 찾아보기
- 사용자 UI 모니터 or lcd or 어플

- 라즈베리파이 모니터 터치 다운로드



#### 11/28 해야 할 일

- 하드웨어 도안 완성
- 라즈베리파이 카메라 -> 사진 -> 서버로 보내는 방법 찾아보기
- tensorflow를 라즈베리파이에 올리는 것 고려 (모델을 라즈베리파이에 올린 다음 병 사진을 모으고 있다가 한 번에 보내기)
- 사용자 UI 모니터 or lcd or 어플
- 라즈베리파이 모니터 터치 다운로드 (ok)
- 라즈베리파이 하나만 쓸 지 아두이노와 라즈베리파이 통신을 할 지



#### 11/30 해야 할 일

- 라즈베리파이와 lcd 모니터 붙이지 않고 선으로 이어지는 지 확인(ok -> 안 된다)

- 툴 찾아서 하드웨어 도안 다듬기(ok)

- 라즈베리파이 웹캠 카메라로 사진 찍는 클래스로 구축(ok)

- 사진 -> 서버로 보내는 코드 짜기

- tensorflow를 라즈베리파이에 올리는 것 고려 (모델을 라즈베리파이에 올린 다음 병 사진을 모으고 있다가 한 번에 보내기)(질문)

  -> 자신이 할 수 있는 방식으로

  -> 일단 하나씩 보내는 걸로 시도해보고 시간이 남으면 tensorflow로

- 라즈베리 하나로 lcd, 모터, 센서 제어 다 할 지, 아니면 아두이노와 라즈베리파이 통신을 할 지(질문)

  -> 시나리오에 따라서 근거리면 ok, 원거리면 아두이노로

- 부품 제안서 수정(ok)

- 사진 크기 64: 256



보통 3차원 배열 가로세로 RGB

4차원 배열을 tensorflow로 입력받는 것

훈련할 때는 한 번에 줘도 되는데.. 

한장을 보내서 결과를 받으면 되는 것인지

사진 한 장이 3차원인데 여러장을 보내면 4차원

훈련할 때는 파일로 훈련을 시키는데... 좀 알아보기



#### 12/01 해야 할 일

- 사진 -> 서버로 올리는 코드 찾고 짜기 (라즈베리파이)(X 필요 없어짐 s3로 바로 ok)

  

![흐름](C:\Users\automata13\Downloads\흐름.PNG)

- 모터 제어 or 센서 제어 코드 짜놓기 + 실험 (아두이노)

- mqtt, socket 서버 구축 (라즈베리파이 브로커, 소켓 보내기 / 아두이노 pub)

- 둘 다 소켓으로 통신? (고민)

- aws iot core 계정 만들어서(ok) 통신 되는 지 확인해보기

- aws iot core를 거치지 않고 s3 bucket로 바로 라즈베리파이 사진을 보내는 방법이 있다고 함 (찾아보기, by python) (ok)

  -> 야매로 os 명령어를 썼는데 규칙에 따라서 이름 달라지도록 수정

  ​																												                             

- 라즈베리파이에 ai 올리는 것 

  -> 모델 파일을 디렉토리에 저장한 다음 함수 부르듯이 (predic) 호출해서 사진 경로?(사진) 넘겨준 후 결과값 도출 -> 제어 + 사진 s3에 저장 



- aws iot core에 보내야 할 정보 (by mqtt)

  -> 분리수거함 상태(초음파센서로 찼는지) (아두이노)

  -> RFID로 얻은 사용자 정보 (아두이노)

  -> AI 돌린 결과 (라즈베리파이)



#### 12/02 해야 할 일

- 야매로 os 명령어를 썼는데 규칙에 따라서 이름 달라지도록 수정

- 음성 녹음 재생하는 것 알아보고 시도해보기(ok)

- iot 전체적 흐름도 그려놓기 (내가 헷갈린다)(ok)

- 모터 제어 or 센서 제어 코드 짜놓기 + 실험 (아두이노)

- aws iot core에 보내야 할 정보 (by mqtt)

  -> 분리수거함 상태(초음파센서로 찼는지) (아두이노)

  -> RFID로 얻은 사용자 정보 (아두이노)

  -> AI 돌린 결과 (라즈베리파이)

- mqtt, socket 서버 구축 (라즈베리파이 브로커, 소켓 보내기 / 아두이노 pub)

  -> 둘 다 소켓으로 통신? (고민)

- aws 계정 certs 갱신, bucket 통일 (cloud와 연동)(오후에 파일 받으면)(ok)

- aws greengrass 찾아보기(할 필요 없을 듯)



#### 12/03 해야 할 일

- 아두이노 - aws 연동 (실패, 결국 수빈님과 돈으로 부품 사서 해결할 예정)



#### 12/04 해야 할 일

- 야매로 os 명령어를 썼는데 규칙에 따라서 이름 달라지도록 수정
- 음성녹음 해놓으면 좋을 듯
- 수행일지 적기(팀원들 진행사항 받으면 다시 수정)
- 멘토님들께 보여드릴 피피티 간단하게 제작
- 아두이노 - aws 연동 (WiFiUtil.h로 바꿔보기)
- ai 모델 돌려보기
- 초음파 없애고 뚜껑 열리는 횟수로 카운트하는 것 생각해보기



#### 12/05 해야 할 일

- 라즈베리파이 rotate(ok) 

- 하드웨어 제작(ok)

- 발표(ok)

- 라즈베리파이 연동(ok) -> Downloads -> 99 ~ -> python predict~~




#### 12/07 해야 할 일

- esp8266 - aws iot core 연동(ok)
- 클래스화
- 모터 제어 코드 짜놓기(ok) -> 90도만 돌아가는 것 맞나? 시킨 서보모터도 90도로만 돌아가는지 확인
- rfid 실험(ok)
- 초음파 센서 실험(ok)
- 라베파 - 아두이노 소켓, mqtt 통신 테스트



#### 12/08 해야 할 일

- 클래스화
- 라베파 - 아두이노 소켓, mqtt 테스트
- 전체적으로 다듬으면서 연동
- 바뀐 점 -> mqtt로 하나하나 보내지 않고 사진 이름으로 날짜, 시간, 사용자id, ai 결과값 보내기
- -> ai와도 상의해봐야 할 듯



#### 12/09 해야 할 일

- 클래스화
- 라베파 -> 아두이노 소켓 통신
- 아두이노 -> 라베파 mqtt (ok)
- 아두이노 -> aws iot core mqtt -> lambda 트리거(ok)
- 전체적으로 다듬으면서 연동
- 바뀐 점 -> mqtt로 하나하나 보내지 않고 사진 이름으로 날짜, 시간, 사용자id, ai 결과값 보내기
- -> ai와도 상의해봐야 할 듯



#### 12/10 해야 할 일

- 클래스화

- 라베파 -> 아두이노 소켓 통신(ok) -> but mqtt가 너무 잘 되어서 소켓 필요 없을듯

- 전체적으로 다듬으면서 연동

  -> 흐름도 보면서 ex) 초음파로 거리 몇이면 mqtt 보내고, 무게 어느정도 이상 감지되면 사진 찍도록 라베파에 mqtt 보내고...




rfid 카드 처음 찍기(mqtt로 정보 보내기) -> 시작 -> 무게 센서에 일정 무게 이상 감지(2초 후) -> 사진 찍기 -> ai 돌리고 결과값에 따라 모터 열고 닫기(반복) -> 사용자 모니터 중지 누르기 or 카드 또 찍기...? -> 버킷에 정보 이름에 넣고 사진 한꺼번에 올리기  



#### 12/11 해야 할 일

- rfid  찍으면 mqtt aws로 보내기
- 종료 버튼 누르면 나는 라베파로 종료했다는 정보(mqtt) 받으면 s3 올리기
- 애로사항 -> esp8266에 hx711.h include시 mqtt 먹통 -> 라이브러리 수정 (ok)
- ppt 수정(ok)
- 라베파 <- aws mqtt 보내기(ok)



음성녹음

rfid 찍 -> 분리수거를 시작합니다 ()

1번 -> 일 번 칸에 투입해주세요~

2번 -> 이 번 칸에 넣어주세요~

3번 -> 삼 번 칸에 넣어주세요~

중지 -> 분리수거를 마칩니다. 적립된 포인트를 확인해주세요 merry christmas~~~

재사용 -> 재사용 병입니다! 

재활용 -> 재활용 유리입니다!

쓰레기 -> 쓰레기!!!입니다 (은서)



wbs  

iot - 센서 소프트웨어 2/3, 하드웨어 설계 2/3, 클라우드 사진 전송 전부, 캠 설치 전부 

cloud -> RDS 반,개발환경구축 전부, 웹인터페이스 1/3, 서비스연동 및 테스트 1/3

빅데이터 -> 수집 데이터 분석 및 예측 1/2, 데이터 추가 수집 완료, 사회현상 및 상품성 데이터 수집 2/3, 웹 인터페이스에 연결



3버전으로!!



#### 12/12 ~ 14 해야 할 일

- 스피커 연동(ok)
- ai 돌려서 결과값 나오도록 -> 새로운 모델로 돌리면 오류 뜸(ok)
- 전체적 흐름으로 가는 거 짜기(ok)
- aws_test랑 mainserver 합치기 (ok)
- 이름 보내는 것 진실이가 보내준 대로 수정(ok)
- 로드셀 테스트해서 전체 소프트웨어 완성(ok)
- 꽉 차는 것 mqtt 보내기 (topic : full, message : 1) -> 일단 12개로 카운트
- 회원가입을 다시 해주십시오(녹음 ok) -> 코드 짜기
- led도 코드 짜두기, 서보모터도
- 로드셀 vin에 꼽아둠



#### 12/15 해야 할 일

- 시작 버튼 누르면 라베파에 신호 받음 -> qr 카메라 키고 -> rfid 번호 다시 aws로 보내기(mqtt)

- rfid 카드 찍으면 aws로 보내기(mqtt), 위와 같은 토픽과 메세지로 하면 될 듯(ok)

- 꽉 차는 것 mqtt 보내기 (topic : full, message : 1) -> 일단 12개로 카운트(ok)

- led, 서보모터 코드 짜두기(ok)

  

#### 12/16 해야 할 일

- 초음파 센서로 코드 짜놓기(ok)
- 하드웨어 전체 연동(ok)
- ai 사진 다시 찍기(ok)
- 안드로이드 회원가입(ok)



#### 12/17 해야 할 일

- RPi -> esp8266 으로 보내는 시작, 종료 관련 topic 봐서 1버전 서브 토픽 바꾸기(취소)

- 서보모터 각도 실험
- 재사용은 11, 3
  재활용은 1, 5, 8, 12, 13
  쓰레기는 0, 2, 4, 6, 7, 9, 10, 14  (ok)
- 하드웨어 수정 : 병 올려놓는 곳에 동그라미 해두기, 병 올려두는 곳 밑에 초음파 구멍 뚫어놓기, 프린트한 것들 붙이기, led 자리 구멍 뚫어놓기
