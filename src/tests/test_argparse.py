from config import argParser

def test_container_value():
    args = argParser.parse_args('-c'.split())

    assert getattr(args, 'containers') == True
