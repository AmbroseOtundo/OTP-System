import os
import math
import random
import smtplib


# Creating a string of digits and an empty string.
digits="0123456789"
OTP=""

# This is the code for generating the OTP.
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp

# This is the code for sending the OTP to the user's email.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")

# This is the code for verifying the OTP.
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")