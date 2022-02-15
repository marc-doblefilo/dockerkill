from config import Client

for container in Client.containers.list(all):
    print(container.name)
