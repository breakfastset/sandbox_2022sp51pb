

def main():
    email = "adam_sandler@yahoo.com"
    if "@" in email and "." in email:
        print("Valid email format")
    else:
        print("Invalid email format")


if __name__ == '__main__':
    main()
