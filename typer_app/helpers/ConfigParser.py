import configparser as configparser


class ConfigParser(object):
    def __init__(self):
        self.Config = configparser.ConfigParser()

    def read_file(self,file):
        self.Config.read(filenames=file)

    def ConfigSectionMap(self, section):
        dict1 = {}
        sections = self.Config.sections()
        options = self.Config.options(section)
        for option in options:
            try:
                dict1[option] = self.Config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1