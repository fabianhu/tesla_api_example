# tesla_api_example
* Example implementation for the Tesla API 2024 in Python
* Uses the library [tesla_api](https://github.com/fabianhu/tesla_api)

## What you need
- A Tesla account
- For commands: A registered domain for public key hosting with a valid SSL certificate
- Until Tesla fixes the registration for hobbyist users, you need a VAT ID number. This does not need to be an exisiting number, it just needs to adhere to the rules for a valid VAT number. Google for what a VAT number looks like in your country/region and use your home adress.
- A mobile phone with the Tesla app installed for key installation to the car
- A Tesla car helps a lot

## What this example will guide you through
- Set up a developer account at Tesla, see [tutorial by Shankar](https://shankarkumarasamy.blog/2023/10/29/tesla-developer-api-guide-account-setup-app-creation-registration-and-third-party-authentication-configuration-part-1/)
- generate a public/private key pair for Tesla Vehicle Commands
- instruct you, how to host your public key in the `/.well-known` section of your website
- get a partner authentication token
- use this token to register a customer account (this may be the same as your developer account - you are your own customer)
- Check if Tesla has your public key recognized
- Request authorization permissions from a customer (for more than one customer, the library has to be extended)
- Install the public key to the customers car
- Get vehicle data
- Send commands to the car

## How to start
- run main.py
- fix all import issues (libraries not installed yet)
- follow the instructions
- If all runs well, your car will honk at you.

## Issues
* This is an implementation of [tesla_api](https://github.com/fabianhu/tesla_api), please report issues there
