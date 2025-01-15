"""Support custom filters for jinja2 templating"""
import ast
import base64
import json
import re
import urllib.parse
import zlib
import logging

from homeassistant.helpers import template

_LOGGER = logging.getLogger(__name__)

_TemplateEnvironment = template.TemplateEnvironment


## -- REPLACE ALL
def setattr(dictionary, key, value):
    dictionary[key] = value
    return dictionary



def init(*args):
    """Initialize filters"""
    env = _TemplateEnvironment(*args)
    env.filters["dictionary"] = dictionary
    return env


template.TemplateEnvironment = init
template._NO_HASS_ENV.filters["dictionary"] = dictionary


async def async_setup(hass, hass_config):
    tpl = template.Template("", template._NO_HASS_ENV.hass)
    tpl._env.globals = set_dict_value
    return True
