from sender import PublicKey, Sender
from receiver import Receiver

m_pubkey = PublicKey()
m_pubkey.gen_pub_key()
print(m_pubkey.pub_key)
