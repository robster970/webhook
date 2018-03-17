from flask import Flask, request
import json

webhook_app = Flask(__name__)


@webhook_app.route('/notifications', methods=['POST'])
def foo():
    notification_data = json.loads(request.data)
    print("JSON response from /notification POST:")
    print(notification_data)
    return "OK"


if __name__ == '__main__':
    webhook_app.run(host='0.0.0.0', port=15151)
