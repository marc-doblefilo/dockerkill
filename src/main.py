from config import Client, argParser

args = argParser.parse_args()

if getattr(args, 'containers') == True:
    containers = Client.containers.list(all=True, before=getattr(args, 'since'))
    print(containers)
    print(len(containers))
