import threading
import snmp

def main():
     snmp.main()

if __name__ == '__main__':
     thread = threading.Thread(target=main)
     thread.start()
     thread.join()

