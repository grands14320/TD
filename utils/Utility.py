import configparser
import json
import math
import os


class Tools:

    @staticmethod
    def create_config_file(path):

        config = """
            [window] \n
            width=1000 \n
            height=600 \n
            fps = 30 \n   
            """

        with open(path, 'a+') as file:
            file.write(config)

    @staticmethod
    def check_files(file_name_list):
        return [file for file in file_name_list if not os.path.isfile('images/' + file)]

    @staticmethod
    def get_config(config_file_path='config.ini'):
        """
        Gets config defined in specified file
        """
        if not os.path.exists(config_file_path):
            Tools.create_config_file(os.getcwd())
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config

    @staticmethod
    def get_length_point_to_point(A, B):
        """
        Calculates lengs from point A to point B
        """
        length_vector = (A[0] - B[0], A[1] - B[1])
        length = math.sqrt(length_vector[0] * length_vector[0] + length_vector[1] * length_vector[1])
        return length

    @staticmethod
    def get_waves_dict():
        """
        Gets waves from json file
        """
        with open("Levels/Level_0/waves.json") as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_single_wave():
        """
        Creates a generator objects yielding single wave.
        """
        wave = Tools.get_waves_dict()
        for wave_name, value in wave.items():
            print(wave_name, value)
            yield wave_name, value



