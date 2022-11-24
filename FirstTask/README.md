# Database Schema

- I have used 2 tables for this project:

## User

- Represents a registered user
- Main fields -
  - `email`
  - `mobile`,
  - `first_name` (optional),
  - `last_name` (optional),
  - `password`.

## Customer

- Represents a customer.
- Fields -
  - `user`(Foreign key with user table),
  - `profile_number`.

# Steps to setup project:

- Install all dependencies using `pip install -r requirements.txt`
- Create all the tables using `python manage.py migrate`.
- create superuser using `python manage.py createsuperuser`
- Start the project using `python manage.py runserver`

### Create Customer

- Url: `http://localhost:8000/customer` (POST)
- Sample request:

```json
{
  "email": "puneetgarg@gmail.com",
  "mobile": "9999999999",
  "password": "User@123",
  "profile_number": "abc",
  "first_name": "Puneet",
  "last_name": "Garg"
}
```

#### First name and Last Name can be left blank
