from random import randint
from prime import generate_random_prime

class PublicKey:
    def __init__(self):
        self.n = None
        self.__p = None
        self.__q = None
        self.__totient = None
        self.totient_coprime = None

    @property
    def pub_key(self):
        return self.n

    @pub_key.setter
    def pub_key(self, n):
        self.n = n

    def generate_totient_coprime(self):
        if self.__totient is None:
            return None

        self.totient_coprime = randint(2, self.pub_key)
        while self.totient_coprime % self.__totient == 0:
            self.totient_coprime = randint(2, self.pub_key)

        return self.totient_coprime

    def set_priv_key(self, __p, __q):
        self.__p = __p
        self.__q = __q
        self.__totient = (self.__p - 1) * (self.__q - 1)

    def transfer_priv_key(self, receiver):
        receiver.set_priv_key(self.__p, self.__q)

    def gen_pub_key(self, min=1, max=1000):
        self.__p = generate_random_prime(max)
        self.__q = generate_random_prime(max)

        while self.__p == self.__q:
            self.__q = generate_random_prime(max)

        self.__totient = (self.__p - 1) * (self.__q - 1)

        self.n = self.__p * self.__q

    def encrypt(self, m):
        return (m ** self.totient_coprime) % self.n


class Sender:
    def __init__(self, pubkey):
        self.pubkey = pubkey

    def send(self, message, receiver):
        tx = self.pubkey.encrypt(message)
        receiver.recv(tx, self.pubkey.pub_key(), self.pubkey.totient_coprime)
