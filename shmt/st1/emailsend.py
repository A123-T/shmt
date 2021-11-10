import smtplib as s
import random
r = random.randint(1111,999999)
r = str(r)
print(r)
ob = s.SMTP("smtp.gmail.com", 587)
ob.starttls()
ob.login("abhinavtyagi0123@gmail.com","Abhinav@123")
subject = "Sending email using Python"
body = "This is Abhinav tyagi .http://127.0.0.1:8000/changepwd1?token="+r
message = "Subject:{}\n\n{}".format(subject, body)
#print(message)
send_to ="abhinavtyagi770@gmail.com"
ob.sendmail("abhinavtyagi0123@gmail.com",send_to,message)
print("sucessfully send........")
ob.quit()