# _*_ coding: utf8 _*_
# !/usr/bin/env python
__author__ = 'TranTien'
import re
import dateparser

class CleanTime:
    def __init__(self):
        pass

    def clean_date(self, date):
        if date is not None:
            m = re.search(r'\d{4}-\d{1,2}-\d{1,2}', date)
            if m is not None:
                date = m.group()

        if date is not None:
            m = re.search(r'\d{1,2}/\d{1,2}/\d{4}', date)
            if m is not None:
                date = m.group()

        if date is not None:
            m = re.search(r'\w+\s+\d{1,2},\s+\d{4}', date)
            if m is not None:
                date = m.group()

        if date is not None:
            m = re.search(r'\d+\s+\w+\s+\d{4}', date)
            if m is not None:
                date = m.group()

        if date is not None:
            m = re.search(r'\w+\s+\d+\w{1,3},\s+\d{4}', date)
            if m is not None:
                date = m.group()

        if date is not None:
            m = re.search(r'\w+\.\s+\d+,\s+\d{4}', date)
            if m is not None:
                date = m.group()

        if date is not None:
            m = re.search(r'\w+\s+\d+\s+\d{4}', date)
            if m is not None:
                date = m.group()

        if date is not None:
            m = re.search(r'\d{1,2}\.\d{1,2}\.\d{4}', date)
            if m is not None:
                date = m.group()
        try:
            date = dateparser.parse(date)
            return date
        except Exception as e:
            print('loi parser date', e)
            return date
