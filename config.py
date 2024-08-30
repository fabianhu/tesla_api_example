# this is the configuration file.
# an example file "config.py.example" is checked in with the project.

home = (50.964668, 7.413264)

tesla_vin = 'LRWYAAAAAAA135456'
tesla_client_id = "aaaaaaaaaaaa-bbbb-cccc-ddddddddddd"
tesla_client_secret = "ta-secret.aaaaaaaaaaaaaaaa"  # only needed during registration, so does not ever need to be on the Pi!
# put your key pair here:
#lib/tesla_api/TeslaKeys/privatekey.pem
#lib/tesla_api/TeslaKeys/publickey.pem
# and store the pubkey at: https://your.domain/.well-known/appspecific/com.tesla.3p.public-key.pem
tesla_redirect_domain = "your.domain"  # NO https:// !!!
tesla_redirect_uri = "https://your.domain/and/stuff/"  # start with https:// and include a tailing '/'!
tesla_audience = "fleet-api.prd.eu.vn.cloud.tesla.com" # Europe
#tesla_audience =  "fleet-api.prd.na.vn.cloud.tesla.com" # North America
tesla_scopes = "user_data vehicle_device_data vehicle_cmds vehicle_charging_cmds energy_device_data energy_cmds"  # match with your application access request

tesla_ble = True # True if commands to be sent via BLE
allow_ble_reboot = True # allow programmatically reebooting the controller to fix a BLE issue
#tesla_remote = "user@192.168.1.77" # user:host if BLE command should be done on another device via SSH
tesla_remote = None # command to be sent from local device

