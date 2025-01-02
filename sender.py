from random import randint
from prime import generate_random_prime

class PublicKey:
    def __init__(self):
        self.n = None
        self.__p = None
        self.__q = None

    @property
    def pub_key(self):
        return self.n

    @pub_key.setter
    def pub_key(self, n):
        self.n = n

    def set_priv_key(self, __p, __q):
        self.__p = __p
        self.__q = __q

    def transfer_priv_key(self, receiver):
        receiver.set_priv_key(self.__p, self.__q)

    def gen_pub_key(self, min=1, max=1000):
        self.__p = generate_random_prime(max)
        self.__q = generate_random_prime(max)

        while self.__p == self.__q:
            self.__q = generate_random_prime(max)

        self.n = self.__p * self.__q

    def encrypt(self, m):
        pass


class Sender:
    def __init__(self, pubkey):
        self.pubkey = pubkey

    def send(self, message, receiver):
        tx = self.pubkey.encrypt(message)
        receiver.decrypt(tx)
