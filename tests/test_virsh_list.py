# -*- coding: utf-8 -*-

from cli_parsers.virsh_list import parse_cmd_output as parse_virsh_list_output


out01 = ("""
 Id    Name                           State
----------------------------------------------------
 3     instance-000003db              running
 4     instance-0000047a              running
""")

out02 = ("""
 Id    Name                           State
----------------------------------------------------
 3     instance-000003db              running
 -     instance-00000015              shut off
""")

out88 = ("""
 Id    Name                           State
----------------------------------------------------
 3     instance-000003db              running
 4     instance-0000047a              running
 28    instance-000009f3              running
 29    instance-00000a0b              running
 30    instance-000009f6              running
 31    instance-00000a02              running
 -     instance-00000015              shut off
""")


def test_parse_virsh_list_output():
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

    assert parse_virsh_list_output(out01, 3) == res_list


def test_parse_virsh_list_output02():
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

    assert parse_virsh_list_output(out02, 3) == res_list
