# website
This is a new website for Colonial which contains a members only section of the page.


## Backend Setup (Django)
You need to use virutalenv to use the virtual environment for this project

1. First you need to use pip to install virtualenv
>	$ pip install virtualenv
2. Next use virtualenv to create your environment folder, where all your installed python modules will live.
>	$ virtualenv env OR ALTERNATIVELY $ virtualenv venv
3. Next you need to go activate your virtualenv
>	$ source env/bin/activate
4. Next you need to install the requirements for the project in your env folder
> 	(env) $ pip install -r requirements.txt
5. If you ever need to install something new, add it to requirements.txt, in the following form:
> module-name >= x.x.x

This way we will all have consistent dependencies and modules and we will also have a consistent environment with what we end up using in deployment.

To start the server, first make sure you have settings.py:
>	(env) $ cd colonialsite/colonialsite

>	(env) $ cp dummy_settings.py settings.py

Then perform migrations and start the server.
>	(env) $ python manage.py migrate

>	(env) $ python manage.py runserver

## Frontend Setup

First, in order to pass authentication, your NetID needs to be in the members.csv file.
Copy the example_members.csv file, rename it, and put your NetID in it.
>	$ cd colonialsite/coloauth

>	$ cp example_members.csv members.csv

Next, you'll need Node.js and NPM installed to run the webpack server.
Once you install Node.js and NPM, install dependencies:
>	$ cd colonialsite

>	$ npm install

Finally, run the webpack server.
>	$ node server.js

## Other

These are the developers:

PM:
Nicholas Yang

Frontend:
Andrew Ruchames(Lead)
Mel Shu
Jay Lee
Kathy Fan

Backend:
Bryan Zhu
Julie Zhu
