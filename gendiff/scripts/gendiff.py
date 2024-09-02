import argparse


def main():
	parser = argparse.ArgumentParser(
		prog = 'Gendiff'
	)
	parser.add_argument('first_file')
	parser.add_argument('second_file')
	parser.add_argument('-f', '--format', help = 'set format of output')
	parser.parse_args(['-h'])


if __name__ == '__main__':
	main()

