# nacos获取认证accessToken
auth = {
    'authentication': {
        'url': '/nacos/v1/auth/login',
        'method': 'post',
        'params': ['username', 'password']
    }
}


"""nacos注册中心"""
discovery = {
    'register': {
        'url': '/nacos/v1/ns/instance',
        'method': 'post',
        'params': ['ip', 'port', 'namespaceId', 'weight', 'enabled', 'healthy', 'metadata', 'clusterName', 'serviceName', 'groupName', 'ephemeral']
    },
    'unregister': {
        'url': '/nacos/v1/ns/instance',
        'method': 'delete',
        'params': ['serviceName', 'groupName', 'ip', 'port', 'clusterName', 'namespaceId', 'ephemeral']
    },
    'updateregister': {
        'url': '/nacos/v1/ns/instance',
        'method': 'put',
        'params': ['serviceName', 'groupName', 'ip', 'port', 'clusterName', 'namespaceId', 'weight', 'metadata', 'enabled', 'ephemeral']
    },
    'beat': {
        'url': '/nacos/v1/ns/instance/beat',
        'method': 'put',
        'params': ['serviceName', 'ip', 'port', 'namespaceId', 'groupName', 'ephemeral', 'beat']
    }
}

"""nacos配置中心"""
config = {
    
}