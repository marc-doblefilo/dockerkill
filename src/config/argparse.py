import argparse

argParser = argparse.ArgumentParser(
        description='Clean your beautiful docker lists',
        prog='dockerkill',
        usage='%(prog)s [OPTIONS]'
        )

argParser.add_argument(
        '-c', '--containers',
        help='Select containers to be deleted',
        action='store_true'
        )

argParser.add_argument(
        '-i', '--images',
        help='Select images to be deleted',
        action='store_true'
        )
