import random
import string
import time
from colorama import Fore, init

# Initialize colorama
init()

total = 0
found_btc = False

try:
    while not found_btc:
        btc_address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=34))
        hash_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=64))

        btc_amount = random.choices([random.uniform(0.01, 10.37), 0], [0.0000001, 0.9999])[0]
        btc_amount_str = "{:.8f}".format(btc_amount)

        if btc_amount != 0:
            found_btc = True
            random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            print(f"{Fore.GREEN}{btc_amount_str} BTC Found!")
            print(f"{Fore.BLUE}To redeem the bitcoins you found, please contact the owner and send him this ID:")
            print(f"{Fore.RED}{random_id}")
        else:
            print(f"{Fore.LIGHTRED_EX}Total: {Fore.LIGHTBLUE_EX}{total} {Fore.WHITE}- {Fore.RED}{btc_address}:{hash_string} {Fore.WHITE}:{Fore.BLUE} {btc_amount_str} BTC")
            total += 1

except KeyboardInterrupt:
    print("Program terminated by the user.")
