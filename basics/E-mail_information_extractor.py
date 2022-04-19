def main():


    popular_domains = {
    "@gmail": "Google",
    "@hotmail": "Microsoft",
    "@yahoo": "Yahoo",
    "@outlook": "Microsoft"}
    # Get user email address
    email = input("What is your email address?: ").strip()

    # Slice out the user name
    user_name = email.split('@')[0]
    # # user_name = email[:email.index("@")]
    
    # # Slice the domain name
    domain_name = email[email.index("@"):]
    domain_name = domain_name.split('.')[0]

    # Format message
    if domain_name in popular_domains.keys():
        print(f"\tHey {user_name} it seems like your email is registered with {popular_domains[domain_name]}!!!")
    else:
        print(f"\tHey {user_name} it seems like you have your own custom domain at \"{domain_name[1:]}\"!")
    # # Display output message

if __name__ == '__main__':
    main()