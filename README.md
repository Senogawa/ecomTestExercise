# How to start web application?

In the working directory with the project, you need to create a virtual environment and load the necessary libraries.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**Next you need to launch the web application with the following command:**  
```
python3 manage.py runserver
```
***Then you can send post requests using the link:*** 
http://127.0.0.1:8000/get_form/

____

The project contains a test database **tiny.json**, work with it is carried out through **tinydb**.  


# Unit Tests (Only with running server)
Tests have been written for the project. They are located:
```
ecom_forms/forms_functions/test_forms.py
```
```
ecom_forms/test_requests.py
```
**To run all tests you can use the command:**
```
python3 -m unittest
```