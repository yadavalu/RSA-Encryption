class Receiver:
    def __init__(self):
        self.__p = None
        self.__q = None

    def set_priv_key(self, __p, __q):
        self.__p = __p
        self.__q = __q

    def recv(self, encrypted, pubkey, coprime):
        message = self.decrypt(encrypted, pubkey, coprime)
        return message

    def decrypt(self, encrypted, pubkey, coprime):
        pass
