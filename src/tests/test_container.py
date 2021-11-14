from models import Container

def test_init_and_getters():
    container = Container("Myid", "MyName", "MyStatus", "MyCreatedOn", "MyImage")

    assert container.get_id() == "Myid"
    assert container.get_name() == "MyName"
    assert container.get_status() == "MyStatus"
    assert container.get_created_on() == "MyCreatedOn"
    assert container.get_image() == "MyImage"

def test_setters():
    container = Container("Myid", "MyName", "MyStatus", "MyCreatedOn", "MyImage")

    assert container.get_name() == "MyName"

    container.set_name("ChangedName")

    assert container.get_name() == "ChangedName"