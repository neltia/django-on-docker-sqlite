# Dockerizing Django with SQLite3, Gunicorn, and Nginx

## Want to learn how to build this?
블로그 포스팅 작성 예정
[post](https://blog.naver.com/dsz08082).


## Want to use this project?
### Dev Env
- Infra: AWS EC2 + Docker
- Front: Bootstrap ver. 5.2 (python lib: django-bootstrap5 ver. 23.1)
- Back : Django ver. 4.2
- DB   : SQLite3
- WSGI : gunicorn 20.1.0
- WebServer: Nginx

### Precautions
1. 다음 파일을 적절히 수정 후 이름에서 -sample을 제거해 사용할 것.
- /app/.config_secret/settings_common-sample
- /app/.config_secret/settings_deploy-sample

2. 장고 배포를 위한 기본적인 틀 구성으로 돼 있으며, 적절히 코드 내용을 변경해 사용할 것.

3. 실제 배포 환경에서는 SQLite3가 아닌 PostgreSQL DB 권장

### Deploy Test
Uses gunicorn + nginx. Build the images and run the containers:
- 최초 빌드 or 수항사항 반영 실행
```
$ docker-compose -f docker-compose.yml up -d --build
```

- 기존 이미지 기반 실행
```
$ docker-compose -f docker-compose.yml up -d
```

- 서비스 중지
```
$ docker-compose -f docker-compose.yml down
```
