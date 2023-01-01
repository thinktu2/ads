import time
from sim_file import sim_file
from server import sim_server

class sim_cache:

    def __init__(self,server):
        self._cache_file = {}
        self._target_server = server

    def _search_cache(self,target_file):
        # search file in the cache
        return target_file in self._cache_file

    def _read_cache(self,target_file):
        #read cached file
        if self._search_cache(target_file):
            return self._cache_file[target_file].get_data()
        else:
            return None

    def _write_cache(self,target_file,data,version):
        #write file to the cache
        if self._search_cache(target_file):
            self._cache_file[target_file].write_data(data,version)
        else:
            self._cache_file[target_file] = sim_file(target_file,data,version)

    def _invalidata_data(self,target_file):
        self._cache_file.pop(target_file)
    
    def _get_new_version(self):
        return time.time()


    '''
    可能用到的类与函数

    sim_file 模拟文件条目类
        sim_file.write(data,verion) 向文件条目写入data和version

        sim_file.get_data() 获取文件条目数据, 返回file_name,data,version

        sim_file.get_version() 获取文件version

    server 模拟服务器类, 在cache类初始化时绑定为self._target_server, 请使用该变量调用
        server.write(target_file,data,version) 尝试向服务器写入目标文件，如果目标文件已经存在，则会覆盖写入
        
        server.read(target_file) 尝试向服务器读取目标文件，如果服务器中存在该文件，则会返回 file_name,data,version
            如果不存在, 则会返回None

        server.get_version(target_file) 尝试向服务器获取目标文件version

    cache 模拟高速缓存类(在实现的函数中时候self调用下列函数)
        cache._get_new_version() 返回一个时间戳作为version

        cache._read_cache(target_file) 尝试从高速缓存中读取目标文件，
            如果高速缓存中存在该文件，则会返回 file_name,data,version
            如果不存在, 则会返回None 
        
        cache._write_cache(target_file,data,version) 尝试向高速缓存中写入目标文件，如果目标文件已经存在，则会覆盖写入

        cache._search_cache(target_file)在高速缓存中检索文件是否已经缓存
    
    '''
    
    """
    注意:
        测试数据确保不会出现读取服务器不存在的文件
        测试程序不存在也不要求高速缓存换出的情况
        请勿直接操作cache类和server类私有变量(除了调用_target_server外)
    """


    def read(self,target_file):
        #read file from file system
        
        ####### Begin #######
        
        #检查缓存中是否已缓存文件

        #向server确认version是否一致

        #选择从cache/server中读取文件

        #缓存从server中读取的文件

        ######## End ########

        # there is no file in the system
        return

    def write(self,target_file,data):
        
        ####### Begin #######

        #生成新version

        #向cache中写入数据并更新version

        #向server中写入数据并更新version

        ######## End ########

        return 