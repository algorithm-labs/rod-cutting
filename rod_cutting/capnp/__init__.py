import os
import sys

import capnp
capnp.remove_import_hook()

__DIR__ = os.path.dirname(__file__)

for filename in (fn for fn in os.listdir(__DIR__) if fn.endswith(".capnp")):
    name = filename.replace(".capnp", "")
    capnp_module = capnp.load( os.path.join(__DIR__, filename) )
    setattr(sys.modules[__name__], name, capnp_module)