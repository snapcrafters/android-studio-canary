#!/usr/bin/python3

import re
import urllib.request

URL_STUDIO_HOME = 'https://developer.android.com/studio/preview/'


def get_latest_studio_url():
    with urllib.request.urlopen(URL_STUDIO_HOME) as response:
        html = response.read().decode()

    matched = re.findall('"((https)?://.*linux.zip)"', html)
    # Ensure unique and then convert to a list of easy access.
    links = list(set(matched))

    if len(links) == 0:
        raise ValueError('Url matching our query not found.')
    elif len(links) > 2:
        raise RuntimeError('More than two urls found, expected two, urls are: {}'.format(
            ' '.join([link[0] for link in links])))

    url1 = links[0][0]
    version1 = url1.split('/')[-2]

    url2 = links[1][0]
    version2 = url2.split('/')[-2]

    version1_broken = list(map(int, version1.split('.')))
    version2_broken = list(map(int, version2.split('.')))

    for i in range(len(version1_broken)):
        if version1_broken[i] > version2_broken[i]:
            return version1, url1
        elif version1_broken[i] < version2_broken[i]:
            return version2, url2
    return version1, url1


if __name__ == '__main__':
    print(' '.join(get_latest_studio_url()))
