class Logger:
    @staticmethod
    def log(message):
        print('[+] {}.'.format(message))

    @staticmethod
    def warn(message):
        print('[!] Warning: {}.'.format(message))

    @staticmethod
    def error(message):
        print('[-] Error: {}.'.format(message))

    @staticmethod
    def indent(message):
        print('\t{}.'.format(message))

if __name__ == '__main__':
    pass
