# -*- coding: utf-8 -*-


class CliParsersBaseError(StandardError):
    """Base error for CliParsers"""


class NotEnoughLinesError(CliParsersBaseError, ValueError):
    """Not enough lines for parsing"""
