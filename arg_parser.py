import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="archive path")
    parser.add_argument("-i", "--in", type=str, required=True)
    parser.add_argument("-o", "--out", type=str, required=False)
    return parser.parse_args()
