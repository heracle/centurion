class Logger:
    @staticmethod
    def log(message):
        print('[+] {}.'.format(message))
        return message

    @staticmethod
    def warn(message):
        print('[!] Warning: {}.'.format(message))
        return message

    @staticmethod
    def error(message):
        print('[----] Error: {}.'.format(message))
        return message

    @staticmethod
    def indent(message):
        print('\t{}.'.format(message))
        return message

if __name__ == '__main__':
    pass
