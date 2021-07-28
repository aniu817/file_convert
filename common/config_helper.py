from configparser import ConfigParser
import os
from common.path_helper import PathHelper


class ConfigHelper:

    @staticmethod
    def config_parser(config_name,
                      section,
                      option):

        config = ConfigParser()
        file_path = PathHelper.get_package_dir('config')
        config.read(os.path.join(file_path, config_name))
        return config.get(section, option)


if __name__ == "__main__":
    print(ConfigHelper.config_parser('row_list', 'rows', 'row').split(','))
    print(111)
