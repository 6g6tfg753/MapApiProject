import argparse


def count_lines(s):
    try:
        with open(s, 'rt') as f:
            lines = f.readlines()
    except Exception:
        lines = []
    return len(lines)


if __name__ == 'main':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='')
    args = parser.parse_args()
    print(count_lines(args.file))
