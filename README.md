# Objective
Develop a Flask API which uses JWT so to use the functionalities of it. Such as:
* Able to Upload the Image
* Display the Name of the Image
* API is limited for 5 requests per minutes and deals with 1 minute of expiration

# Install the Dependencies for Python application
Python(Above 2.7)
flask
flask_limiter
flask_sqlalchemy (Not Yet Used)

# How to Run the application
--> Unzip the folder in the desired location

--> Open the terminal and set to the package location
        .../cvision-ai
--> Since it is Flask application, set the application to flask variable. So type it in the terminal
        export FLASK_APP=run.py (for Mac)
        set FLASK_APP=run.py (for Windows)
--> then write
        flask run

Incase if you are using Visual Code, Then open the package folder in the visual studio and then open "run.py" file. Right click to select the option: "Run Python File in Terminal".

By default it runs on the remote IP machine which is set as URL : http://127.0.0.1:5000/

--> Open the the borwser, type the above URL into it. The application will run.

# Output
The screenshots are captured in the Output.pdf file where the objectives such as:
--> Two webpage application (Upload the image and display the name of the image)
--> Json Web Tokens Validations
--> Image Validations
--> API limiter by 5 calls per minutes


# Acknowledgments
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
https://www.youtube.com/watch?v=J5bIPtEbS0Q
https://www.youtube.com/watch?v=vQleDvTM5xA&t=295s




