
#Jada, dette virket veldig fornuftig dette!



from abaqus import *
from abaqusConstants import *
import __main__

def bf_2_x_make_own_sets():
    import re
    """
    Creates new sets based on names of old sets

    Configure what happens in this function.

    Regex 101:

    - "abc+" matches "abc"

    - "." matches any single character.
      "abc." matches "abc1", "abc2", "abc&" -- "abc" followed by any single character

    - "a*" matches "" (empty string), "a", a single a, "aaaaaa" (many as)
      ".*" matches anything
      "_abc.*" matches "_abcQWEQWE", "_abc123123" -- "_abc" followed by anything

    - "(abc|def)" matches "abc" or "def"
    """

    config = [
        ("w_pont_[0-9].*", "pont"),                    # Match _rodmat1, _rodmat2, ...
    ]

    # On this model
    modelname = "Bjornafjorden"

    # On this part
    partname = "Bridge"

    p = mdb.models[modelname].parts[partname]
    set_names_on_part = p.sets.keys()

    for pattern, newsetname in config:
        match = re.compile(pattern).match
        set_names = filter(match, set_names_on_part)
        oldsets = [p.sets[name] for name in set_names]
        p.SetByBoolean(name=newsetname, sets=tuple(oldsets))
    pass
