import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\cprakash\PycharmProjects\restAPI_Project1\utilities\properties.ini')
    return config