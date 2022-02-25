import json
import appdirs
import os
import csv
import xlsxwriter

_version = 'Version 1.2'
_author = 'Sergio Pereira'


class CacheHelper(object):
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

    def cache_dump(self, data_object, cache_name, indent=None):
        """
        Method serialize to  object as a JSON formatted stream. More information: https://docs.python.org/3/library/json.html#py-to-json-table
        :param data_object: dictionary, list, tuple, str, into, float boolean
        :param cache_name: file name
        :param indent: integer to pretty print JSON formart
        :return:
        """
        file = os.path.join(self.cache_dir, cache_name)
        try:
            with open(file, "w") as output_file:
                json.dump(data_object, output_file, indent)
            print("data object was dumped into {}".format(file))
        except json.JSONDecodeError as e:
            print(e)
        return file

    def cache_load(self, cache_name):
        """
        Method to load serialized object from a binary file.
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        with open(file, "rb") as input_file:
            try:
                return json.load(input_file)
            except ValueError as e:
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
        self.cache_dump(data_object, cache_name)

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

    def text_dump(self, data, file_name, ):
        """
        Method to dump text into a file
        :param data: string
        :param file_name: file name
        :return: None
        """
        file = os.path.join(self.cache_dir, file_name)
        with open(file, "w") as output_file:
            output_file.write(data)
        return

    def csv_dump(self, fields, rows, file_name):
        """
        Method to dump into a csv file
        :param fields: list of field names
        :param rows:  list of rows
        :param file_name: file name
        :return:  None
        """
        file = os.path.join(self.cache_dir, file_name)
        with open(file, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        print("csv was generated:  {}".format(file))
        return

    def excel_dump(self,filename, fields, rows,sheet_name='Data' ):
        """
        Method to dump into a excel file
        :param fields: Fields names
        :param row: list of rows. Each row is a list
        :param filename: file name
        :return:  None
        """
        workbook = xlsxwriter.Workbook('{filename}.xlsx')
        ws = workbook.add_worksheet('sheet_name')
        ws.autofilter('A1:G1')
        row = 0
        column = 0
        for tag in fields:
            ws.write(row, column, tag)
            column += 1
        row = 1
        for item in list:
            for col_num, data in enumerate(item):
                ws.write(row, col_num, data)
            row += 1
        workbook.close()    