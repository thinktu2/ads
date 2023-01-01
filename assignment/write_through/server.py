from sim_file import sim_file

class sim_server:
    def __init__(self):
        self._server_file = {}

    def _search_server(self,file_name):
        return file_name in self._server_file

    def get_version(self, file_name):
        _,_,version = self.read(file_name)
        return version

    def write(self,file_name,data,version):
        if self._search_server(file_name):
            self._server_file[file_name].write_data(data,version)
        else:
            self._server_file[file_name] = sim_file(file_name,data,version)
        
    def read(self,file_name):
        if self._search_server(file_name):
            return self._server_file[file_name].get_data()
        else:
            return None
