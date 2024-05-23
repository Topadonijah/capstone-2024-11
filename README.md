<div align=center>
  
![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Only%20You&fontSize=90)
  
</div>

<div align = center>

# Github Pages

2024년 국민대학교 캡스톤 11조

[소개페이지](https://kookmin-sw.github.io/capstone-2024-11/)

</div>

<br>

<div align=center>

# 2024 캡스톤 11조 **Only You**

**_사람마다 어울리는 색과 머리스타일이 있다는 사실을 아시나요?_**<br>저희 서비스는 퍼스널 컬러 검출과 얼굴형 검출을 통해 <br>본인에게 맞는 퍼스널 컬러와 헤어스타일을 추천해드립니다.

<br>

# 프로젝트 소개

본인에게 맞는 헤어스타일과 퍼스널 컬러를 찾기위해서는 다양한 헤어스타일을 시도해보고 전문가의 도움을 구하여 퍼스널 컬러를 진단받아야 했습니다. <br>
이러한 과정은 많은 비용과 시간을 요구하기 때문에 접근하기에 어려움이 존재하였습니다. <br>
그렇기 때문에 저희는 이러한 비용과 시간을 줄이고 나에게 맞는 색상과 스타일을 빠르게 알 수 있는 서비스를 제공하는 것을 목표로 하고있습니다.

<br>

# Abstract

To find the right hairstyle and personal color, one typically needed to try various hairstyles and consult professionals for a personal color analysis.
However, this process demanded significant costs and time, making it difficult to access. <br>
Therefore, we aim to provide a service that reduces these costs and time, enabling individuals to quickly discover their personal colors and styles.

<br>

# 프로젝트 구현 개요

:one: cv2와 dlib을 사용하여 이미지속 사람의 얼굴을 인식합니다.<br>
:two: 인식된 얼굴의 81개의 랜드마크 좌표를 활용하여 얼굴의 비율을 구합니다.<br>
:three: 인식된 얼굴에서 피부 부분만을 추출합니다.<br>
:four: 추출한 정보를 벡터화하여 학습데이터를 구축합니다.

<br>

# [:link: 소개 영상 :link:](www.youtube.com)

<br>

# :smile: 팀 소개

### 팀장

### :one: [\*\*\*\*1668 정태성](https://github.com/Topadonijah) <br>

Role: 얼굴형 검출 및 헤어스타일 추천 모델 구현

### 팀원 <br>

### :two: [\*\*\*\*1627 오홍석](https://github.com/lkl4502)

Role: 백엔드 개발, 퍼스널컬러 진단 구현

### :three: [\*\*\*\*1659 전기정](https://github.com/Jeon3625)

Role: 퍼스널컬러 모델 구현

### :four: [\*\*\*\*1660 전병우](https://github.com/wjsquddn)

Role: 프론트엔드 개발, 프론트 디자인
<br>
<br>

# :smile: 기술 스택

### AI

![Pytorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=React&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) <br>
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

### Back-end

![Spring Boot](https://img.shields.io/badge/SpringBoot-6DB33F.svg?style=for-the-badge&logo=React&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

### Front-end

![React](https://img.shields.io/badge/React-61DAFB.svg?style=for-the-badge&logo=React&logoColor=white)
![Styled Components](https://img.shields.io/badge/styled--components-DB7093?style=for-the-badge&logo=styled-components&logoColor=white)
![Axios](https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=Axios&logoColor=white)


<br>

# :video_game: 사용법

> level 1
>
> > level 2
> >
> > > level 3<br> 여기에 쓰면 됩니다.

</div>

---

### Commit Convention

1. `feat`: **새로운 기능 추가**
2. `fix`: **버그 수정**
3. `docs`: **문서 수정**
4. `style`: **코드 포맷팅 → Code Convention**
5. `refactor`: **코드 리팩토링**
6. `test`: **테스트 코드**
7. `chore`: **빌드 업무 수정, 패키지 매니저 수정**
8. `comment`: **주석 추가 및 수정**

### Branch Naming Convention

브랜치를 새롭게 만들 때, 브랜치 이름은 항상 위 `Commit Convention`의 Header와 함께 작성되어야 합니다.

### 예시

> `feat/On_you`  
> `refactor/On_you`
