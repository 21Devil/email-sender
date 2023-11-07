# email_sender

### Introduction
Simple Python program that allows user to send randomly generated quote 
from a csv file header 'Quote' to any gmail user. 
The program contains CLI which requires user to pass 3 arguments. 
This is the first personal project I have made so there is no graphical component at all.
<br>

### Install
No major install needed. If not installed install python3. Make sure that the password you enter 
is <b>app password</b> of sender email. Note: make sure there are no space in app password.
<br>
I first used pyIsEmail library to validate email but it had some uncomatibility with some devices 
and had to be installed externally which some of users struggled. So, in second commit I changed to use of re standard python 
library to check emails which turned out to be just as efficient. I could just import match from re library to reduce the space taken by
the entire library but I forgot it at second commit. If I do have some major changes that will be done in third commit.
<br>

### Usage
Usage: python script.py sender_email app_password receiver_email
<br>
So, in terminal enter 

```python
python3 main.py example@gmail.com app_password example@gmail.com
```

For details about how to get app password go here:
https://support.google.com/mail/answer/185833?hl=en-GB
<br><br><br>
### Credit
Original copy of csv file belongs to: https://gist.github.com/JakubPetriska/060958fd744ca34f099e947cd080b540
