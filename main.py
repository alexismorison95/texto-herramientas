from args import parseArgs
from functions import resolver
import sys



def main():
    parser, args = parseArgs()

    if len(sys.argv) > 1:
        resolver(args.input, args.output, args.justificado, args.guion)
    else:
        parser.print_help(sys.stderr)
        sys.exit()



if __name__ == '__main__':
    main()