# -*- coding: utf-8 -*-
"""
    hooks.up2local
    ~~~~~~~~~~~~~~

    Save uploaded pictures locally.

    :copyright: (c) 2019 by staugur.
    :license: BSD 3-Clause, see LICENSE for more details.
"""

__version__ = '0.2.1'
__author__ = 'staugur'
__description__ = '将图片保存到本地'
__catalog__ = 'upload'

from os import makedirs, remove
from os.path import exists, join, isfile
from utils._compat import string_types


def upimg_save(**kwargs):
    res = dict(code=1)
    try:
        filename = kwargs["filename"]
        stream = kwargs["stream"]
        upload_path = kwargs.get("upload_path") or ""
        local_basedir = kwargs["local_basedir"]
        if not filename or not stream or not local_basedir:
            return ValueError
    except (KeyError, ValueError):
        res.update(msg="Parameter error")
    else:
        if isinstance(upload_path, string_types):
            if upload_path.startswith("/"):
                upload_path = upload_path.lstrip('/')
            saveto = join(local_basedir, upload_path)
            if not exists(saveto):
                makedirs(saveto)
            filepath = join(saveto, filename)
            with open(filepath, "wb") as fp:
                fp.write(stream)
                res.update(code=0)
        else:
            res.update(msg="The upload_path type error")
    return res


def upimg_delete(sha, upload_path, filename, basedir, save_result):
    filepath = join(basedir, upload_path, filename)
    if isfile(filepath):
        remove(filepath)
