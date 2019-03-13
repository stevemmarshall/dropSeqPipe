import sys
import subprocess
import os

def main():
	arguments = ['snakemake']
	arguments.extend(sys.argv[1:])
	subprocess.run(args=arguments, 	cwd=os.path.join(os.path.dirname(__file__),'..'))


if __name__=='__main__':
	main()