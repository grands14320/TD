import configparser
import os
import math
import sys
import json


class Tools:

    @staticmethod
    def create_config_file(path):

        config = """
            [window] \n
            width=600 \n
            height=800 \n
            fps = 30 \n   
            """

        with open(path, 'a+') as file:
            file.write(config)

    @staticmethod
    def check_files(file_name_list):
        return [file for file in file_name_list if not os.path.isfile('images/' + file)]

    @staticmethod
    def get_config(config_file_path='config.ini'):
        if not os.path.exists(config_file_path):
            Tools.create_config_file(os.getcwd())
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config

    @staticmethod
    def get_length_point_to_point(A, B):
        length_vector = (A[0] - B[0], A[1] - B[1])
        length = math.sqrt(length_vector[0] * length_vector[0] + length_vector[1] * length_vector[1])
        return length

    @staticmethod
    def get_waves_dict():
        with open("Levels/Level_0/waves.json") as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_single_wave():
        lol = Tools.get_waves_dict()
        for raz, dwa in lol.items():
            print(raz, dwa)
            yield raz, dwa



