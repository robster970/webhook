from flask import Flask, request
import re
import os

# Servlet to listen for Docker Hub based webhook
# and rotate a new docker image into production

webhook_app = Flask(__name__)


@webhook_app.route('/notifications', methods=['POST'])
def foo():
    repo_url = 'https://hub.docker.com/r/robster970/sierra-nginx'
    repo_name = 'robster970/sierra-nginx'
    tag = 'latest'
    notification_data = str(request.data)
    print("Response from /notification endpoint")
    if re.search(repo_url, notification_data) and re.search(repo_name,
                                                            notification_data) and re.search(tag, notification_data):
        print('Match for repo_url: ', repo_url)
        print('Match for repo_name: ', repo_name)
        print('Match for tag: ', tag)
        # os.system('./sierra_docker_update.sh')
        os.system('./sierra_docker_test.sh')
    else:
        print('Partial or no match: ', notification_data)

    return "OK"


if __name__ == '__main__':
    webhook_app.run(host='0.0.0.0', port=15151)
