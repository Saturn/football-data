import json

import requests


fd_url = "https://www.football-data.org"
invalid_api_message = ("You must have an API token."
                       " Get one from {}.".format(fd_url))


class InvalidAPIKey(Exception):
    pass


class RestrictedResource(Exception):
    pass


class TooManyRequests(Exception):
    pass


class ResourceNotFound(Exception):
    pass


class BadRequest(Exception):
    pass


def check_response(response):
    code = response.status_code
    if code == 429:
        throttling_url = 'https://www.football-data.org/documentation/api#request-throttling'
        raise TooManyRequests('You have exceeded request quote. See {}'.format(throttling_url))
    if code == 403:
        raise RestrictedResource('Resource is restricted.')
    if code == 404:
        raise ResourceNotFound('You tried to access resource that doesn\'t exist')
    if code == 400:
        raise BadRequest('Your request was malformed')


class FootballData:
    def __init__(self, auth_token=None):
        with open('config.json') as f:
            self.config = json.load(f)

        self.base_url = self.config.get('base_url')
        if auth_token:
            self.auth_token = auth_token
        else:
            self.auth_token = self.config.get('auth_token')

        if self.auth_token == 'YOUR_AUTH_TOKEN':
            raise InvalidAPIKey(invalid_api_message)
        self.headers = {'X-Auth-Token': self.auth_token}

    def get_competitions(self):
        rv = requests.get(self.base_url + 'competitions/', headers=self.headers)
        check_response(rv)
        return rv.json()

    def get_competition(self, id):
        rv = requests.get(self.base_url + 'competitions/' + str(id),
                          headers=self.headers)
        check_response(rv)
        return rv.json()

    def get_competition_teams(self, id, season=None):
        rv = requests.get(self.base_url + 'competitions/' + str(id) + '/matches',
                          params={'season': season},
                          headers=self.headers)
        check_response(rv)
        return rv.json()

    def get_competition_standings(self, id):
        rv = requests.get(self.base_url + 'competitions/' + str(id) + '/standings',
                          headers=self.headers)
        check_response(rv)
        return rv.json()

    def get_competition_scorers(self, id):
        rv = requests.get(self.base_url + 'competitions/' + str(id) + '/scorers',
                          headers=self.headers)
        check_response(rv)
        return rv.json()

    def get_match(self, competitions=None, status=None,
                  stage=None, group=None, dateFrom=None, dateTo=None):
        rv = requests.get(self.base_url + 'matches',
                          params=dict(competitions=competitions,
                                      status=status,
                                      stage=stage,
                                      group=group,
                                      dateFrom=dateFrom,
                                      dateTo=dateTo),
                          headers=self.headers)
        check_response(rv)
        return rv

    def get_teams(self, competition=None):
        if competition:
            url = 'competitions/' + str(competition) + '/teams'
        else:
            url = '/teams'
        rv = requests.get(self.base_url + url,
                          headers=self.headers)
        return rv.json()
