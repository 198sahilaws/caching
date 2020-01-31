import pickle
import appdirs
import os
_version = 'Version 1.0'
_author = 'Sergio Pereira'

class Serialization(object):
    def __init__(self, appname):
        self.appname = appname
        self.cache_dir = self.create_cache()

    def create_cache(self):
        """
        Method to create cache directory
        :return:
        """
        _ad = appdirs.AppDirs(appname=self.appname, appauthor=None, version=None, roaming=True, multipath=False)
        cache_dir = _ad.user_cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
            print("Caching directory {} was created ".format(cache_dir))
        else:
            print("Caching directory {} already exists".format(cache_dir))
        return cache_dir

    def pickle_dump(self, data_object, cache_name):
        """
        Method to serialize object into binary file.
        :param data_object: dictionary, array, etc
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        try:
            with open(file, "wb") as output_file:
                pickle.dump(data_object, output_file)
            print("data object was dumped into {}".format(file))
        except pickle.PicklingError as e:
            print(e)

    def pickle_load(self, cache_name):
        """
        Method to load serialized object from a binary file.
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        with open(file, "rb") as input_file:
            try:
                return pickle.load(input_file)
            except pickle.UnpicklingError as e:
                print(e)
        return

    def update_cache(self, data_object, cache_name):
        """
        Method to update existing binary serialized file.
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        if os.path.exists(file):
            os.remove(file)
        self.pickle_dump(data_object, cache_name)

    def delete_cache(self, cache_name):
        """
        Method to delete  binary serialized file.
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        if os.path.exists(file):
            os.remove(file)
        return
