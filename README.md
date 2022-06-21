# __Task__
This Django application is a simple app for the stuff.
1. The project in Docker containers\containers
2. docker-compose to run application
3. User roles - employee, admin
4. Implemented APIs:<br/>
    4.1 Authorization with JWT<br/>
    4.2 Creating a task with a mandatory title, description and optional priority and deadline (for employee)<br/>
      priorities - low, medium, high<br/>
    4.3 Employees can view their tasks only related to them(except admin)<br/>
    4.4 Deleting and editing a task (for the task creator or admin)<br/>
5. If a deadline is running out of time the app will send the notifications in an hour to the email of user

For that you need to configure main mail, I leave the instructions below.

In this project I use Docker for building the project, Postgres as Database, Redis as a message broker, and Celery as a task queue.

---

## __Prepare email (in this case mail.ru)__
[ссылка для настройки почтовой программы](https://help.mail.ru/mail/mailer/popsmtp)


Here you can read configurations. Change the login and password of your mail
If you use gmail.com I want to warn you that from May 30, 2022
Google no longer supports the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password.
Also don't forget to get from mail.ru temporary password

>EMAIL_USE_TLS = False<br/>
>EMAIL_USE_SSL = True<br/>
>EMAIL_HOST = 'smtp.mail.ru'<br/>
>EMAIL_HOST_USER = 'nurzhan.kartaev@mail.ru'<br/>
>EMAIL_HOST_PASSWORD = 'cYkRm3zU0BU4Y7iaH1zc'<br/>
>EMAIL_PORT = 465<br/>

---

### Start the Project

>docker-compose build;<br/>
>docker-compose up;<br/>

