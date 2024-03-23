from web3 import Web3
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

private_key = "ce2c7b0b166145d6830e0b60f6009038a7d7b08751c5ea1095662c62e2bf977b"


account = web3.eth.account.from_key(private_key)

print("Address:", account.address)
print("Private Key:", private_key)


# acc1 = '0x93eef1AFB989267AA54F4391Acd80f0A2507b6Bd'

# p1 = "0x856c9597eeaf0b33dc0b97a834fb624358362010226ce369609e1884efbb5cfd"

acc2 = web3.eth.account.from_key('76f41de1637335b1a60db3514781809350713cdfb0c8df6c80366b319d923228').address

p2 = "76f41de1637335b1a60db3514781809350713cdfb0c8df6c80366b319d923228"

nonce = web3.eth.get_transaction_count(account.address)

t = web3.eth.get_balance(account.address)

print(web3.from_wei(web3.eth.get_balance(acc2), 'ether'), "account 2")

print(web3.from_wei(t, "ether"), "Account 1")
tx = {
    'nonce': nonce,
    'to': acc2,
    'value': web3.to_wei(100, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
}



# # tempstring  = '''
# # flutter: Mne : market review actor clown blouse infant envelope regular amused torch panic feature
# # flutter: pri : ce2c7b0b166145d6830e0b60f6009038a7d7b08751c5ea1095662c62e2bf977b
# # flutter: Public : 0xa94a39901b262ffc4918fb1b49f522120dd6f224
# # '''


tempa = '''flutter: Mne : abandon impact label three upgrade kidney tattoo lizard size cube salon bubble
flutter: pri : 76f41de1637335b1a60db3514781809350713cdfb0c8df6c80366b319d923228
flutter: Public : 0x7d5485b9b23b58e8778fdc989294c0a872dbdfdf'''

signed_tx = web3.eth.account.sign_transaction(tx, private_key)

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(web3.to_hex(tx_hash))

print(web3.from_wei(web3.eth.get_balance(account.address), "ether"))
print(web3.from_wei(web3.eth.get_balance(acc2), 'ether'), "account 2")