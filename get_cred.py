def get_cred():

    """ Get the credentials required for SSH"""
    import getpass
    username = input("Enter Username: ")
    password = getpass.getpass("Enter password: ")
    
    return username, password


def main():

    username, password = get_cred()
    print(f"Username: {username}") 
    print(f"Password: {password}")

if __name__ == "__main__":
    main()

