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

from abc import ABCMeta, abstractmethod


class PluginSlide(metaclass=ABCMeta):
    @abstractmethod
    def get_duration(self):
        """ Returns the slide duration as integer milliseconds. """
        pass

    @abstractmethod
    def get_content(self):
        """
            Returns the slide content as a dictionary in the form
                {
                    '[field-type]-[field-number]': {'[input-type]': '[field-data]'},
                    ...
                }
            Please consult the documentation for a complete explanation of this dictionary.
        """
        pass

    @abstractmethod
    def get_template(self) -> str:
        """ Returns the name of the template without any file extension. """
        pass
