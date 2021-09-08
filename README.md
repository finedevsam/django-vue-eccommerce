# ecommerce


baseUrl = http://127.0.0.1:8000

# Authentications

Request Method = POST

Endpoint = baseUrl/store/token/login/

Body:

{
    "username": "admin",
    "password": "12345"
}

Response

{
    "auth_token": "550e8041485f631e25f47886895e82e7e93442ce"
}


# Create User

Request Method = POST

Endpoint = baseUrl/store/create_user/

header: 
Content-Type: application/json
Authorization: Token {auth_token}

Body:

{
    "username": "",
    "fullname": "",
    "email": "",
    "password": "",
    "confirm_password": "",
    "isAdmin": True
}

Response

{
    "code": 200,
    "status": "successful",
    "message": "USer Created"
}



# Create Product

Request Method = POST

Endpoint = baseUrl/store/create_product/

header: 
Content-Type: application/json
Authorization: Token {auth_token}

Body:

{
    "productTitle": "",
    "productDesc": "",
    "productCategory": "",
    "price": "",
    "quantity": ""
}

Response

{
    "code": 200,
    "status": "successful",
    "message": "Product Created"
}


# Delete Product

Request Method = DELETE

Endpoint = baseUrl/store/delete_product/{productId}

header: 
Content-Type: application/json
Authorization: Token {auth_token}


Response

{
    "code": 200,
    "status": "successful",
    "message": "Product Deleted"
}



# Update Product

Request Method = PUT

Endpoint = baseUrl/store/update_product/{productId}

header: 
Content-Type: application/json
Authorization: Token {auth_token}

Body:

{
    "productTitle": "",
    "productDesc": "",
    "productCategory": "",
    "price": "",
    "quantity": ""
}

Response

{
    "code": 200,
    "status": "successful",
    "message": "Product Updated"
}


# Create Category

Request Method = POST

Endpoint = baseUrl/store/create_category/

header: 
Content-Type: application/json
Authorization: Token {auth_token}

Body:

{
    "name": ""
}

Response

{
    "code": 200,
    "status": "successful",
    "message": "Category Created"
}


# All Categories

Request Method = GET

Endpoint = baseUrl/store/all_category/

header: 
Content-Type: application/json
Authorization: Token {auth_token}


Response

[
    {
        "id": 1,
        "name": "Cloth"
    }
]


# All Product

Request Method = GET

Endpoint = baseUrl/store/allproduct/

header: 
Content-Type: application/json
Authorization: Token {auth_token}


Response

[
    {
        "id": 1,
        "productTitle": "Good Cloth",
        "productDesc": "Test",
        "productCategory": "1",
        "price": "200",
        "quantity": "10"
    }
]


# Product By ID

Request Method = GET

Endpoint = baseUrl/store/allproduct/

header: 
Content-Type: application/json
Authorization: Token {auth_token}


Response

[
    {
        "id": 1,
        "productTitle": "Good Cloth",
        "productDesc": "Test",
        "productCategory": "1",
        "price": "200",
        "quantity": "10"
    }
]