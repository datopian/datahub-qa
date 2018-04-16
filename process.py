#!/usr/bin/env python3
"""
This script counts number of issues in the github repository
on the current date and updates 'data/issues.csv' file.

Run it daily to have the actual information
"""
import os
import csv
import requests
from pprint import pprint
from datetime import datetime, timedelta


# github API docs https://developer.github.com/v3/issues/#list-issues-for-a-repository
API = "https://api.github.com/repos/datahq/datahub-qa/issues"
# script will get and count issues with the given labels:
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
# script will get and count issues with the given labels:
labels_to_track = [
    'Severity: Critical',
    'Severity: Major',
    'Severity: Minor',
    'Severity: Trivial',
    'NEW FEATURE'
]
# path to save the data
path = 'data/issues.csv'


def count_open_issues(label):
    print('get "%s" issues' % label, end=" ... ")
    r = requests.get(API, params={'labels': label, 'access_token': GITHUB_TOKEN})
    issues = r.json()
    print(len(issues))
    return len(issues)


def count_closed_last_24h():
    print('get issues, closed last 24h', end=' ... ')
    r = requests.get(API, params={
        'state': 'closed',
        'since': str(datetime.now() - timedelta(days=1))
    })

    # filter Duplicated issues
    """ API response structure (non-sensitive info excluded):
    [
        issue{..., "labels": [{"name": "duplicate",...},...],...},
        issue{},
        ...
    ]
    """
    issues_num = 0
    for issue in r.json():
        try:
            labels = [l['name'] for l in issue['labels']]
        except:  # sometimes response is not correct, let's see it
            print('Something wrong with the response:')
            pprint(r.json())
            exit(1)

        if 'duplicate' not in labels and 'invalid' not in labels:
            issues_num += 1
    print(issues_num)
    return issues_num


def main():
    """
    date, label1, label2, ..., closed
    """
    headers = [
        'date',
        *[l.replace('Severity: ', '') for l in labels_to_track],
        'closed'
    ]
    data = [
        datetime.now().date(),
        *[count_open_issues(l) for l in labels_to_track],
        count_closed_last_24h()
    ]

    if not os.path.isfile(path):
        with open(path, 'w') as file:
            csv.writer(file).writerow(headers)

    with open(path, 'a') as file:
        csv.writer(file).writerow(data)

    print(path, 'is updated.')


if __name__ == "__main__":
    main()
