import idautils
import re
import libs2sigs

def main():
    sc = idautils.Strings()

    pattern = re.compile(r'([\w\d\-_]+)-(\d\.\d+\.\d+)')
    libs = set(re.findall(pattern, ''.join(map(str, sc))))

    print('Found %d libraries!' % len(libs))

    for lib, version in libs:
        print('%s = "%s"' % (lib, version))

    libs2sigs.rlib_to_sig(libs)

if __name__ == '__main__':
    main()
