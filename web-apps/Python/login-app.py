new_user = input('Please enter a desired username: ').strip().lower()
new_pass = input('Please enter a desired password: ').strip().lower()

print('Please log in with your new username and password')

user = input('Enter username: ').strip().lower()
pswd = input('Enter password: ').strip().lower()

if user == new_user and pswd == new_pass:
    print(f'Welcome back {user}')
    #print('Welcome back {}'.format)
    
else:
    print('Please try again')