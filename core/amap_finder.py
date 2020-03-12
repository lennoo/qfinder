#{{{-----------------------------------------------------------
#
# QGIS Quick Finder Plugin
# Copyright (C) 2014 Denis Rouzaud, Arnaud Morvan
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------}}}

from builtins import str
import urllib,json

from qgis.core import QgsGeometry
from .http_finder import HttpFinder
from . import geochina


class AmapFinder(HttpFinder):

    name = 'amap'

    def __init__(self, parent):
        HttpFinder.__init__(self, parent)

    def start(self, to_find, bbox=None):
        super(AmapFinder, self).start(to_find, bbox)

        url = self.settings.value('amapUrl')
        o = urllib.parse.urlsplit(url)
        url = urllib.parse.urlunsplit((o.scheme,o.netloc,o.path,'',''))     #ampa query base url
        params = dict(urllib.parse.parse_qsl(o.query))
        default_params = {
            'keywords': to_find,
            'city': 330327, # wenzhou, chinese code
            'types':    '',
            'format'       : 'json',
            'offset'        : '25',
            'children': 1,
            'page': '1',
        }
        params = {**default_params, **params}
        self._sendRequest(url, params)

    def load_data(self, data):
        print(data)
        pois = data['pois']
        for p in pois:
            lng, lat = p['location'].split(',')
            lng, lat = geochina.gcj02_to_wgs84(float(lng), float(lat))
            wkt = f'POINT({lng} {lat})'
            geometry = QgsGeometry.fromWkt(wkt)
            self.result_found.emit(self,
                                  p['type'],
                                  p['name'],
                                  geometry,
                                  4326)
        self._finish()
#        for d in data:
#            try:
#                wkt = d['geotext']
#            except KeyError:
#                wkt = 'POINT(%s %s)' % (d['lon'], d['lat'])
#            geometry = QgsGeometry.fromWkt(wkt)
#            self.result_found.emit(self,
#                                  d['type'],
#                                  d['display_name'],
#                                  geometry,
#                                  4326)
#        self._finish()
