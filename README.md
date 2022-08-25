# 🧑‍💻 Partner Map
http://wumusill.pythonanywhere.com/
## ✅ Description
> 소속집단에서 받을 수 있는 다양한 혜택 <br>
> 하지만 알아보기 귀찮아서 그냥 안받고 마는 상황에서 출발했습니다. <br>
> Partner Map은 충북대학교 제휴 정보를 제공합니다.

<br>


### 🦁 멋쟁이 사자처럼 대학 10기 : 22.03.22 ~ 22.08.20
### ⏱ 프로젝트 기간 : 22.06.26 ~ 22.08.20

<br>

## ✅ 서비스 핵심 기능
### 1. 제휴 업체 출력
> 제휴 업체의 위치를 지도에 마커로 찍어줍니다. <br>
> 제휴 내용, 전화번호와 같은 부가정보를 표로 만들어 보여줍니다. 
### 2. 좋아요 기능
> 사용자가 제휴 내용에 대한 선호도를 표현할 수 있습니다. <br>
> 사용자들이 어떤 제휴를 좋아하는지 좋아요 순위를 출력해줍니다.
### 3. 친구 찾기 게시판 
> 인원을 모집할 수 있는 게시판입니다. <br>
> 학원 단체 등록과 같이 여러 인원이 요구되는 제휴를 이용하기 위함입니다.

<br>

## 🛠 개발 도구
<img alt="Html" src ="https://img.shields.io/badge/HTML5-E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=white"/> <img alt="Css" src ="https://img.shields.io/badge/CSS-1572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=white"/>
<img src="https://img.shields.io/badge/django-006643?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/mariaDB-003545?style=for-the-badge&logo=mariaDB&logoColor=white">

<br>

## 📁 Foldering
```
📁 partnermap
        ├── accounts
        │   ├── templates
        │   │   ├── differ_pwd.html
        │   │   ├── join.html
        │   │   ├── join_nothing.html
        │   │   ├── login.html
        │   │   └── login_error.html
        │   └── views.py
        ├── intro
        │   ├── models.py
        │   ├── templates
        │   │   ├── business.html
        │   │   ├── doctor.html
        │   │   ├── elec.html
        │   │   ├── engine.html
        │   │   ├── farm.html
        │   │   ├── humanity.html
        │   │   ├── intro.html
        │   │   ├── life.html
        │   │   ├── medicine.html
        │   │   ├── mixed.html
        │   │   ├── science.html
        │   │   ├── society.html
        │   │   ├── teacher.html
        │   │   └── vet.html
        │   ├── urls.py
        │   └── views.py
        ├── like
        │   ├── models.py
        │   ├── urls.py
        │   └── views.py
        ├── manage.py
        ├── partnerapp
        │   ├── forms.py
        │   ├── models.py
        │   ├── templates
        │   │   ├── board.html
        │   │   ├── detail.html
        │   │   ├── home.html
        │   │   ├── post_form.html
        │   │   └── preference.html
        │   └── views.py
        ├── partnermap
        │   ├── asgi.py
        │   ├── my_settings.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── static
        │   ├── css
        │   │   └── partnermap.css
        │   ├── img
        │   │   ├── google.png
        │   │   ├── hhg.jpeg
        │   │   ├── ksy.jpeg
        │   │   ├── lra.JPG
        │   │   ├── people.jpg
        │   │   ├── picture1.jpg
        ─────────────────────────────────────────────
```