# Blog Post
To run this Blog_post api in flask use follwing steps

# Step 1
Create virtual environment in any IDE of any system.

Or you can use following command to create one.

-> Install Virtual environment

For Windows
```bash
py -m pip install virtualenv
```
For Linux/Mac os
```bash
python -m pip install --user virtualenv
```


-> Create an environment
```bash
python -m venv <ENVIRONMENT NAME>
```
-> Access virtual environment
```bash
virtualenv <ENVIRONMENT NAME>
```
-> Start Virtual Environment 

For Windows
```bash
<ENVIRONMENT NAME>\Scripts\activate
```
For Linux/Mac os
```bash
source <ENVIRONMENT NAME>/bin/activate
```

# Step 2
Run following command to install all the requirement after starting virtual environment
```bash
pip install -r requirements.txt
```
# Step 3
After compilation of all requirements for the project run following command
```bash
set FLASK_APP=main.py
```

# Step 4
Now start the flask
```bash
flask run
```



# Expected URL link
Application started at localhost with port 5000

[127.0.0.1:5000/]( 127.0.0.1:5000/ )


# Link to check /api/ping
Check the status for API connectivity status

[127.0.0.1:5000/api/ping]( 127.0.0.1:5000/api/ping )

# Link to check /api/posts
I am providing two different example to check the parameters

-> Tag parameters are history and tech, sortBy is based on likes and in descending order 

[127.0.0.1:5000/api/posts?tags=history,tech&sortBy=likes&direction=desc]( 127.0.0.1:5000/api/posts?tags=history,tech&sortBy=likes&direction=desc )

-> Tag parameters is tech, sortBy is based on id and in ascending order 

[127.0.0.1:5000/api/posts?tags=tech&sortBy=id&direction=asc]( 127.0.0.1:5000/api/posts?tags=tech&sortBy=id&direction=asc )

# Step 5
To run test cases after staring flask server
```bash
python test.py
```
