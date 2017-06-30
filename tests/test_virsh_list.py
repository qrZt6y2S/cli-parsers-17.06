# -*- coding: utf-8 -*-
from pytest import raises

from cli_parsers.virsh_list import parse_cmd_output as parse_virsh_list_output
from cli_parsers.exceptions import NotEnoughLinesError


# ----------------------------------------------------------------

out01 = ("""
 Id    Name                           State
""")

out02 = ("""
 Id    Name                           State
----------------------------------------------------
""")

out03 = ("""
 Id    Name                           State
----------------------------------------------------
 3     instance-000003db              running
 4     instance-0000047a              running
""")

out04 = ("""
 Id    Name                           State
----------------------------------------------------
 3     instance-000003db              running
 -     instance-00000015              shut off
""")

# ----------------------------------------------------------------


def test_parse_virsh_list_out01():
    with raises(NotEnoughLinesError, message="Expecting NotEnoughLinesError"):
        parse_virsh_list_output(out01, 3)


def test_parse_virsh_list_out02():
    assert parse_virsh_list_output(out02, 3) == []


def test_parse_virsh_list_out03():
    res_list = [
        {
            'Id': '3',
            'Name': 'instance-000003db',
            'State': 'running',
        },
        {
            'Id': '4',
            'Name': 'instance-0000047a',
            'State': 'running',
        }
    ]

    assert parse_virsh_list_output(out03, 3) == res_list


def test_parse_virsh_list_out04():
    res_list = [
        {
            'Id': '3',
            'Name': 'instance-000003db',
            'State': 'running',
        },
        {
            'Id': '-',
            'Name': 'instance-00000015',
            'State': 'shut off',
        }
    ]

    assert parse_virsh_list_output(out04, 3) == res_list
