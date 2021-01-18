#!/usr/bin/python3

from bs4 import BeautifulSoup
import re
import urllib.request

URL_STUDIO_HOME = 'https://developer.android.com/studio/preview/index.html'

def get_latest_studio_url():
    with urllib.request.urlopen(URL_STUDIO_HOME) as response:
        html = response.read().decode()

    bs = BeautifulSoup(html, "html.parser")
    result = bs.find('a', {'data-category': 'canary_linux_bundle_download', 'data-action': 'download'})

    if result is None:
        raise ValueError('Url matching our query not found.')

    url = result['href']
    version = url.split('/')[-2]

    return version, url


if __name__ == '__main__':
    print(' '.join(get_latest_studio_url()))
