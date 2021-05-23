import re
import pybins.linux as lin
import pybins.windows as win

def main(parser):
    args = parser.parse_args()

    mode=0
    fragment = {}
    
    if args.binary is not None:
        fragment['cmd'] = args.binary
        mode = mode + 1

    if args.function is not None:
        fragment['function'] = args.function
        mode = mode + 2
    
    if args.platform is None:
        print("the following arguments are required: -p/--platform\n")
        parser.print_help()
        return False

    platform = args.platform.lower()

    win_re = re.compile(r'(win$|windows$)')
    lin_re = re.compile(r'(lin$|linux$)')

    if win_re.match(platform):
        plat = win
    elif lin_re.match(platform):
        plat = lin
    else:
        print("Platform must be Windows os Linux")
        return False


    if mode == 1:
        plat.print_binary_functions(args.binary)
    elif mode == 2:
        plat.print_function_binaries(args.function) 
    elif mode == 3:
        plat.print_binary_cmd(args.binary, args.function)
    else:
        plat.print_platform_all()



