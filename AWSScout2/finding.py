#!/usr/bin/env python2

class Finding():

    def __init__(self, description, name, entity, callback, callback_args, idprefix, level):
        self.description = description
        self.name = name
        self.level = level
        self.entity = entity
        self.callback = callback
        self.callback_args = callback_args,
        self.idprefix = idprefix
        self.level = level
        self.items = []
        self.macro_items = []