from collections import namedtuple
import os.path
import pkgutil
import sys

PackageLoader = namedtuple('PackageLoader', ['fqname', 'loader', 'module'])

class InvalidModuleError(Exception):
    def __init__(self, label, name):
        s = '{label}: Invalid module name: {name}' \
            .format(label=label, name=name)
        super(InvalidModuleError, self).__init__(s)


def version_renamer(s):
    return s.replace('_', '.')


def dirname(f):
    return os.path.dirname(os.path.abspath(f))


class MultiModule(object):
    def __init__(self, loglabel, dirname):
        self.label = loglabel
        self.dirname = dirname
        self.loaders = {}
        self.modules = {}

    def load(self, renamer=None):
        for importer, package_name, _ in pkgutil.iter_modules([self.dirname]):
            full_package_name = '%s.%s' % (self.dirname, package_name)
            newname = renamer(package_name) if renamer else package_name
            if full_package_name not in sys.modules:
                self.loaders[newname] = PackageLoader(full_package_name, importer.find_module(package_name), None)
            else:
                self.modules[newname] = sys.modules[full_package_name]

    def get(self, name):
        if name not in self.loaders:
            raise InvalidModuleError(self.label, name)
        if name not in self.modules:
            l = self.loaders.get(name)
            self.modules[name] = l.loader.load_module(l.fqname)
        return self.modules[name]

