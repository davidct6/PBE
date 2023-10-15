from pynfc import Nfc, Desfire, TimeoutException

n = Nfc("pn532_uart:/dev/ttyS0:115200") 
DESFIRE_DEFAULT_KEY = b'\x00' * 8 
MIFARE_BLANK_TOKEN = b'\xFF' * 1024 * 4

class rfidImproved:
    for target in n.poll():
        try:
            uidbytes = target.uid