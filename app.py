import requests, sys

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/bid', methods=['post'])
def bid():
    return jsonify({'url': 'http://example.com/image/999',
                    'price': 50})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
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
