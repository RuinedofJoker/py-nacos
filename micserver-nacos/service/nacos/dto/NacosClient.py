import requests
from threading import Thread, Timer
from time import sleep
import logging

import service.nacos.constants.NacosUrls as NacosUrls

"""https://nacos.io/zh-cn/docs/open-api.html"""
class NacosClient:

    # nacos的ip
    nacosIp_ = '127.0.0.1'
    # nacos的端口
    nacosPort_ = 8848
    # 注册服务ip
    ip = '127.0.0.1'
    # 注册服务端口
    port = 8080
    # 往注册中心服务名称
    serviceName = None
    # 注册到的命名空间id
    namespaceId = None
    # 注册到的集群名
    clusterName = None
    # 注册到的分组名
    groupName = None

    # 权重
    weight = None
    # 是否临时实例
    ephemeral = True
    # 扩展信息
    metadata = None
    # 是否健康
    healthy = None

    # nacos登录名
    username = None
    # nacos密码
    password = None
    # 登录密钥
    accessToken = None

    # 编码
    encoding = None

    def __dir__(self):
        return ['nacosIp_', 'nacosPort_', 'ip', 'port', 'serviceName', 'namespaceId', 'clusterName', 'groupName', 'weight', 'ephemeral', 'metadata', 'healthy', 'username', 'password', 'accessToken']

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        attr_dict = {}
        for attr_ in dir(self):
            if not(attr_[:2] == '__' and attr_[-2:] == '__'):
                attr_dict[attr_] = getattr(self, attr_)
        return str(attr_dict)
    
    def getParams(self) -> dict:
        attr_list = self.dir()
        param_dict = {}
        for attr_ in attr_list:
            if not(attr_[-1:] == '_' or getattr(self, attr_) == None):
                param_dict[attr_] = getattr(self, attr_)
        if self.accessToken != None:
            param_dict['accessToken'] = self.accessToken
        return param_dict
    
    def getParams(self, paramList : list) -> dict:
        if paramList == None:
            return self.getParams()
        param_dict = {}
        for attr_ in paramList:
            if hasattr(self, attr_) and getattr(self, attr_) != None:
                param_dict[attr_] = getattr(self, attr_)
        if self.accessToken != None:
            param_dict['accessToken'] = self.accessToken
        return param_dict

    def authentication_func(self):
        if self.username == None and self.password == None:
            return self
        try:
            self.username = self.username if self.username != None else 'nacos'
            self.password = self.password if self.password != None else 'nacos'
            response_ = getattr(requests, 'post')(f'{self.getNacosUri()}{NacosUrls.auth["authentication"]["url"]}?username={self.username}&password={self.password}')
            self.accessToken = response_.json()['accessToken']
            if self.accessToken == None:
                logging.error(response_.text)
                raise Exception
        except Exception as e:
            logging.error(str(e))
            raise Exception('登录失败，用户名或密码错误')
        return self

    def register_func(self):
        try:
            response_ = self.getNacosResponse(NacosUrls.discovery['register'])
            if response_.text != 'ok':
                logging.error(response_.text)
                raise Exception()
        except Exception as e:
            logging.error(str(e))
            raise Exception('服务注册失败')
        return self
    
    def beat_func(self):
        try:
            response_ = self.getNacosResponse(NacosUrls.discovery['beat'])
            if not response_.json()['lightBeatEnabled']:
                print(response_.text)
                raise Exception()
        except Exception as e:
            logging.error(str(e))
            self.authentication_func()
            raise Exception('服务心跳发送失败')
        return self
    
    def persist_beat_func(self):
        def published_beat_func():
            while True:
                try:
                    Timer(5, self.beat_func, ()).start()
                except Exception as e:
                    logging.error(str(e))
                sleep(5)
        try:
            Thread(target=published_beat_func).start()
        except Exception as e:
            logging.error(str(e))
            raise Exception('持续服务心跳启动失败')
        return self

    def unregister_func(self):
        """TODO"""
        try:
            response_ = self.getNacosResponse(NacosUrls.discovery['unregister'])
            #if response_.text != 'ok':
            print(response_.text)
            #    raise Exception()
        except Exception as e:
            logging.error(str(e))
            raise Exception('服务注销失败')
        return self

    def getNacosUri(self) -> str:
        return f'http://{self.nacosIp_}:{str(self.nacosPort_)}'
    
    def getUrl(self, api : dict) -> str:
        return self.getNacosUri() + api['url']
    
    def getParamsUrl(self, api : dict, paramsDict=None, paramsMixed=True) -> str:
        base_url = self.getUrl(api)
        req_params = self.getParams(api['params']) if paramsDict == None or paramsMixed else paramsDict
        if paramsMixed and paramsDict != None:
            req_params.update(paramsDict)
        req_param = ''
        for param_key in req_params.keys():
            req_param = f'{req_param}&{param_key}={req_params[param_key]}'
        req_param = f'?{req_param[1:]}' if req_param != '' else ''
        return base_url + req_param

    def getNacosResponse(self, api : dict, paramsDict=None, paramsMixed=True):
        url_ = self.getParamsUrl(api, paramsDict, paramsMixed)
        logging.debug(f'-Request=[{api["method"]}_{url_}]')
        resp_ = getattr(requests, api['method'])(url_)
        logging.debug(f'-Response=["code":{resp_.status_code}];"body":{resp_.text}')
        return resp_