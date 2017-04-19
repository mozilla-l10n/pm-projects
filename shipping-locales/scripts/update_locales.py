#! /usr/bin/env python

import os
import urllib


def main():
    update_sources = {
        'nightly': {
            'android-multi': 'http://hg.mozilla.org/mozilla-central/raw-file/default/mobile/android/locales/maemo-locales',
            'android-single': 'http://hg.mozilla.org/mozilla-central/raw-file/default/mobile/android/locales/all-locales',
            'desktop': 'http://hg.mozilla.org/mozilla-central/raw-file/default/browser/locales/all-locales'
        },
        'beta': {
            'android-multi': 'http://hg.mozilla.org/releases/mozilla-beta/raw-file/default/mobile/android/locales/maemo-locales',
            'android-single': 'http://hg.mozilla.org/releases/mozilla-beta/raw-file/default/mobile/android/locales/all-locales',
            'desktop': 'http://hg.mozilla.org/releases/mozilla-beta/raw-file/default/browser/locales/shipped-locales'
        },
        'release': {
            'android-multi': 'http://hg.mozilla.org/releases/mozilla-release/raw-file/default/mobile/android/locales/maemo-locales',
            'android-single': 'http://hg.mozilla.org/releases/mozilla-release/raw-file/default/mobile/android/locales/all-locales',
            'desktop': 'http://hg.mozilla.org/releases/mozilla-release/raw-file/default/browser/locales/shipped-locales'
        }
    }

    # Get absolute path of ../sources from current script location (not current folder)
    locales_folder = os.path.abspath(
        os.path.join(os.path.dirname( __file__ ),
        os.pardir,
        'locales')                    )

    for channel_id, update_source in update_sources.iteritems():
        for product, url in update_source.iteritems():
            filename = os.path.join(locales_folder, '{0}-{1}.txt'.format(channel_id, product))
            print 'Storing sources for {0} to {1}'.format(channel_id, filename)
            try:
                urllib.urlretrieve(url, filename)
            except Exception as e:
                print e


if __name__ == '__main__':
    main()
