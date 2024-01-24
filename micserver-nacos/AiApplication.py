from flask import Flask

from controller.CommonController import common
from controller.AiController import ai

import logging
logging.basicConfig(filename='log/log.txt',
                     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                     level=logging.INFO)
urls = [common, ai]

app = Flask(__name__)

for url in urls:
    app.register_blueprint(url)

if __name__ == '__main__':
    from service.nacos.dto.NacosClient import NacosClient
    nacos_client = NacosClient(username="nacos", password="nacos", serviceName='py-ai', groupName='DEV_GROUP', namespaceId='fe84cfd2-e510-4a4a-815d-749341820650').authentication_func().register_func()
    nacos_client.persist_beat_func()
    app.run(port=8080, debug=True)