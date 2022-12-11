

## CRUD API using Concrete View Classes
Concrete views do most of the work that we need to do on our own when using APIView. They use mixins as their basic building blocks, combine the building blocks with GenericAPIView, and bind actions to the methods.

The view classes can be imported from rest_framework.generics.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView , ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


<br/>

# Requirements

Last tested successfully with Python 3.6.19 and Ubuntu 16.04
Django==3.1.1\
djangorestframework==3.12.4


[Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).

[DRF](https://github.com/gitgik/django-rest-api/blob/master/www.django-rest-framework.org): A powerful and flexible toolkit for building Web APIs


<br/>

# Quick Setup

1. Create a folder for your project on your local machine
```bash
  mkdir myproject; 
  cd myproject
```

2. Create a virtual environment and install django

```bash
  virtualenv venv --python=python3 ; 
  source venv/bin/activate; 
```

3.  Install the dependencies needed to run the app:
```bash
  pip install -r requirements. txt 
```

4. Download this project template from GitHub
```bash
  git clone https://github.com/parshurampatil197/CRUD_API_Using_Concrete_View_Classes.git
  cd CRUD_API_Using_Concrete_View_Classes
```

5. Initialize the database
```bash
  python manage.py makemigrations
  python manage.py migrate
```

6. Run the project
```bash
  python manage.py runserver
```

<br/>

# API Reference
 
Test API by Using POSTMAN
#### Http request: POST 

```http
  http://127.0.0.1:8000/api/
```

#### Request

```http
 {
    "name" : "Parshuram",
    "roll" : 101,
    "city": "Pune",
    
}
```
#### Http request: GET 

```http
  http://127.0.0.1:8000/api/
```

```http
  http://127.0.0.1:8000/api/1
```


#### Response

```http
{
    "name" : "Parshuram",
    "roll" : 101,
    "city": "Pune",
    
}
```

#### Http request: PUT 

```http
  http://127.0.0.1:8000/api/1
```

#### Http request: DELETE 

```http
  http://127.0.0.1:8000/api/1
```



## Authors

- [@parshuram](https://github.com/parshurampatil197)

