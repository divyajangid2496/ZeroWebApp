Zero Web Application Development Using Flask

Approach:
1.	My approach to this problem was to first understand the Pig Latin conversion, figuring out the API or a database that could fetch me the county and population based on the provided zip code
2.	After doing some research on the internet, I came across an API named “uszipcode” in python. This API basically provides a SearchEngine that can be used to query and fetch county and population details by providing any of us zip code
3.	Next step was to figure out the UI that I will be using to provide a form to the user. For that I used the bootstrap template which helped me beautify the UI
4.	Then, I did all the setup for the flask and other depended libraries and exposed an endpoint “/create_pharse” (as mentioned in the problem description) that acted as an entry point of my web application
5.	“index.html” is my landing page that has the form which asks for a name and zip code from the user.
6.	On submit, fetch_data () method in the backend is called which does all the processing such as converting the provided name into Pig Latin, fetching county and population from the provided zip code. A python dictionary is created that stores all the fetched information such as latin_name, county and population details.
7.	In response, this dictionary is converted in json using python json.dumps()
8.	Html is then able to render the result using JavaScript logic of building the answer from a json.

Implementation:
1.	My application backend logic is in file named index.py. This is the python file that holds all the end API and backend logic
2.	My UI is named index.html. This page renders the form and displays the result on click of submit button
3.	The html file is in the template directory. And python file is in the project directory

Validations:
1.	I did some basic validation on the backend
•	If the request received is not json return msg “Missing JSON in request”
•	If name is blank, then return msg “Missing name parameter”
•	If zip code is blank, then return msg “Missing zip code parameter”
2.	For all the above errors the UI displays Invalid Input error on UI

Project Directory:
ZeroWebAppFlask
•	Templates
      o	index.html
•	index.py

GitHub: https://github.com/divyajangid2496/ZeroWebApp/tree/main/ZeroFlaskWebApp

WebApp Link: https://flask-app-zero-dj.herokuapp.com/create_phrase

