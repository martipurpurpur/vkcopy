import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="archive path")
    parser.add_argument("-p", "--path", type=str, )
    return parser.parse_args()
