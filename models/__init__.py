#!/usr/bin/python3
"""FileStorage instance for application"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
