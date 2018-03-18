from flask import Flask, request, abort, jsonify
import re
import os

# Flask based servlet to listen for Docker Hub webhook indicating a
# new container has been built in Travis.
# Rotate a new docker image into production,
# clean up local filesystem of redundant docker images and containers

webhook_app = Flask(__name__)


@webhook_app.route('/notifications', methods=['POST'])
def webhook():
    repo_url = 'https://hub.docker.com/r/robster970/sierra-nginx'
    repo_name = 'robster970/sierra-nginx'
    tag = 'latest'
    notification_data = str(request.data)
    if request.method == 'POST':
        print("Response from /notifications endpoint")
        if re.search(repo_url, notification_data) and re.search(repo_name,
                                                                notification_data) and re.search(tag,
                                                                                                 notification_data):
            print('Match for repo_url: ', repo_url)
            print('Match for repo_name: ', repo_name)
            print('Match for tag: ', tag)
            os.system('./sierra_docker_update.sh')
            # os.system('./sierra_docker_test.sh')
            return jsonify({'status': 'success'}), 200
        else:
            print('Partial or no match, JSON: ', notification_data)
            return jsonify({'status': 'forbidden'}), 403
    else:
        abort(400)


if __name__ == '__main__':
    webhook_app.run(host='0.0.0.0', port=15151)
