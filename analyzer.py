import requests
import sys
from colorama import Fore, init
# we are importing specific tools, not the whole libary of coloroma tools


init(autoreset=True) # init function will actually activiate coloroma 
# and it will intercipt our print functions applying its changes
# the autoreset=True part just ensures the colour is reset after each print
# or else we would be stuck with one colour

url = ""

if len(sys.argv) < 2: 
    print("NO URL INPUTTED")
    sys.exit()
    # will terminate program 

else:
    url = sys.argv[1]


# else block didnt matetr but added anyway for understanding and clarity

try:

    response = requests.get(url, timeout=5)
  

    if response.status_code == 200:
        print("SUCCESS CONNECTED")

        security_headers_to_check = [
            'Content-Security-Policy',
            'Strict-Transport-Security'
        ]

        print("\n--- Security Header Analysis ---")

        foundOrNot = True
        # intially set to true, if we cant find a specific header, we make it false
        for header in security_headers_to_check:
            if header in response.headers: # this is going to take constant time
                print(f"{Fore.GREEN} [FOUND] {header}")
            else:
                print(f"{Fore.RED} [MISSING] {header}")
                foundOrNot = False

        if foundOrNot == True:
            print("Secure: All critical secuirty headers were found.")
        else:
            print("Not Secure: One ore more critical secuirty headers are missing.")
    
    else:
        print(f"FAILED (Status Code: {response.status_code})")

except requests.exceptions.RequestException as e:
    # this code will run onlu if the connection fails.
    # this part of the code will run if there is a fundamental network problem, where connection itself isnt possible
    # the other part in the try block that outputs response for an unncessful connection is when the connection itself occurs, but the server denies our request
    print(f"Could not connect to the URL. Error: {e}")