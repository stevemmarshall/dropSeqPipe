import sys
import subprocess

def main():
	arguments = ['snakemake']
	arguments.extend(sys.argv[1:])
	subprocess.run(args=arguments)


if __name__=='__main__':
	main()