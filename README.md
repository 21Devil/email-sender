# email_sender

### Introduction
Simple Python program that allows user to send randomly generated quote 
from a csv file header 'Quote' to any gmail user. 
The program contains CLI which requires user to pass 3 arguments. 
<br>
### Install
<br>
Install from PyPI using 
[pip](https://pip.pypa.io/en/latest/), a package manager for Python.

```
pip install pyIsEmail
```
The program uses is_email from pyisemail library by [michaelherold](https://github.com/michaelherold/pyIsEmail) which checks
whether the email address user passed in as arguments for both sender and receiver are valid or not.
### Usage
Usage: python script.py sender_email app_password receiver_email
<br>
So, in terminal enter 

```python
python3 main.py example@gmail.com app_password example@gmail.com
```
If not installed install python3. Make sure that the password you enter 
is <b>app password</b> of sender email. Note: make sure there are no space in app password.
<br>
For details about how to get app password go here:
https://support.google.com/mail/answer/185833?hl=en-GB
<hr>

This is the first personal project I have made so there is no graphical component at all.
<br><br><br>
Original copy of csv file belongs to: https://gist.github.com/JakubPetriska/060958fd744ca34f099e947cd080b540
