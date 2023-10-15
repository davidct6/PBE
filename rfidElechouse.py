from pynfc import Nfc, Desfire, Timeout

N = Nfc("pn532_uart:/dev/ttyS0:115200")
DESFIRE_DEFAULT_KEY = b'\x00'*8
MIFARE_BLANK_TOKEN =b'xFF'*1024*4

print("Apropeu targeta")

class rfidElechouse:
    def read_uid(self):
        for target in n.poll():
            try:
                uid = target.uid.decode().upper()
                return uid
            except TimeoutException:
                pass

if __name__ == "__main__":
    rf = rfidElechouse()
    uid =rf.read_uid()
    print(uid)
