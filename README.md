# 치킨어때 🍗
나만 먹기 아까운 치킨들을 남들에게 추천하고 싶은 적 있지 않나요? 혹은 어떤 치킨을 먹을지 메뉴판을 보며 고민한 적 있지 않나요?

__치킨어때__ 는 나만 먹기 아까운 맛있는 치킨들을 공유하고 리뷰를 남기면서 치킨을 고를 때 참고할 수 있게 서로의 의견을 공유하는 플랫폼입니다.

---------------------------------------

#### 목차
* 사용 기술
* 팀원 목록
* 프로젝트 소개
  * 와이어 프레임
  * 프로젝트 결과 
* 문제 해결 방법


## 사용 기술

* **회원가입** : 중복확인 및 정규식 확인하여 회원가입
* **로그인/로그아웃** : JWT 토큰방식을 이용하여 로그인 및 토큰 미발급 상태 시 메인페이지, 상세페이지 이동 불가 설정
* **카드 출력** : 해당하는 카드 클릭시 상세페이지 이동
* **카드 검색** : 검색 시 해당하는 치킨으로 스크롤바 이동 및 항이라이트 표시
* **좋아요** : 게시글당 한번씩 추천 가능, 한번 더 누르면 취소
* **리뷰작성** : 로그인한 사용자에 한해 별점 (1~5)추가 및 댓글 장석 가능
* **리뷰삭제** : 게시글의 ⓧ버튼을 누르면 리뷰 삭제

## 팀원 목록
* 천두인
* 조현준
* 이주영
* 신동석




## 프로젝트 소개
* 와이어 프레임

##### 로그인 화면
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmZBTV%2FbtrqobWjeRN%2F5gQ4HBfkVtLwUMiAzrwHuk%2Fimg.png" width="50%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
##### 회원가입 화면
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbvt2GB%2FbtrqmM3MyVl%2FOGIVG0TzR4rKjIx0N4Q9MK%2Fimg.png" width="50%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
##### 메인 화면
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbN8G6u%2FbtrqoaJRUXK%2FLbYrEIhu3ICXtqvR9KxowK%2Fimg.png" width="50%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
##### 세부 화면
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcu4N5U%2FbtrqdUhJP5z%2Fn0CTvWtu8Q3OTBpMYVMpAk%2Fimg.png" width="50%" height="50%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>

* 프로젝트 결과

이미지
이미지
이미지
이미지


## 문제해결 방법

* 로그아웃 시 로그인 페이지 이동 오류
```
메인페이지와 상세페이지 모두 동일하게 token 인증이 될 경우에만 접근 가능하도록 설정한 뒤, 로그아웃 버튼 클릭 시
token이 삭제되는 함수를 추가하여 해결
```

* 상세페이지별 포스팅 기능 구현 오류
```
특정 치킨 클릭시, url/<keyword> 서버에서 keyword를 'detail.html'파일로 보냄, 저장된 리뷰데이터를 받을 때,
keyword에 부합하는 리뷰만 ajax로 받아옴, 이후 해당 치킨 페이지 전용의 댓글이 나오는 기능 구현 해결
```
