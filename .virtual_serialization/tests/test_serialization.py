from serialization import Serialization
import unittest
from os import path

device_info = {
    "server1": "192.168.1.100",
    "server2": "192.168.1.200",
}
new_device_info = {
    "server1": "172.16.0.100",
    "server2": "172.16.0.200",
}


class TestSerialization(unittest.TestCase):

    def test_pickle_dump(self):
        a = Serialization('appname')
        file = a.pickle_dump(data_object=device_info, cache_name="device_info")
        self.assertTrue(path.exists(file))

    def test_pickle_loads(self):
        a = Serialization('appname')
        load_dic = a.pickle_load(cache_name="device_info")
        self.assertEqual(device_info, load_dic)

    def test_update_cache(self):
        a = Serialization('appname')
        a.update_cache(data_object=new_device_info, cache_name="device_info")
        load_dic = a.pickle_load(cache_name="device_info")
        self.assertEqual(new_device_info, load_dic)

