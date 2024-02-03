# This is an example of how to use the library tesla_api
import config
import lib.tesla_api.tesla_api_2024 as tesla_api

def register_developer_account():
    # register a developer account
    # this is only needed once, and the client_id and client_secret are stored in the config file
    print("Registering a developer account")
    print("Please go to the following URL and register a developer account and your app:")
    print("https://developer.tesla.com/")
    input("Press [Enter] to continue, when registration is complete or <Ctrl-C> to cancel...")

    if config.tesla_client_id == "aaaaaaaaaaaa-bbbb-cccc-ddddddddddd":
        print("Please enter the client_id and client_secret and the rest of the info into the config.py file")
        return

    # generate the keys
    # check, if os command openssl is available
    import os
    if os.name == 'nt':
        print("Sorry, this script might not work on Windows")
        return
    if os.system("openssl version") != 0:  # check, if openssl is installed
        print("Sorry, this script requires openssl to be installed")
        return

    # check, if the keys already exist
    if os.path.exists("lib/tesla_api/TeslaKeys/privatekey.pem"):
        print("The keys already exist")

    else:
        print("Generating the keys...")
        os.system("openssl ecparam -name prime256v1 -genkey -noout -out lib/tesla_api/TeslaKeys/privatekey.pem")
        os.system("openssl ec -in lib/tesla_api/TeslaKeys/privatekey.pem -pubout -out lib/tesla_api/TeslaKeys/public-key.pem")

    # push the public key to your domain
    print("Please push the public key 'lib/tesla_api/TeslaKeys/publickey.pem' to your domain at the following URL:")
    print(f"https://{config.tesla_redirect_domain}/.well-known/appspecific/com.tesla.3p.public-key.pem")
    re = input("Press Enter to continue, when the public key is pushed... or press <d> to confirm done.")
    if re != "d":
        return

    # get partner token
    print("Getting the partner token...")
    partner_token = tesla_api.tesla_get_partner_auth_token(config.tesla_client_id, config.tesla_client_secret, config.tesla_audience)
    _r = tesla_api.tesla_register_partner_account(partner_token, config.tesla_audience)
    print("Registration result:", _r)

    re = input("Was the registration successful? (y/n)")
    if re != "y":
        return


def register_customer_account():
    """
    Register a customer account

    :return:
    """
    myTesla = tesla_api.TeslaAPI()

    print("Registering this app to the customer account using the Tesla app")
    tesla_api.tesla_register_customer(myTesla)

    re= input("Was the registration successful? (y/n)")
    if re != "y":
        return
    print("The app is now registered to the customer account")
    print("Install the app key to the car using the Tesla app")
    tesla_api.tesla_register_customer_key() # this will install the key to the car using Tesla's server and the Tesla app




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test functions of the library tesla_api here:
    pass


