from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

@app.route('/transaction', methods=['POST'])
def make_transaction():
    try:
        acc1 = request.form['acc1']
        p1 = request.form['p1']
        acc2 = request.form['acc2']
        eth = request.form['eth']
        

        nonce = web3.eth.get_transaction_count(acc1)
        
        balance = web3.eth.get_balance(acc1)

    

        if balance < web3.to_wei(eth, 'ether'):
            return jsonify({'message': 'Insufficient balance for the transaction.'}), 400

        tx = {
            'nonce': nonce,
            'to': acc2,
            'value': web3.to_wei(eth, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei'),
        }
        
        signed_tx = web3.eth.account.sign_transaction(tx, p1)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
 
        return jsonify({'transaction_hash': web3.to_hex(tx_hash)}), 200
    except Exception as e:
        # print(":gerererererrere")
        return jsonify({'error': str(e)}), 500

@app.route('/make_account', methods=['POST'])
def make_account():
    try:
        p2 = request.form['pri_key']
        acc2 = web3.eth.account.from_key(p2).address

        acc1 = "0x93eef1AFB989267AA54F4391Acd80f0A2507b6Bd"
        p1 = "0x856c9597eeaf0b33dc0b97a834fb624358362010226ce369609e1884efbb5cfd"
        

        nonce = web3.eth.get_transaction_count(acc1)
        
        balance = web3.eth.get_balance(acc1)

    

        if balance < web3.to_wei(100, 'ether'):
            return jsonify({'message': 'Insufficient balance for the transaction.'}), 400

        tx = {
            'nonce': nonce,
            'to': acc2,
            'value': web3.to_wei(100, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei'),
        }
        
        signed_tx = web3.eth.account.sign_transaction(tx, p1)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
 
        return jsonify({'transaction_hash': web3.to_hex(tx_hash), "address" : acc2, "private_key" : p2}), 200
    except Exception as e:
        
        return jsonify({'error': str(e)}), 500


@app.route('/get_balance', methods=['POST'])
def get_balance():
    try:
        address = request.form['address']
        
        
        balance = web3.from_wei( web3.eth.get_balance(address), "ether")

        return jsonify({"balance" : balance}), 200
    except Exception as e:
        
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
