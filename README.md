# fun-with-orm
Demostration for arbitrary attribute assignment for objects

```
.
├── docker-compose.yaml
├── README.md
└── webapp
    ├── app.py
    ├── database.py
    ├── Dockerfile
    ├── models.py
    ├── requirements.txt
    └── test_user_assignments.py
```

`app.py` creates a flask app with routes to test user model creation and update.

### Routes

```
GET /api/v1/users/
```
Returns all users in JSON format.

#### Creating new user:

```
POST /api/v1/create/
```

Form data:

| Field          | Description                                                       | Optional   |
| -------------- | ----------------------------------------------------------------- | ---------- |
| `email`        | User email, primary key                         | no        |
| `first_name`         | First name of the user                                      | yes        |
| `last_name`         | Last name of the user                                      | yes        |


#### Updating user properties:

```
PATCH /api/v1/update/
```

Form data:

| Field          | Description                                                       | Optional   |
| -------------- | ----------------------------------------------------------------- | ---------- |
| `email`        | User email, primary key                         | no        |
| `first_name`         | First name of the user                                      | yes        |
| `last_name`         | Last name of the user                                      | yes        |


Both methods are designed to work with arbitrary fields. However, currently `email`, `first_name` and `last_name` are the only editable properties of the `User` model. Any other value passed that's not a property of the `User` method will be ignored.

### Running and testing locally

```
docker-compose up --build
```

The above command will build and run the `web` service defined by the Dockerfile in `./webapp` folder. A local folder inside the container will be used to keep sqlite data.

To obtain container's ip address use the command `docker inspect <containerNameOrId> | grep '"IPAddress"'`.
Something like;
>docker inspect funwithorm_web_1 | grep '"IPAddress"'

### Running tests
```
docker-compose run web python -m unittest discover -v
```

#### Example: creating a user
```
curl -d '{"first_name":"kerem", "email":"kerem@email.com"}' -H "Content-Type: application/json" -X POST http://172.18.0.2:5000/api/v1/create
```

```
{
  "created_at": "Wed, 29 May 2019 18:50:43 GMT", 
  "deleted_at": null, 
  "email": "kerem@email.com", 
  "first_name": "kerem", 
  "last_name": null, 
  "updated_at": "Wed, 29 May 2019 18:50:43 GMT"
}
```

#### Example: updating existing user
```
curl -d '{"first_name":"not kerem", "email":"kerem@email.com"}' -H "Content-Type: application/json" -X PATCH http://172.18.0.2:5000/api/v1/update
```

```
{
  "created_at": "Wed, 29 May 2019 18:50:43 GMT", 
  "deleted_at": null, 
  "email": "kerem@email.com", 
  "first_name": "not kerem", 
  "last_name": null, 
  "updated_at": "Wed, 29 May 2019 18:51:39 GMT"
}
```
