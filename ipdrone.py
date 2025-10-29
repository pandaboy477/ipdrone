# coded by N17RO (noob hackers)
# safe/fixed version to avoid KeyError on missing fields (e.g., 'isp')

import argparse
import requests, json
import sys
import os

# arguments and parser
parser = argparse.ArgumentParser()
parser.add_argument("-v", help="target/host IP address", type=str, dest='target', required=True)
args = parser.parse_args()

# colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# banner of script
print(red + """

██╗██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗
██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║██████╔╝██║  ██║██████╔╝██║   ██║██╔██╗ ██║█████╗  
██║██╔═══╝ ██║  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══╝  
██║██║     ██████╔╝██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                      v 1.0
""" + red)
print(lgreen + bold + "         <===[[ coded by N17RO ]]===> \n" + clear)
print(yellow + bold + "   <---(( search on youtube Noob Hackers ))--> \n" + clear)

ip = args.target
api = "http://ip-api.com/json/"

try:
    response = requests.get(api + ip, timeout=10)
    # ensure we got valid json
    data = response.json() if response.status_code == 200 else {} 

    # helper to safely get a key with a fallback value
    def safe(key, default="N/A"):
        # if data is not a dict or key not present, return default
        try:
            return data.get(key, default) if isinstance(data, dict) else default
        except Exception:
            return default

    sys.stdout.flush()
    a = lgreen + bold + "[$]"
    b = cyan + bold + "[$]"

    print(a, "[Victim]:", safe('query'))
    print(red + "<--------------->" + red)
    print(b, "[ISP]:", safe('isp'))
    print(red + "<--------------->" + red)
    print(a, "[Organisation]:", safe('org'))
    print(red + "<--------------->" + red)
    print(b, "[City]:", safe('city'))
    print(red + "<--------------->" + red)
    print(a, "[Region]:", safe('region'))
    print(red + "<--------------->" + red)
    print(b, "[Longitude]:", safe('lon'))
    print(red + "<--------------->" + red)
    print(a, "[Latitude]:", safe('lat'))
    print(red + "<--------------->" + red)
    print(b, "[Time zone]:", safe('timezone'))
    print(red + "<--------------->" + red)
    print(a, "[Zip code]:", safe('zip'))
    print(" " + yellow)

except KeyboardInterrupt:
    print('Terminating, Bye' + lgreen)
    sys.exit(0)

except requests.exceptions.ConnectionError:
    print(red + "[~] check your internet connection!" + clear)
    sys.exit(1)

except requests.exceptions.Timeout:
    print(red + "[~] request timed out, check your internet!" + clear)
    sys.exit(1)

except ValueError:
    # invalid JSON
    print(red + "[~] received invalid response from API" + clear)
    sys.exit(1)

except Exception as e:
    # catch-all to avoid crash; show error for debugging
    print(red + "[!] unexpected error:", str(e) + clear)
    sys.exit(1)