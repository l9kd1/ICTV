# -*- coding: utf-8 -*-
#
#    This file belongs to the ICTV project, written by Nicolas Detienne,
#    Francois Michel, Maxime Piraux, Pierre Reinbold and Ludovic Taffin
#    at Université catholique de Louvain.
#
#    Copyright (C) 2016-2018  Université catholique de Louvain (UCL, Belgium)
#
#    ICTV is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ICTV is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with ICTV.  If not, see <http://www.gnu.org/licenses/>.

import web
from sqlobject import SQLObjectNotFound

from ictv.models.screen import ScreenMac
from ictv.pages.utils import ICTVPage


class ScreenRouter(ICTVPage):
    def get(self, mac):
        """ Redirects a screen with its given mac to its secret link. """
        try:
            screen = ScreenMac.selectBy(mac=mac).getOne().screen
        except SQLObjectNotFound:
            raise web.notfound()
        raise web.seeother(screen.get_view_link())
