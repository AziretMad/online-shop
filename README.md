# Test task from Sunrise IT company

[Description of test task](https://docs.google.com/document/d/1RS_pdW3k7wOn_bQbN1kqYHEXLR8quhU8mOP37gZZqf0/edit)

The service uses the following technologies:

- `Python 3.8`
- `Django 3.1`
- `Huey (task queue)`
- `PostgreSQL 12.4`
- `Redis 6.2.1`
- `Docker`

## How to run development environment
##### Download and install postgres version 12.4
link to download - https://www.postgresql.org/download/

```sh
$ sudo -u postgres createdb online_shop # creating a database with name online_shop.
```

```sh
$ git clone https://github.com/AziretMad/online-shop.git && cd online_shop
$ cp .env.example .env # or see environment variables below.
$ export $(cat .env | xargs) # to activate environment variables
$ mkvirtualenv shop_env
$ pip install -r requirements.txt
$ python manage.py migrate # add migration into database.
$ python manage.py runserver # run backend.
```

## How to run production environment via docker

Use `docker-compose up --build -d` for pull images and start

---

### Environment variables

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | Django secret key  | vj0q*s86^y+%8&nbp05_722*vv84%2r8g3m22_y$w*0&y6w)%)              |
| `DATABASE_URL`  | Database url for connection with a backend | postgres://online_shop:online_shop@127.0.0.1:5432/online_shop |
| `DEBUG`  | Debug mode displays of detailed error pages | True |
| `EMAIL_HOST`  | Email host | smtp.gmail.com |
| `EMAIL_HOST_USER`  | Email host user | youremail@gmail.com |
| `EMAIL_HOST_PASSWORD`  | Email host password | yourpassword |
| `EMAIL_PORT`  | Email port | 587 |
| `REDIS_URL`  | Redis url | redis://redis:6379/0 |

