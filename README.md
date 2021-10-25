# Address Book Api
Address Book api developed in django using rest framework library.

## Setup Instructions:

### Clone repository:

```console
$ git clone https://github.com/kenvac/qogita-address-book-api
```

### Install library and dependency requirements:

```console
$ pip install -r requirements.txt
```

### Set up DB:

```console
$ python manage.py makemigrations
$ python manage.py migrate
```

### Run the app:

```bash
$ python manage.py runserver
```

### Create users:
Use the following commands to create super users in the system
```bash
$ python manage.py createsuperuser --username=example1 --email=example1@example.com
```

## API Usage:
### Login
User needs to login to perform any kind of requests. The login use email and
password fields of user.

#### HTTP request
```bash
POST http://{url}/api/login
```

#### Request headers
| Header | Value |
|--------|-------|
| Content-Type | application/json |

#### Request body
In the request body, supply a JSON representation of an items object.

#### Response
If successful,  this method returns 200 ok response code and an items object in the response body

#### Example
Request
Here is an example of a request
```json
POST http://{url}/api/login
Content-type: application/json

{
"auth_token": "ff2fff6508a17423f6320a824d3c795dabba6271"
}
```

### Logout
Any current session will expire and client will require to login to perform any new requests.

#### HTTP request
```bash
POST http://{url}/api/logout
```

#### Request headers
| Header | Value |
|--------|-------|
| Authorization | Token {token_value} |
| Content-Type | application/json |

#### Request body
In the request body, supply a JSON representation of an items object.

#### Response
If successful,  this method returns 204 No Content response code

#### Example
Request
Here is an example of a request
```json
POST http://{url}/api/logout
Content-type: application/json

{}
```

### Create Address
Create an address using api.
Note: Duplicate address with same name, street and zip are not allowed

#### HTTP request
```bash
POST http://{url}/api/addressbook
```

#### Request headers
| Header | Value |
|--------|-------|
| Authorization | Token {token_value} |
| Content-Type | application/json |

#### Request body
In the request body, supply a JSON representation of an items object.

#### Response
If successful, this method returns 201 Created response code and returns the
item  in the response body

#### Example
##### Request
Here is an example of a request.
```json
POST http://{url}/api/addressbook
Content-type: application/json

{
  "name": "Home",
  "street": "6 Cannon",
  "street2": "street2",
  "zip": "380061",
  "country": "GB"
}
```

##### Response
Here is an example of the response.
```json
{
    "status": "success",
    "data": {
    "id": 7,
    "street2": "street2",
    "city": "",
    "state": "",
    "country": {
        "code": "GB",
        "name": "United Kingdom"
    },
    "phone_number": "",
    "email": "",
    "name": "Home",
    "street": "6 Cannon",
    "zip": "380061",
    "owner": 1
    }
}
```

### Get Address
Fetch addresses api

#### HTTP request
Get all addresses from database

```bash
GET http://{url}/api/addressbook
```

Get an address with database id

```bash
GET http://{url}/api/addressbook/{id}
```

Filter address using zip code
```bash
GET http://{url}/api/addressbook?zip={value}
```

#### Request headers
| Header | Value |
|--------|-------|
| Authorization | Token {token_value} |
| Content-Type | application/json |

#### Request body
In the request body, supply a JSON representation of an items object.

#### Response
If successful, this method returns 200 OK response code and returns the
item  in the response body

#### Example
##### Request
Here is an example of a request.
```json
GET http://{url}/api/addressbook/{id}
Content-type: application/json
```

##### Response
Here is an example of the response.
```json
{
    "status": "success",
    "data": {
    "id": 7,
    "street2": "street2",
    "city": "",
    "state": "",
    "country": {
        "code": "GB",
        "name": "United Kingdom"
    },
    "phone_number": "",
    "email": "",
    "name": "Home",
    "street": "6 Cannon",
    "zip": "380061",
    "owner": 1
    }
}
```

### Update Address
Update an address api

#### HTTP request

```bash
PATCH http://{url}/api/addressbook/{id}
```

#### Request headers
| Header | Value |
|--------|-------|
| Authorization | Token {token_value} |
| Content-Type | application/json |

#### Request body
In the request body, supply a JSON representation of an items object.

#### Response
If successful, this method returns 200 OK response code and returns the
item  in the response body

#### Example
##### Request
Here is an example of a request.
```json
PATCH http://{url}/api/addressbook/{id}
Content-type: application/json

{
  "city": "Rugby",
  "phone_number": "1234567"
}
```

##### Response
Here is an example of the response.
```json
{
    "status": "success",
    "data": {
    "id": 6,
    "street2": "street2street",
    "city": "Rugby",
    "state": "",
    "country": {
        "code": "GB",
        "name": "United Kingdom"
    },
    "phone_number": "1234567",
    "email": "",
    "name": "Kinner",
    "street": "street1",
    "zip": "380061",
    "owner": 1
    }
}
```

### Delete Address
Delete addresses api

#### HTTP request
Delete single record using id
```bash
DELETE http://{url}/api/addressbook/{id}
```

Batch delete addresses
```bash
POST http://{url}/api/addressbook/batchdelete

{
  "ids": {list_ids}
}
```

#### Request headers
| Header | Value |
|--------|-------|
| Authorization | Token {token_value} |
| Content-Type | application/json |

#### Request body
In the request body, supply a JSON representation of an items object.

#### Response
If successful, this method returns 200 OK response code and returns the
item  in the response body

#### Example
##### Batchdelete
##### Request
Here is an example of a request.
```json
POST http://{url}/api/addressbook/batchdelete
Content-type: application/json

{
  "ids": [7,8]
}
```

###### Response
Here is an example of the response.
```json
{
    "status": "success",
    "reason": "Addresses Deleted",
    "data": {
    "ids": [7,8],
    }
}
```

##### Record delete
##### Request
Here is an example of a request.
```json
DELETE http://{url}/api/addressbook/{id}
Content-type: application/json

```

###### Response
Here is an example of the response.
```json
{
    "status": "success",
    "data": "Address Deleted"
}
```
