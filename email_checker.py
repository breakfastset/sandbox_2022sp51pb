

def main():
    email = "adam.sandler@yahoo.com"

    if valid_email_format(email):
        print("Valid email format")
    else:
        print("Invalid email format")


def valid_email_format(email):
    """Return true if email contains @ and ."""
    return len(email) > 2 and (email.find("@") < email.rfind("."))


if __name__ == '__main__':
    main()
