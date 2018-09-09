# -*- coding: utf-8 -*-

"""Main module."""
import os
import requests


class TokenError(BaseException):
    """ No token passed to client """


class Resource:
    """ An Abstract REST Resource """
    PATH = None
    BASE_URL = 'https://api.loadlab.co/v1'

    def __init__(self, token):
        self.headers = {
            'Authorization': f'Token {token}',
            'Accept': 'application/json',
        }

    def get(self):
        return requests.get(self.BASE_URL + self.PATH, headers=self.headers).json()

    def create(self, **data):
        return requests.post(self.BASE_URL + self.PATH, data=data, headers=self.headers).json()


class Plans(Resource):
    PATH = '/plans/'


class Jobs(Resource):
    PATH = '/jobs/'


class Sites(Resource):
    PATH = '/sites/'


class LoadLab:

    def __init__(self, token: str = None):
        self.token = token or os.getenv('LOADLAB_API_TOKEN')
        if not self.token:
            raise TokenError('Missing environment variable `LOADLAB_API_TOKEN`')
        self.jobs = Plans(self.token)
        self.plans = Plans(self.token)
        self.sites = Sites(self.token)
