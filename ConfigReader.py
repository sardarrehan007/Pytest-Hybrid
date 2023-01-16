import configparser

from Librariries import *

config = configparser.RawConfigParser()
config.read("Main/config.ini")

class ReadConfig_URL:

    @staticmethod
    def SET_ADMIN_URL():
      BASE_URL = config.get('URLS', 'BASE_URL')
      return BASE_URL




class ReadConfig_LOGIN:

    @staticmethod
    def SET_LOGIN_EMAIL():
      EMAIL = config.get('MP32_LOGIN', 'EMAIL')
      return EMAIL

    @staticmethod
    def SET_LOGIN_PASSWORD():
        PASSWORD = config.get('MP32_LOGIN', 'PASSWORD')
        return PASSWORD

    @staticmethod
    def SET_LOGIN_EMAIL2():
        EMAIL = config.get('ADMIN_LOGIN_LAB', 'EMAIL')
        return EMAIL

    @staticmethod
    def SET_LOGIN_PASSWORD2():
        PASSWORD = config.get('ADMIN_LOGIN_LAB', 'PASSWORD')
        return PASSWORD

    @staticmethod
    def SET_LOGIN_EMAIL3():
        EMAIL = config.get('ADMIN_LOGIN_OPS', 'EMAIL')
        return EMAIL

    @staticmethod
    def SET_LOGIN_PASSWORD3():
        PASSWORD = config.get('ADMIN_LOGIN_OPS', 'PASSWORD')
        return PASSWORD

    @staticmethod
    def SET_LOGIN_EMAIL4():
        EMAIL = config.get('ADMIN_LOGIN_SALES', 'EMAIL')
        return EMAIL

    @staticmethod
    def SET_LOGIN_PASSWORD4():
        PASSWORD = config.get('ADMIN_LOGIN_SALES', 'PASSWORD')
        return PASSWORD

class ReadConfig_EXECUTABLE_PATH:

    @staticmethod
    def SET_CHROME_EXECUTABLE_PATH():
      CHROME_EXECUTABLE_PATH = config.get('EXECUTABLE_PATHS', 'CHROME_EXECUTABLE_PATH')
      return CHROME_EXECUTABLE_PATH

    @staticmethod
    def SET_EDGE_EXECUTABLE_PATH():
      EDGE_EXECUTABLE_PATH = config.get('EXECUTABLE_PATHS', 'EDGE_EXECUTABLE_PATH')
      return EDGE_EXECUTABLE_PATH



