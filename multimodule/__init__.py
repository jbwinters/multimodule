import os.path
import pkgutil
import sys


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
    def __init__(self, label, dirname):
        self.label = label
        self.dirname = dirname
        self.modules = {}

    def load(self, renamer=None):
        for importer, package_name, _ in pkgutil.iter_modules([self.dirname]):
            full_package_name = '{}.{}'.format(self.dirname, package_name)
            if full_package_name not in sys.modules:
                module = importer.find_module(package_name).load_module(full_package_name)
                r_pkg_name = renamer(package_name)
                self.modules[r_pkg_name] = module

    def get(self, name):
        if name not in self.modules:
            raise InvalidModuleError(self.label, name)
        return self.modules[name]
