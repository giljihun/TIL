# DHCP(Danamic Host Configuration Protocol)

<p align='center'><img src = image-22.png width = 500 height = 300></p>

**<p align='center'>'Dynamic Host Configuration Protocol'(동적 호스트 구성 프로토콜)**

## 정의
DHCP란 호스트의 IP주소와 각종 TCP/IP 프로토콜의 기본 설정을 클라이언트에서 자동적으로 제공해주는 프로토콜을 말한다.

쉽게 설명해서, 네트워크 안 컴퓨터에 자동으로 DNS server, IP주소, Default Gateway주소를 할당해주는 것을 의미한다!

해당 **클라이언트에게 일정기간 '임대'를 하는 동적 주소 할당 프로토콜!** 이라고 생각하면 된다!

## 장/단점
**<장점>**

PC의 수가 많거나, PC 자체 변동사항이 많은 경우 IP설정을 자동으로 할 수 있으므로 IP충돌을 막을 수 있다. 새로운 디바이스가 네트워크에 연결되면 DHCP 서버가 자동으로 사용 가능한 IP주소를 할당해주기 때문!!

'네트워크에 연결된 다수의 컴퓨터(PC)가 있거나 PC의 변동사항이 빈번한 환경'은 우리 삶과 아주 밀접하다.
> 1. 가정용 공유기 : DHCP를 사용하여 집 안의 다양한 디바이스에 자동으로 IP 주소를 할당한다. (스마트폰, 노트북, 스마트 TV, 게임 콘솔 등) 
> 2. 오피스 네트워크
> 3. 공공 무선 네트워크(공공 장소, 카페 등)

~~~
요약 : DHCP는 다양한 환경에서 IP 주소 할당을 자동화하고 IP충돌을 방지하는 데 사용된다.
~~~

**<단점>**  

DHCP Server에 의존하기 때문에 서버가 다운되면 모든게 말짱도루묵. 아무것도 못함. IP 할당이 제대로 안됨.

## 프로토콜의 원리

DHCP를 통한 IP 주소 할당은 **"Lease Time"**라는 개념이 있다.

DHCP가 IP를 할당해주는 것은 엄연한 "임대"일 뿐이다.   
명시된 Lease Time 동안만 IP주소를 사용하도록 하는 것이다.

## 임대절차
<p align='center'><img src = image-24.png width = 500 height = 300></p>

**<p align='center'>위 그림이 DHCP의 임대절차(과정)을 한 눈에 표현한 사진인데 설명을 통해 이해해보도록 합시다!!</p>**

> 1) **DHCP Discover : "안녕하세요!!! 혹시 거기 DHCP 서버님 계시면 제게 답 좀 주세요 플리즈."**  
- 메시지 방향 : 단말 ----> DHCP 서버
- DHCP서버를 찾기 위한 메시지를 네트워크 내에 브로드캐스트 방식으로 보낸다. 

> 2) **DHCP Offer : "오잉? 네! 저 여기 있어요. 제 IP는 x.x.x.1 이고요~. 클라이언트님에게 x.x.x.88를 임대해 드릴 수 있답니다 껄껄스."**
- 메시지 방향 : DHCP 서버 ----> 단말
- DHCP서버가 단말이 보낸 메시지에 답변을 주는 것. 해당 패킷의 내부를 보면 아래와 같다.
~~~
- Client MAC : 단말의 MAC 주소
- Subnet Mask (Option 1)
- Rounter (Option 3) : 단말의 Default Gateway IP 주소
- DNS (Option 6) : DNS 서버 IP 주소
- IP Lease Time(Option 51) : 단말이 IP 주소(Your IP)를 사용(임대)할 수 있는 기간(시간)
- DHCP Server Identifier (Option 54) : 본 메시지(DHCP Offer)를 보낸 DHCP 서버의 주소. 2개 이상의 DHCP가 Offer를 보낼 수 있으므로 각 DHCP 서버는 자신의 IP 주소를 본 필드에 넣어서 단말에 보냄!!
~~~
위와 같은 정보를 모아서 패킷에 실어 단말에 보낸다!

> 3) **DHCP Request : "와우!!! 답변 감사합니다. 그럼 x.x.x.1 주소를 가진 DHCP 서버님! 제게 IP 주소를 할당해주시겠습니까???"**
- 메시지 방향 : 단말 ----> DHCP 서버
- 단말은 DHCP 서버(들)의 존재를 인지함! DHCP 서버 중 하나를 선택하여 서버에게 "해당 IP를 사용하겠다!"라고 확인 전달하는 것.

> 4) **DHCP Ack : "Of Course죠. 클라이언트님에게 IP x.x.x.88을 포함한 필요하신 네트워크 정보를 임대해드리겠습니다. Lease Time은 2시간입니다~ 고객님 ^^싱긋."**
- 메시지 방향 : DHCP 서버 ----> 단말
- 마지막 DHCP 절차로, DHCP 서버가 단말에게 "네트워크 정보"를 전달해주는 메시지.

**----> IP adress x.x.x.99 allocation completed.**


[참고자료] https://m.blog.naver.com/yeopil-yoon/221288525875