class Container:
    _id: str
    _name: str
    _status: str
    _created_on: str
    _image: str

    def __init__(self, id, name, status, created_on, image):
        self._id = id
        self._name = name
        self._status = status
        self._created_on = created_on
        self._image = image

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_status(self):
        return self._status

    def get_created_on(self):
        return self._created_on
    
    def get_image(self):
        return self._image

    def set_id(self, id: str):
        self._id = id

    def set_name(self, name: str):
        self._name = name
    
    def set_status(self, status: str):
        self._status = status
    
    def set_created_on(self, created_on: str):
        self._created_on = created_on

    def set_image(self, image: str):
        self._image = image