# -*- coding: utf-8 -*-


class CliParsersBaseError(StandardError):
    """Base error for CliParsers"""


class NotEnoughLinesError(CliParsersBaseError):
    """Not enough lines for parsing"""
