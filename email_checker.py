

def main():
    email = "adam_sandler@yahoo.com"
    if valid_email_format(email):
        print("Valid email format")
    else:
        print("Invalid email format")


def valid_email_format(email):
    """Return true if email contains @ and ."""
    return "@" in email and "." in email


if __name__ == '__main__':
    main()
