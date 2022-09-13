#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'


class Employee(object):

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def set_salary(self, salary):
        self._salary = salary

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary

    def get_name(self):
        return self._name

