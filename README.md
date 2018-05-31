# openinfradays-2018

## 싷행 환경
* python : 3.6.x


## 실행 방법
### 1. virtualenv 생성
```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

### 2. 의존 패키지 설치
```bash
$ pip3 install -r requirements.txt
```


### 3. DB 초기화
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 4. 관리자 생성
```bash
$ python manage.py createsuperuser
```

### 5. 메시지 파일 생성 / 컴파일
```bash
$ python manage.py makemessages
$ python manage.py compilemessages
```

### 6. static files 생성
```bash
$ python manage.py collectstatics
```