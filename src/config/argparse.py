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

argParser.add_argument(
        '-o', '--older',
        help='Number of months that a container/image need to be older than to be deleted',
        action='store',
        nargs='?',
        default=argparse.SUPPRESS,
        type=int,
        metavar='MONTHS'
        )
