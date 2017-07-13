#!/bin/python
#
# https://docs.python.org/2.7/
# based on https://github.com/zag2me/plugin.audio.example/blob/master/default.py
#
# Author: M de Jong
# 2017

import urllib
import urllib2
import urlparse
import sys
import os
import xbmcgui
import xbmcplugin
import xbmcaddon

# set global vars
url = ''

# player defnition
def player(url):
    # set the path of the song to a list item
    play_item = xbmcgui.ListItem(path=url)
    # the list item is ready to be played by Kodi
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)


if __name__ == '__main__':
    url = 'http://stream2.rhr.fm'
    #addon_handle = int(sys.argv[1])
    player()
