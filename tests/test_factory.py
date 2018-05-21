# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:23:32 2018

@author: johnc
"""

from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'