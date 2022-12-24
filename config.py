# Anki 2.1.x add-on to adjust the sound volume
# Copyright (C) 2021  Muneyuki Noguchi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
Handle the volume configurations
"""
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Type

from aqt import mw


@dataclass
class LoudnormConfig:
    """The loudnorm filter configuration"""
    enabled: bool = False
    i: int = -24
    dual_mono: bool = False
    ignored_files: List[str] = field(default_factory=list)


@dataclass
class VolumeConfig:
    """The volume configuration"""
    volume: int = 100
    loudnorm: LoudnormConfig = field(default_factory=LoudnormConfig)


def load_value(config: Dict[str, Any], key: str, type_: Type) -> Any:
    if key in config and isinstance(config[key], type_):
        return config[key]

    return None


def load_config() -> VolumeConfig:
    """Load the sound volume configuration."""
    volume_config = VolumeConfig()

    if mw is None:
        return volume_config

    config = mw.addonManager.getConfig(__name__)
    if config is None:
        return volume_config

    value = load_value(config, 'volume', int)
    if value is not None:
        volume_config.volume = value

    if 'loudnorm' not in config:
        return volume_config

    loudnorm_config = config['loudnorm']

    value = load_value(loudnorm_config, 'enabled', bool)
    if value is not None:
        volume_config.loudnorm.enabled = value

    value = load_value(loudnorm_config, 'i', int)
    if value is not None:
        volume_config.loudnorm.i = value

    value = load_value(loudnorm_config, 'dual_mono', bool)
    if value is not None:
        volume_config.loudnorm.dual_mono = value

    value = load_value(loudnorm_config, 'ignored_files', list)
    if value is not None:
        volume_config.loudnorm.ignored_files = value

    return volume_config
