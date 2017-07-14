# -*- coding: utf-8 -*-
import logging
# try:
#     try:
#         ccfile = open('carddata.txt')
#         txns = ccfile.readlines()
#     except IOError:
#         log.write('no txns this month\n')
# finally:
#     ccfile.close()

#方式2
try:
    try:
        ccfile = open('carddata.txt')
        txns = ccfile.readlines()
    finally:
        ccfile.close()
except IOError:
    log.write('no txns this month\n')