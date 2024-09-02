import argparse


def main():
	parser = argparse.ArgumentParser(
		prog = 'Gendiff'
	)
	parser.add_argument('first_file')
	parser.add_argument('second_file')
	parser.parse_args(['-h'])


if __name__ == '__main__':
	main()

