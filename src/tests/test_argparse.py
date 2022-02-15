from config import argParser

def test_container_value():
    args = argParser.parse_args('-c'.split())

    assert getattr(args, 'containers') == True

def test_images_value():
    args= argParser.parse_args('-i'.split())

    assert getattr(args, 'images') == True
