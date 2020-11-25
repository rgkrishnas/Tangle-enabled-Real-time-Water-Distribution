### This is developed by Gopal (rgkrishnas@gmail.com) for IOTA payment
## payment_transfer() function needs to be called from main program with valid address to transfer the fund
## e.g. given below

import iota
from pprint import pprint
import config
#address = config.wallet_address
myseed = config.mywatersensor_seed
DEVICE_ID=config.DEVICE_ID
def payment_transfer(transfer_address):
    api = iota.Iota("https://nodes.iota.org:443",myseed) #,local_pow=True
    
    # Preparing transactions
    pt = iota.ProposedTransaction(address = iota.Address(transfer_address),
                                  message = iota.TryteString.from_unicode('Automatic Water consumption payment from '+str(DEVICE_ID)),
                                  tag     = iota.Tag(b'SMARTWATERFLOWMEASURE'), # Up to 27 trytes
                                  value   = 1)
    
    # `send_transfer` will take care of the rest
    response = api.send_transfer([pt])
    
    pprint('Broadcasted bundle:')
    pprint(response['bundle'].as_json_compatible())
    
#payment_transfer(b'WaterDeptWalletAddressForFundTransfer') # sample address for Water dept
