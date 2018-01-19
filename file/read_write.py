#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Author:lthan
# @Email :xiaohan809@qq.com
# @Time  :2018/1/19 12:03
class Read(object):
    def __init__(self):
        pass
    def readlines(self,file_name,strip=None,sep=None,decode=None,encode=None):
        '''
        逐行读取
        :param file_name: 文件名
        :param strip: 去除两端的字符
        :param sep:分隔符
        :param decode:解码
        :param encode:编码
        :return:逐行返回
        '''
        with open(file_name,'r') as fr:
            for line in fr:
                if decode:
                    assert type(decode) == str,'参数decode应该为字符串类型'
                    line = line.decode(decode,'ignore')
                if encode:
                    assert type(encode) == str, '参数encode应该为字符串类型'
                    line = line.encode(encode, 'ignore')
                if strip:
                    assert type(strip) == str, '参数strip应该为字符串类型'
                    line = line.strip(strip)
                if sep:
                    line = line.split(sep)
                yield line

    def read(self,file_name,strip=None,sep=None,decode=None,encode=None):
        '''
        返回list格式数据
        :param file_name: 文件名
        :param strip: 去除两端的字符
        :param sep: 分隔符
        :param decode: 解码
        :param encode: 编码
        :return: 返回list
        '''
        ret_list = []
        with open(file_name,'r') as fr:
            for line in fr:
                if decode:
                    assert type(decode) == str,'参数decode应该为字符串类型'
                    line = line.decode(decode,'ignore')
                if encode:
                    assert type(encode) == str, '参数encode应该为字符串类型'
                    line = line.encode(encode, 'ignore')
                if strip:
                    assert type(strip) == str, '参数strip应该为字符串类型'
                    line = line.strip(strip)
                if sep:
                    line = line.split(sep)
                ret_list.append(line)
        return ret_list

class Write(object):
    def __init__(self):
        pass
    def write(self,data,file_name,conn=None,end='\n'):
        with open(file_name,'w') as fw:
            for line in data:
                print line
                if conn:
                    assert type(conn) == str, '参数conn应该为字符串类型'
                    print str(line)
                    line = conn.join([str(val) for val in line])
                if end:
                    assert type(end) == str,"参数end应该为字符串类型"
                    fw.write(line)
                    fw.write(end)



