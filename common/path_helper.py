import os


class PathHelper:

    @staticmethod
    def get_project_dir():
        # return os.path.abspath(os.path.dirname(os.getcwd()))
        return os.path.abspath(os.path.join(os.getcwd()))

    @staticmethod
    def get_package_dir(package_name):
        return os.path.join(PathHelper.get_project_dir(), package_name)


if __name__ == "__main__":
    print(PathHelper().get_project_dir())
    print(PathHelper().get_package_dir('row_list'))
