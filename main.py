# This is an example of how to use the library tesla_api

import os
import config
import lib.tesla_api.tesla_api_2024 as tesla_api
import lib.logger as logger

def register_developer_account():
    # register a developer account
    # this is only needed once, and the client_id and client_secret are stored in the config file

    # check, if .dev_registered file exists
    try:
        with open(".dev_registered", "r") as f:
            if f.read() == "registered":
                print("The developer account is already registered")
                print("delete the file '.dev_registered' to re-register the developer account")
                return
    except FileNotFoundError:
        pass

    print("Registering a developer account")
    print("Please go to the following URL and register a developer account and your app:")
    print("https://developer.tesla.com/")
    input("Press [Enter] to continue, when registration is complete or <Ctrl-C> to cancel...")

    if config.tesla_client_id == "aaaaaaaaaaaa-bbbb-cccc-ddddddddddd":
        print("Please enter the client_id and client_secret and the rest of the info into the config.py file")
        logger.error("Please enter the client_id and client_secret and the rest of the info into the config.py file and restart")
        exit(1)

    # generate the keys
    # check, if os command openssl is available
    if os.name == 'nt':
        print("Sorry, this script might not work on Windows")
        return
    if os.system("openssl version") != 0:  # check, if openssl is installed with return code
        print("Sorry, this script requires openssl to be installed")
        return

    # check, if the keys already exist
    if os.path.exists("lib/tesla_api/TeslaKeys/privatekey.pem"):
        print("The keys already exist in the directory 'lib/tesla_api/TeslaKeys'")

    else:
        print("Generating your keys in the directory 'lib/tesla_api/TeslaKeys'...")
        os.system("openssl ecparam -name prime256v1 -genkey -noout -out lib/tesla_api/TeslaKeys/privatekey.pem")
        os.system("openssl ec -in lib/tesla_api/TeslaKeys/privatekey.pem -pubout -out lib/tesla_api/TeslaKeys/com.tesla.3p.public-key.pem")

    # push the public key to your domain
    print("Please push the public key 'lib/tesla_api/TeslaKeys/com.tesla.3p.public-key.pem' to your domain at the following URL:")
    print(f"https://{config.tesla_redirect_domain}/.well-known/appspecific/com.tesla.3p.public-key.pem")
    print(f"optional: put the php script 'tesla_api/WWW-example/index.php' to your {config.tesla_redirect_uri} directory to ease the code retrieval for later customer registration")
    input("Press Enter to continue, when the public key is pushed...")

    # get partner token
    print("Getting the partner token...")
    partner_token = tesla_api.tesla_get_partner_auth_token(config.tesla_client_id, config.tesla_client_secret, config.tesla_audience)
    if partner_token is None:
        print("Getting the partner token failed")
        return
    # print("Partner token:", partner_token)

    print(f"Registering the partner account and domain {config.tesla_redirect_domain}")
    _r = tesla_api.tesla_register_partner_account(partner_token, config.tesla_audience)  # fixme do this for every audience where you expect to register customers
    # already printed from above fn. print("Registration result:", _r)
    if _r.get("client_id") == config.tesla_client_id:
        print("Registration was successful!")
    else:
        re = input("Was the registration successful? (y/n/d) (d=don't know) ")
        if re == "d":
            # print a good result
            print("A good result looks like this (field order may vary):")
            print("{'client_id': 'aaaaaaaaaaaa-bbbb-cccc-dddddddddddd', 'name': 'Your app name', 'description': 'your application description', 'domain': 'your.domain', 'ca': None, 'created_at': '2024-02-02T02:02:02.002Z', 'updated_at': '2024-02-02T02:02:02.002Z', 'enterprise_tier': 'free', 'account_id': 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'issuer': None, 'public_key': 'aaaaaaaaaaaaaaaa  ...")
            # ask again
            re = input("Was the registration successful? (y/n) ")
        if re != "y":
            print("Please check the configuration and try again")
            exit(1)

    # save the state in a signal file
    with open(".dev_registered", "w") as f:
        f.write("registered")
    pubkey_from_reg = _r.get("public_key")

    # wait for key press
    input("Press Enter to continue...")

    # bonus step
    print("Checking the public key with the Tesla server...")
    _r = tesla_api.tesla_partner_check_public_key(partner_token, config.tesla_audience)
    if _r.get("public_key") == pubkey_from_reg:
        print("The public key is correctly registered with the Tesla server!")
    else:
        print("The public key is not correctly registered with the Tesla server!")
        print("registered:", pubkey_from_reg)
        print("server:", _r.get("public_key"))
        exit(1)

    # wait for key press
    input("Press Enter to continue...")


if __name__ == '__main__':
    # test functions of the library tesla_api here:

    print("Welcome to the guided tour of the tesla_api library\n")

    register_developer_account()

    myTesla = tesla_api.TeslaAPI()

    # check, if token myTesla.token_file is available
    if not os.path.exists(myTesla.token_file):
        print("The token file does not yet exist - we register the customer account now...")
        tesla_api.tesla_register_customer(myTesla)

    # get the vehicle info
    vl = myTesla.get_vehicles_list()
    print(vl)

    vin = vl[0]['vin']

    # wake up the car to be able to get the vehicle data
    myTesla.cmd_wakeup(vin)

    # get the vehicle data
    vd = myTesla.get_vehicle_data(vin)
    print(vd)

    # before sending commands, we have to register the key with the car (once)
    print("Install the app key to the car using the Tesla app")
    tesla_api.tesla_register_customer_key() # this will install the key to the car using Tesla's server and the Tesla app

    # to send commands from this app, we have to build the Go client "tesla-control" first
    # check, if the Go client is available
    if not os.path.exists("lib/tesla_api/tesla-control/tesla-control"):
        print("The Go client 'tesla-control' is not available")
        print("Please build it first following the instructions in the go building.txt file in the directory 'lib/tesla_api/tesla-control'")
        # stop here
        exit()

    # send a command to the car
    myTesla.tesla_command("honk", vin)
    # see the source code of the tesla_api library for more commands




