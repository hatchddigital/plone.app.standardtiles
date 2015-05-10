# -*- coding: utf-8 -*-
from plone.app.standardtiles import PloneMessageFactory as _
from plone.supermodel.model import Schema
from plone.tiles import Tile
from zope import schema

import re


class IVideoTile(Schema):
    """Video tile."""

    youtubeURL = schema.TextLine(title=_(u"Youtube URL"), required=True)


class VideoTile(Tile):
    """A tile that displays a youtube movie. Purely as a proof of concept and
    to showcase possibilities of Deco."""

    def __call__(self):
        youtubeURL = self.data.get('youtubeURL')
        youtubeID = re.split('v=([A-Za-z00-9_\-]+)', youtubeURL)[1]

        return '<html><body><object width="425" height="344"><param ' \
               'name="movie" value="http://www.youtube.com/v/%s&hl=en_GB&fs=' \
               '1&"></param><param name="allowFullScreen" value="true">' \
               '</param><param name="allowscriptaccess" value="always">' \
               '</param><embed src="http://www.youtube.com/v/%s&hl=en_GB&fs=' \
               '1&" type="application/x-shockwave-flash" allowscriptaccess=' \
               '"always" allowfullscreen="true" width="425" height="344">' \
               '</embed></object></body></html>' % (youtubeID, youtubeID)
