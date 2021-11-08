#!/usr/bin/env python3
# -*- coding: utf8 -*-

# Copyright (c) 2021 Birnadin Erick

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
    Maiden File

    This module contains maiden class. This class should be used to talk or 
    walk the aria2c(addressed as engine). Name "MAIDEN" describes what this 
    does. This does everything associated with aria2c. This is the only 
    module straightly interfaces with engine. Every other components of 
    ```aria2me``` should use this module to keep coupling minimal as 
    possible.

    ```Maiden``` follows OOP[with pinch of functional programming for 
    utility works]. ```Maiden``` tries to utilize built-in python3(3.8) 
    library to minimize dependent on third-party library. If any library 
    throws error, first check for version compatobility. 
    ***```Maiden``` was developed in Ubuntu 20.04 with python 3.8***.
    If you encounter any incompatibility due to different versions please 
    open an issue.

    ```Maiden``` is inspired by Aria2JsonRpc.py from **python3-aria2jsonrpc**
    # project url: http://xyne.archlinux.ca/projects/python3-aria2jsonrpc'
    # author: Xyne (enyx.xunilhcra.ac) [not sure -\(*_*)/-]
    # license: GNU GENERAL PUBLIC LICENSE Version 2, June 1991
    # changlog last entry date: 2019-12-30

    ***Note***: ```Maiden``` should be singleton in a process. Though it is 
                not tested but being singleton in a thread is also ok.
"""

# _________________ IMPORTS _________________________________________________

try:
    import http.client
    import json
    import logging
    import math
    import os
    import subprocess
    import sys
    import time
    import urllib.parse as _parse
    import urllib.request as _requets
except Exception as e:
    # TODO: raise custom exception and log
    pass
else:
    pass

# _________________ GLOBAL CONFIG ___________________________________________

try:
    stage = os.getenv("STAGE") or "DEBUG"
    logging.basicConfig(
        format="[%(name)s] @ %(asctime)s %(levelname)s: %(message)s",
        datefmt="%b %d, %Y %H:%M",
        level=(logging.INFO if stage=="PROD" else logging.DEBUG)
        )
    para = True if os.getenv("PARA") == 1 else False
except Exception as e:
    # TODO: raise custom exception and log
    pass
else:
    # TODO: log succeed
    pass

# _________________ CONSTANTS _______________________________________________

try:
    PORT:int = 6800
    NGIN:str = "{}://{}:{:d}/jsonrpc"
    LOGGER = logging.getLogger(name="aria2me.backend.maiden")
except Exception as e:
    # TODO: raise custom exception and log
    pass
else:
    pass


# _________________ MAIDEN __________________________________________________

class Maiden(object):
    pass
