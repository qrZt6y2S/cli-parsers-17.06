# -*- coding: utf-8 -*-
from .exceptions import NotEnoughLinesError


def double_space_split(in_str):
    return [res.strip() for res in in_str.split('  ') if res]


def parse_cmd_output(in_text, columns_count):
    lines = in_text.strip().splitlines()
    lines_count = len(lines)

    if lines_count < 2:
        raise NotEnoughLinesError('lines == {0} (expected >= 2)'.format(lines_count))
    elif lines_count == 2:
        result = []
    else:
        headers = double_space_split(lines[0])
        assert len(headers) == columns_count

        result = []

        for line in lines[2:]:
            values = double_space_split(line)
            assert len(values) == columns_count

            result.append(dict(zip(headers, values)))

    return result
