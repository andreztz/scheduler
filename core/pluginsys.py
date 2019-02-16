import importlib

PLUGIN_NAME = "plugins.sms plugins.mail plugins.notify".split(" ")

PLUGINS = []
for plug in PLUGIN_NAME:
    PLUGINS.append(importlib.import_module(plug, "."))
