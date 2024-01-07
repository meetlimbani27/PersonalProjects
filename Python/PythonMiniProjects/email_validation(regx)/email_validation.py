k,j,d = 0,0,0
email = input("Enter your Email:")
if len(email)>=6:
   if email[0].isalpha():
      if ("@" in email) and (email.count("@")==1):
         if (email[-4]==".") ^ (email[-3]=="."):
            for i in email:
               if i == i.isspace():
                  k=1
               elif i.isalpha():
                  if i == i.upper():
                     j=1
               elif i.isdigit():
                  continue
               elif i=="_" or i=="." or i=="@":
                    continue
               else:
                  d=1

            if k == 1 or j==1 or d==1:
               print("wrong Email 5")
         
         else:
            print("wrong Email 4")
      else:
         print("wrong Email 3")
   else:
      print("wrong Email 2")
else:
   print("wrong Email 1")










# # using regex method and validation
# import re

# def validate_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     match = re.match(pattern, email)
#     if match:
#         return True
#     else:
#         return False

# # Test the function with example emails
# emails = ["user@example.com", "abc@def@ghi.com", "example@domain", "user name@example.com", "User@Example.com"]

# for email in emails:
#     if validate_email(email):
#         print(f"{email} is a valid email.")
#     else:
#         print(f"{email} is an invalid email.")

