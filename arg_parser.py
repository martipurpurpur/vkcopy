import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="url parser")
    parser.add_argument("-u", "--url", type=str, )
    return parser.parse_args()
