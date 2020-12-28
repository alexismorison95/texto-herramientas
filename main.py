from args import parseArgs
from functions import resolver
import sys


def main():
    parser, args = parseArgs()

    #print(args)

    if len(sys.argv) > 1:

        if args.input:
            resolver(args.input, None, args.justificado, args.guion, True)

        else:
            with args.file:
                with args.save:
                    resolver(args.file.name, args.save.name, args.justificado, args.guion, False)
    else:
        parser.print_help(sys.stderr)
        sys.exit()


if __name__ == '__main__':
    main()

