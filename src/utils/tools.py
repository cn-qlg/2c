#!/usr/bin/env python
"""
    Created by howie.hu at 2021/4/7.
    Description：通用函数
    Changelog: all notable changes to this file will be documented
"""

import hashlib


def md5_encryption(string: str) -> str:
    """
    对字符串进行md5加密
    :param string: 加密目标字符串
    :return:
    """
    m = hashlib.md5()
    m.update(string.encode("utf-8"))
    return m.hexdigest()


def is_contain_text(text: str, text_list: list) -> bool:
    """
    判断输入的本文是否被文本列表包含
    :param text: 文本
    :param text_list: 文本列表
    :return:
    """
    if text:
        for each in text_list:
            if each in text:
                return True
    return False


def load_text_to_list(file_path) -> list:
    """
    加载文本返回列表
    :param file_path:
    :return:
    """
    text_list = []
    with open(file_path, encoding="utf-8") as fp:
        for line in fp:
            line = line.replace("\n", "").strip()
            if line:
                text_list.append(line)
    return text_list
