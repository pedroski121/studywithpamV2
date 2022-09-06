To run this on your pc

1. Ensure you have python3 and pip installed on your local machine
2. In the project directory run
   pip install -r requirements.txt or
   py -m pip install -r requirements.txt
   if any module is missing, install it
3. In the directory where this project is located
   Open up the terminal and run
   set FLASK_DEBUG=1
   set FLASK_APP=studywithpamV2
4. In the project directory, open the routes directory and change the name of the aws folder to .aws
5. Get your preferred aws region, aws_access_key_id and aws_secret_access_key and change them where neccessary in the
   credential and config files that are found in .aws directory
6. Copy the .aws folder and paste it at C:\Users\user
7. If an error such as "The difference between the request time and the current time is too large" occurs.
   Make sure you synchronize your computer clock
8. In the directory where the project using your terminal
   run
   from studywithpamV2 import db
   from studywithpamV2.extensions import db
   from studywithpam import create_app
   from studywithpamV2 import create_app
   from studywithpamV2.models import \*
   db.create_all(app=create_app())
