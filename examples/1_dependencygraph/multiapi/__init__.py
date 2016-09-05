from multimodule import (dirname,
                        MultiModule,
                        version_renamer)

mm = MultiModule('API', dirname(__file__))
mm.load(renamer=version_renamer)


def get(version):
    return mm.get(version)

