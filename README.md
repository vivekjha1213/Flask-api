Flask API for User Registration and Authentication

This code provides an API built with Flask that allows users to register and authenticate. It uses MongoDB to store user data and Flask-JWT-Extended to handle authentication.

Dependencies
Flask
Flask-RESTful
Flask-JWT-Extended
pymongo


![Screenshot 2023-05-02 at 12 59 32 PM](https://user-images.githubusercontent.com/67068290/235605901-ffd72cfc-cf07-4520-ad67-2be5e1898942.png)







API Endpoints
/register
Method: POST
Required fields: email, username, password, mobile_no, address, city, message
Returns:
success: "User {username} created"
message: "We will contact you shortly"
/login
Method: POST
Required fields: username, password
Returns:
access_token: JWT access token
Example Usage
Start the Flask server using python app.py
Register a new user by sending a POST request to /register with the required fields in the request body. Example:


POST /register HTTP/1.1
Content-Type: application/json

{
    "email": "test@example.com",
    "username": "testuser",
    "password": "password",
    "mobile_no": "1234567890",
    "address": "1234 Main St",
    "city": "Anytown",
    "message": "Hello, I'm interested in your product"
}
Authenticate the user by sending a POST request to /login with the username and password in the request body. Example:


POST /login HTTP/1.1
Content-Type: application/json

{
    "username": "testuser",
    "password": "password"
}
The API will return a JWT access token that can be used to access protected endpoints. Example:

HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImlhdCI6MTYyMjcyOTU5NCwiZXhwIjoxNjIyNzMzMTk0fQ.MGQnbdm6SDd7QJrC59stR-OVz8-VwGgKeVhZaJ9MX7I"
}

