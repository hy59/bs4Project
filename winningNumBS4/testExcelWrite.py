# -*- coding: utf-8 -*-
'''
Created on 2017.04.11
@Author: wujiu
'''

import xlwt


if __name__ == '__main__':
    book = xlwt.Workbook(encoding='utf8', style_compression=0)
    sheet = book.add_sheet('dede')
    sheet.write(0, 0, 'wujiu')
    sheet.write(1, 1, u'中文测试'.encode('utf8'))
    book.save('d:\\1.xls')
