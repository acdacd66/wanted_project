<h1>에이모X원티드 기업협업 프로젝트</h1>

## 참가인원
- 성우진
- 이정우


<h1>장고 프로젝트 초기 설정</h1>
1.프로젝트 폴더인 mySite 폴더랑 같은 위치에 가상 환경을 먼저 만든다 <br>
  -mySite 안에 "mySite"라는 같은 이름의 폴더가 존재하지만 본 문서에서 말하는 프로젝트 폴더는 제일 밖의 mySite폴더다. <br>
  -> python -m venv "가상환경"  <br>
2.가상환경이 있는 위치에서 가상 환경을 킨다.<br>
  -> source "가상환경"/bin/activate(mac 일 경우)<br>
  -> source "가상환경"/scripts/activate(mac이 아닐 경우)<br>
3.프로젝트 폴더(mySite)로 들어가서 requirement file의 모듈들을 다운 받는다.<br>
  ->pip install -r requirement.txt<br>
4.프로젝트 폴더(mySite)안에서 migration을 진행해준다.<br>
  4.1.<br>
    -> python manage.py makemigrations<br>
  4.2.<br>
    ->python manage.py migrate<br>
5. 해당 장고 서버를 실행 시킨다.<br>
  ->python manage.py runserver<br>
  
<h1> api 설명</h1>
1.회원 가입,로그인<br>
  - django에서 자체적으로 jwt 토큰을 이용하요 유저 생성, 인가,인증을 해주는 라이브러리(django-allauth,django-rest-auth)를 사용하여 구현하였습니다. <br>
  라이브러리를 사용하지 않고 자체적으로 구현하지 않은 이유는 인가,인증을 완벽히 검증하기엔 개인으로선 한계가 있기에 이미 공인 검증된 라이브러리를 쓰게 되었습니다. <br>
  - 회원가입 api spec -> https://www.notion.so/http-127-0-0-1-8000-account-rest-auth-registration-84abb6d2b1c348ffbfdf57acc73b1d0b <br>
  - 로그인 api spec -> https://www.notion.so/http-127-0-0-1-8000-account-rest-auth-login-f037552f76f34d6e83a1683a14ef05ad <br><br>
2. 게시판 글 list 가져오기<br>
  - LimitOffsetPagination 기법을 적용하여 구현하였습니다. pagination 설정으로 웹프레임워크의 setting에서 global 설정하였습니다. <br>
  - 게시판 글 list api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-offset-number-limit-number-d0d51ad9a197451db5d54f024880e7c9 <br><br>
3. 게시판 글 생성<br>
  -django orm 모듈을 이용하여 입력 데이터들을 db 레코드에 저장하였습니다.<br>
  - 게시판 글 생성 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-981b6d06e539449c83cb3291e839e43a <br><br>
4. 게시판 글 열람<br>
  - django orm 모듈을 이용하여 해당 pk의 글을 불러와서 직렬화한후 리턴해줍니다.<br>
  - 게시판 글 열람 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-offset-number-limit-number-d0d51ad9a197451db5d54f024880e7c9 <br><br>
5. 게시판 글 수정
  -django orm 모듈을 이용하여 해당 pk의 db 레코드를 불러와서 수정하였습니다.<br>
  -게시판 글 수정 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-int-pk-e6a1bbdb238a474d92d295161a4b83e8 <br><br>
6. 게시판 글 삭제
   -django orm 모듈을 이용하여 해당 pk의 db 레코드를 삭제하였습니다.<br>
  -게시판 글 삭제 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-int-pk-2cb7dca59c5147a1b68052b34e1a6051 <br><br>
7. 게시판 제목 검색
   -icontain을 이용하여 입력된 값을 제목으로 가직 있는 게시판의 정보를 리턴하여줍니다. <br>
   - 게시글 제목 검색 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-search-search-4-e14be12d82174ee2acd594c957942272 <br><br>
8. 댓글 생성/조회 및 대댓글 생성/조회
  - 댓글 생성 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-comment-ecedd0c573924e43941466ceb3c49852 <br>
  - 댓글 조회 api sepc -> https://www.notion.so/http-127-0-0-1-8000-crud-comment-board_id-int-pk-c03f7904cf3445a5a60f8926911639f0 <br>
  - 대댓글 생성 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-Nestedcomment-62458797262e46e39cf89c9e8e60df2c <br>
  - 대댓글 조회 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-Nestedcomment-comment_id-int-pk-d97dc9e85d4a4e75b7a58b4945d2051a <br>

<h1> 배포 서버 주소</h1>
-> http://ec2-13-209-12-175.ap-northeast-2.compute.amazonaws.com:8080/
