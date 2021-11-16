from config import Client

def test_create_and_delete_container():
    test_container = Client.containers.run("hello-world", detach=True)
    all_containers = Client.containers.list(all)
    assert any(container.name == test_container.name for container in all_containers) == True

    Client.containers.get(test_container.id).remove(force=True)

    assert any(container.name == test_container.name for container in all_containers)
