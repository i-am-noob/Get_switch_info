def get_cred():

    """ Get the credentials required for SSH"""
    import getpass
    username = input("Enter Username: ")
    password = getpass.getpass("Enter password: ")
    
    return username, password


def main():

    user, pwd = get_cred()
    print(f"Username: {user}") 
    print(f"Password: {pwd}")

if __name__ == "__main__":
    main()

