
# This is a India and I am now in Noida"

# This is a Login Methon 
def login(username, password):
    if len(username) > 8 and '@' in username:
        if len(password) > 10:
            print("Login successful!")
        else:
            print("Password must be more than 10 characters.")
    else:
        print("Username must be more than 8 characters and contain '@' symbol.")

# This is another Login Method
def main():
    username = input("Enter your username: ") # Ameet@tjs.com
    password = input("Enter your password: ") # Parse78651112
    login(username, password)


#netry Point
if __name__ == "__main__":
    main()


