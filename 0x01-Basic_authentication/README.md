# Simple API

Simple HTTP API for playing with `User` model.

## Background Context

In this project, you will learn what the authentication process means and implement a **Basic Authentication** on a simple API.

In the industry, you should **not** implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://intranet.alxswe.com/rltoken/rpsPy0M3_FJuCLGNPUbmvg "Flask-HTTPAuth")). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/5/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240603%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240603T114114Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ec08464c4f46f2bc78a6c40596e82fe12ac9f85fa428ba339b71051dd692f117)

## Resources

**Read or watch**:

- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY "REST API Authentication Mechanisms")
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html "Base64 in Python")
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization "HTTP header Authorization")
- [Flask](https://palletsprojects.com/p/flask/ "Flask")
- [Base64 - concept](https://palletsprojects.com/p/flask/ "Base64 - concept")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/swiIZazfz7mspY1vjuy_Zg "explain to anyone"), **without the help of Google**:

### General

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

## Setup

```
$ pip3 install -r requirements.txt
```

## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

---
