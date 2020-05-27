import argparse
from program import Program


def main():
    parser = argparse.ArgumentParser(description='You started a proxy-script.'
                                                 ' Enter your port to use '
                                                 'this')
    parser.add_argument('-p', '--port', help='This will be your port')
    port = parser.parse_args().port
    prog = Program(port)
    prog.process()


if __name__ == '__main__':
    main()
