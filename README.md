## final pjt

## 상세 정보

1. 팀원 정보 및 업무 분담 내역 팀원: 유태규, 정유진 업무 분담 내역: 공통: 구현할 기능 및 api end points 설정 유태규: backend api 서버 구축 정유진: frontend 서버 구축
2. 목표 서비스 구현 및 실제 구현 정도
   -  목표 서비스: 
     - 필수: 영화 추천 기능, 커뮤니티 기능(댓글, 리뷰), 평점(0~5) 
     - 추가기능: 영화 검색어 자동완성, 닉네임 정해주기, 광고 기능, 영화 스케쥴러 
   - 실제 구현 정도: 
     - 필수:   
       - 영화 추천 기능(O)
       - 커뮤니티 기능(O)
       - 평점(O) 
     - 추가기능:  
       -  영화 검색어 자동완성 
       -  닉네임 정해주기 
       -  광고 기능(X: 사용한 static파일들의 source가 무료인지 아닌지 알 수가 없었으므로 광고는 달지 않았다)
       -   영화 스케쥴러
3. 데이터베이스 모델링(ERD)![img](https://lh3.googleusercontent.com/RPeD0nf82SzK4b_Mu51pXgKTheg4ynFcvpCP3EvPavjIO2KUNiZR9g6tny6KSzuDzz_--lcrN7UkbaccHsqbE8NfbRk-OG5njf_ZvtzKA2b8iRr-eK3_JgfvmZhrkwL4akzwqPJD)![img](https://lh5.googleusercontent.com/JTtmpERNgzXcgLs0-zn9SwmV18RG0JAzu_GxgSjLWPQv1W2f7V3LVLCE8_WvxWroBGGqEuWM_XRo1GG7CnfWvpNjW4tGdIuveOcGECtuOBItplOZviJwaBwSBudbN1eeOBlBAX3R)
4. 필수 기능에 대한 설명 추천 기능: 
   - 처음 회원가입시에 몇 개의 영화에 대해 평점을 매길 수 있도록 하고,
   - 이를 바탕으로 선호하는 영화 시리즈를 결정, 이 영화 시리즈에 해당하는 영화중 평점을 주지 않은 영화들을 보지 않은 영화라고 간주하여 추천
   - 익명 닉네임 설정 기능: 선호하는 영화 시리즈가 결정되면, 그 시리즈에 해당하는 캐릭터를 결정할 수 있는 질문을 사용자에게 제시. 그 답변 결과 정해진 캐릭터와 무작위 형용사를 조합하여 유저 닉네임 결정.
   - 영화 스케쥴러: 영화에 후속작 관계를 이용하여 영화 관람 순서를 사전에 어느정도 정해둠. 실제로 영화를 볼려고 보는 시간에 대한 정보를 입력하면, 이 조건에 맞는 영화들을 그 시간에 맞게 배치하여 사용자에게 제시
5. 배포 서버 URL
   - 백엔드 서버 : http://ec2-3-21-154-255.us-east-2.compute.amazonaws.com/
6. 기타(느낀점)

## 진행

- 5/20 
  - 직접 만나서 공통에 해당하는 부분 작성
  - 가장 크게 구현하고자 하는 기능을 결정
  - erd 작성
  - 이후 필요한 api ends point를 협의
  - front의 전체적인 조형을 결정하는 테마를 결정
  - 기초적인 데이터 틀 및 수집
- 5/21
  - 구체적인 데이터 수집
  - 개발 시작
  - erd에 기반한 모델 구축
  - movies app의 fixture 생성
  - rest_framework, rest_framwork_jwt, all_aut, rest_framework_auth를 이용한 로그인 구현
- 5/22
  - movies app에 관련된 기능 구현
  - community app에 관련된 기능 구현
- 5/23
  - accounts app에 관련된 기능 구현
- 5/24
  - accounts app에 관련된 기능 중 못 다한 것들 마저 구현
  - 프론트와의 협의를 통해 변경된 점들 반영
  - db에 채울 데이터 생성
- 5/25
  - db에 채울 데이터 마무리
  - 최종 fixture 생성
  - 배포