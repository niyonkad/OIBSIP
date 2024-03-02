#................................. LEARNING API PYTHON................................

#API (Application Programming Interface) : it's a way of communicating between one or more servers through the program.
#It is a gateway of connection between the server and the client.
#The authentication of API is done through the "API key".

#----------------------------------API METHODS-------------------------------
        # GET: To request data from the API.
        # POST: To send data to the API.
        # PUT: To change the state of the server.
        # DELETE: To remove data from the server.


#API responses are always in the format called JSON.
#JSON (Javascript Object Notation) can be manipulated just like a dictionary in Python.


#In Python, we have to <import> an external library in order to be able to connect to an API server.
#The library we use is called "requests".

#To retrieve some information from an API server, we use <.get()> method:
        # the .get() method takes a parameter of the URL and the API Key. Sometimes the key is not unnecessary.

#We use .post() method to send some data to the API server:
        # It requires 2 arguments: URL, Headers and Data.
        # The principle is that the parameters will be sent to the URL with an authentication of the API key.
        # THE API KEY should be passed as the key-value pair to the headers

#Once you either get() or post() into an API, you will recieve a response object which will be stored in a variable.
#To receive the JSON format of your response , you say : data= response.json().



import requests

response= requests.get("https://reqres.in");
print(response.status_code);
print(response.url);


response= requests.post("https://dummyapi.io/data/v1/user/create ", headers={
    "app-id": "62b0433d2dfd91d4bf56c584"
}, data={
    "firstName": "James", 
    "lastName": "Shelby", 
    "email": "jamesshelbysXXXX@dusmdemsy.com"

});

print(response.status_code);
print(response.json()["firstName"]);
print(response.json()["lastName"]);




response= requests.get("https://dummyapi.io/data/v1/user/",headers={"app-id": "62b0433d2dfd91d4bf56c584"})
data=response.json();
result= data["data"][0];

print(result['id']);


#USING AN API KEY
response= requests.get("https://api.openweathermap.org/data/2.5/weather", params={"appid": "9afc8ba689304327d6f998a73e4ecc44"});




json = {
    "errors": [
        {
            "status": "422",
            "source": {
                "pointer": "/data/attributes/firstName"
            },
            "title": "Invalid Attribute",
            "detail": "First name must contain at least two characters."
        }
    ]
}

### Write Your Code Below This Line
print(json["errors"]); # {'status': '422', 'source': {'pointer': '/data/attributes/firstName'}, 'title': 'Invalid Attribute', 'detail': 'First name must contain at least two characters.'}