# python -m unittest -v tests.test_cachehelper.CacheHelper
from cachehelper import CacheHelper
import unittest
from os import path

device_info = {
    "server1": "192.168.1.100",
    "server2": "192.168.1.200"
}
new_device_info = {
    "server1": "172.16.0.100",
    "server2": "172.16.0.200",
}


class TestSerialization(unittest.TestCase):

    def test_pickle_dump(self):
        a = CacheHelper(appname='appname')
        file = a.pickle_dump(data_object=device_info, cache_name="device_info")
        self.assertTrue(path.exists(file))
