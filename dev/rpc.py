#!/usr/bin/env python
# coding=utf-8
import xmlrpclib

# server_url = 'http://42.96.194.60:4560'
# server = xmlrpclib.ServerProxy(server_url)
#
# EJABBERD_XMLRPC_LOGIN = {'user': 'zyf', 'server': 'coopens.com', 'password': '123456'} # , 'token': 'k1iTItUPDgH9NB4yTFYyTttRtNIlHjyV'
#
# def ejabberdctl(command, data):
#     fn = getattr(server, command)
#     return fn(EJABBERD_XMLRPC_LOGIN, data)
#
# result = ejabberdctl('register', {'user':'ggeo221', 'host':'coopens.com', 'password':'gogo11'})
# print result


server_url = 'http://47.90.15.40:4560'
# server_url = 'http://127.0.0.1:4560'
# http://dongweiming.github.io/blog/archives/guanyuxmlrpclibyanjiu/
# 返回一个连接服务器的实例,verbose=True显示调试信息，否则直接输出结果
# encoding='gbk':默认的编码是utf－8，这里可以修改成'gbk'。
server = xmlrpclib.ServerProxy(server_url, verbose=True)

EJABBERD_XMLRPC_LOGIN = {'user': 'zyf', 'server': 'coopens.com',
                         'password': '123456', 'admin': True}  #, 'admin': True , 'token': 'k1iTItUPDgH9NB4yTFYyTttRtNIlHjyV'


def ejabberdctl(command, data):
    fn = getattr(server, command)
    print "IIIIIIIIII"
    # print fn
    print "UUUUUUUUUU"
    return fn(EJABBERD_XMLRPC_LOGIN, data)


# result = ejabberdctl('register', {'user':'ggeo224', 'host':'coopens.com', 'password':'gogo11'})
# result = ejabberdctl('check_account', {'user': 'c-1', 'host': 'coopens.com'})
result = ejabberdctl('get_roster', {'user': 'c-1', 'server': 'coopens.com'})
# result = ejabberdctl('get_last', {'user': 'zyf', 'host': 'coopens.com'})
print result



# https://github.com/processone/ejabberd/issues/845
# server_url = 'http://42.96.194.60:4560'
# server = xmlrpclib.ServerProxy(server_url)
#
# EJABBERD_XMLRPC_LOGIN = {'user': 'zyf', 'server': 'coopens.com', 'password': '123456', 'admin': "true"}
#
# def calling(command, data):
#     fn = getattr(server, command)
#     return fn(EJABBERD_XMLRPC_LOGIN, data)
#
# print ""
# print "Calling with auth details:"
# result = calling('get_roster', {'user':'zyf', 'server':'coopens.com'})
# print result




## [关于xmlrpclib研究](http://www.dongwm.com/archives/guanyuxmlrpclibyanjiu/)
## [Python的XMLRPC简介及小技巧](http://hgoldfish.com/blogs/article/50/)
## [SimpleXMLRPCServer — Basic XML-RPC server](https://docs.python.org/2/library/simplexmlrpcserver.html)
## [xmlrpclib — XML-RPC client access](https://docs.python.org/2/library/xmlrpclib.html)