To run this on your pc

1. Ensure you have python3 and pip installed on your local machine
2. In the project directory run <br/>
   '''pip install -r requirements.txt'''<br/>
   or
   '''py -m pip install -r requirements.txt '''<br/>
   if any module is missing, install it<br/>
3. In the directory where this project is located<br/>
   Open up the terminal and run<br/>
   '''set FLASK_DEBUG=1'''<br/>
   '''set FLASK_APP=studywithpamV2'''<br/>
4. In the project directory, open the routes directory and change the name of the aws folder to .aws<br/>
5. Get your preferred aws region, aws_access_key_id and aws_secret_access_key and change them where neccessary in the
   credential and config files which are found in the .aws directory
6. Copy the .aws folder and paste it at C:\Users\user
7. If an error such as "The difference between the request time and the current time is too large" occurs.
   Make sure you synchronize your computer clock
8. Using your terminal, navigate to the directory where studywithpamV2 is located<br/>
   run<br/>
   '''from studywithpamV2 import db'''<br/>
   '''from studywithpamV2.extensions import db'''<br/>
   '''from studywithpam import create_app'''<br/>
   '''from studywithpamV2 import create_app'''<br/>
   '''from studywithpamV2.models import \* '''<br/>
   ''' db.create_all(app=create_app())'''<br/>
