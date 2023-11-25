import re
import cutter
import rzpipe


import libs2sigs


class MyCutterPlugin(cutter.CutterPlugin):
    name = 'My Plugin'
    description = 'Test plugin'
    version = '1.0'

    def setupPlugin(self):
        pass

    def setupInterface(self):

    def terminate(self):

def create_cutter_plugin():
    return MyCutterPlugin()
binary_path = './lib.so'

pattern = re.compile(r'([\w\d\-_]+)-(\d+\.\d+\.\d+)')

rz = rzpipe.open(binary_path)
rz.cmd('aa')

libs = set(re.findall(pattern, rz.cmd('izQ')))

print('Found %d libraries!' % len(libs))

for lib, version in libs:
    print('%s = "%s"' % (lib, version))

libs2sigs.rlib_to_sig(libs, 'rizin')
