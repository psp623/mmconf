# Copyright (c) OpenMMLab. All rights reserved.
from mmconf.utils import is_list_of
from .base import BaseFileHandler
from .json_handler import JsonHandler
from .yaml_handler import YamlHandler
from .toml_handler import TomlHandler

file_handlers = {
    'json': JsonHandler(),
    'yaml': YamlHandler(),
    'yml': YamlHandler(),
    'toml': TomlHandler(),
}


def _register_handler(handler, file_formats):
    """Register a handler for some file extensions.

    Args:
        handler (:obj:`BaseFileHandler`): Handler to be registered.
        file_formats (str or list[str]): File formats to be handled by this
            handler.
    """
    if not isinstance(handler, BaseFileHandler):
        raise TypeError(
            f'handler must be a child of BaseFileHandler, not {type(handler)}')
    if isinstance(file_formats, str):
        file_formats = [file_formats]
    if not is_list_of(file_formats, str):
        raise TypeError('file_formats must be a str or a list of str')
    for ext in file_formats:
        file_handlers[ext] = handler


def register_handler(file_formats, **kwargs):

    def wrap(cls):
        _register_handler(cls(**kwargs), file_formats)
        return cls

    return wrap
