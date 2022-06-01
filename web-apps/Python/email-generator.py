#SIMPLE NEW HIRE CREDENTIAL GENERATOR
import random

def genEmployee():
  firstName = input('Enter employee first name... ').capitalize()
  lastName = input('Enter employee last name... ').capitalize()
  email = '@company.com'  
  slackUser = 'Employee slack username is: '
  slackPass = 'Employee slack password is: '
  uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowercase_letters = uppercase_letters.lower()
  digits = "0123456789"
  symbols = ",./;'[]{}()*&%$#@!\\?-+_ "
  
  upper, lower, nums, syms = True, True, True, True
  
  all = ""
  
  if upper: 
      all += uppercase_letters
  if lower:
      all += lowercase_letters
  if nums:
      all += digits
  if syms: 
      all += symbols
  
  amount = 10
  
  for x in range(amount):
    length_password = int(input("Enter the length of the password : "))
    password = "".join(random.sample(all, length_password))
    print('Employee name:' + ' ' + firstName.capitalize() +' '+ lastName.capitalize())
    print('Employee email:' + ' ' + firstName[0].lower() + '.' + lastName.lower() + email)
    print(slackUser + firstName[0] + lastName)
    print(slackPass + ' ' + password)

    return
genEmployee()