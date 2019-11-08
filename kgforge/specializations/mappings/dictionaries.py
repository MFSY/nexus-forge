# 
# Knowledge Graph Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Knowledge Graph Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
# General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Knowledge Graph Forge. If not, see <https://www.gnu.org/licenses/>.

from collections import OrderedDict
from pathlib import Path

import hjson

from kgforge.core.commons.attributes import sort_attributes
from kgforge.core.commons.typing import FilePath
from kgforge.core.transforming.mapping import Mapping


class DictionaryMapping(Mapping):

    def __init__(self, mapping: str) -> None:
        super().__init__(mapping)

    @staticmethod
    def load(path: FilePath) -> "DictionaryMapping":
        text = Path(path).read_text()
        return DictionaryMapping(text)

    def _load_rules(self, mapping: str) -> OrderedDict:
        return hjson.loads(mapping)

    def _normalize_rules(self, rules: OrderedDict) -> str:
        return hjson.dumps(rules, indent=4, item_sort_key=sort_attributes)
