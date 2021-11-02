
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
  - 회원가입 api spec -> https://www.notion.so/http-127-0-0-1-8000-account-rest-auth-registration-d95dc07309d74f21b4042e577ff5e0cc <br>
  - 로그인 api spec -> https://www.notion.so/http-127-0-0-1-8000-account-rest-auth-login-ae4ad33e94e64e17ae5e4ee8ff4d84ca <br><br>
2. 게시판 글 list 가져오기<br>
  - LimitOffsetPagination 기법을 적용하여 구현하였습니다. pagination 설정으로 웹프레임워크의 setting에서 global 설정하였습니다. <br>
  - 게시판 글 list api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-offset-number-limit-number-db5da45154e24772aaa19ac3945f982d<br><br>
3. 게시판 글 생성<br>
  -django orm 모듈을 이용하여 입력 데이터들을 db 레코드에 저장하였습니다.<br>
  - 게시판 글 생성 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-7bbee4e52ff94b6284142d0d7918f383<br><br>
4. 게시판 글 열람<br>
  - django orm 모듈을 이용하여 해당 pk의 글을 불러와서 직렬화한후 리턴해줍니다.<br>
  - 게시판 글 열람 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-int-pk-92687f3597714ca89357735a76c9bdc9<br><br>
5. 게시판 글 수정
  -django orm 모듈을 이용하여 해당 pk의 db 레코드를 불러와서 수정하였습니다.<br>
  -게시판 글 수정 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-int-pk-5185e5c6548249aab793e06e56445ba0 <br><br>
6. 게시판 글 삭제
   -django orm 모듈을 이용하여 해당 pk의 db 레코드를 삭제하였습니다.<br>
  -게시판 글 삭제 api spec -> https://www.notion.so/http-127-0-0-1-8000-crud-blog-int-pk-5c43798d723742be86438de88239b6d3 <br>
7. 게시판 제목 검색
   -icontain을 이용하여 입력된 값을 제목으로 가직 있는 게시판의 정보를 리턴하여줍니다.
   - 게시글 제목 검색 api spec -> https://www.notion.so/95b94a7f6ff54c5c8b041aae6d02010a?v=ea5ba941fc9c48eb82489412f3d45bc9
