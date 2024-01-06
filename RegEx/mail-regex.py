import re

p = r'[a-zA-Z0-9_\.\-]+@[a-zA-Z\-]{3,8}\.[a-zA-Z]{2,5}'

def email_validation(email):
	if(re.fullmatch(p, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

if __name__ == '__main__':

	email = "dummymail15@gmail.org"
	email_validation(email)
	
	email = "dashmail152@e-mail.in"	
	email_validation(email)
	
	email = "onemoremail.com"
	email_validation(email)
