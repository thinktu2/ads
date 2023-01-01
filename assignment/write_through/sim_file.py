class sim_file:
    def __init__(self,file_name, data, version = 0):
        self._file_name = file_name
        self._data = data
        self._version = version

    def write_data(self,data,version):
        self._data = data
        self._version = version

    def get_data(self):
        return self._file_name ,self._data,self._version

    def get_versoin(self):
        return self._version
