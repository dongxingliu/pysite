#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : regexp.py
# @Author: Feng
# @Date  : 2018/10/11
# @Desc  :

import sys
import re
result = re.findall('[0-9]*', "0912ab123")


print(result)

print(sys.version)
