import requests, sys, random, time

from flask import Flask, jsonify, request

app = Flask(__name__)
price_range = (1, 100)
sample_domain = 'example.com'

@app.route('/bid', methods=['post'])
def bid():
    if random.randint(1, 100) == 1: # 1/100 で sleep
        time.sleep(1)
    print('returned:', sample_domain)
    return jsonify({'url': f'http://{sample_domain}/image/999',
                    'price': random.randint(*price_range)})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
        sample_domain = str(sys.argv[2])
        debug = False
    except IndexError:
        port = 8888
        debug = True

#    # SSPに登録
#    r = requests.post('http://localhost:8080/buyer/registration',
#                      json={'bidRequestEndpoint': 'http://localhost:8888'})
#    if not r.ok:
#        print('SSP registration failed.')
#        exit(1)

    app.run(port=port, debug=debug)
