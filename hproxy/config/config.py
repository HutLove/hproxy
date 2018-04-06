#!/usr/bin/env python
"""
 Created by howie.hu at 06/04/2018.
"""
import os


class Config():
    """
    Basic config for hproxy
    """

    # Application config
    VAL_HOST = os.getenv('VAL_HOST', 'true')
    HOST = ['127.0.0.1:8001', '0.0.0.0:8001', '127.0.0.1:8002', '0.0.0.0:8002']
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

    DB_TYPE = 'memory'
