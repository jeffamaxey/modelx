from modelx.serialize.jsonvalues import *

_formula = None

_bases = []

_allow_none = None

_spaces = []

# ---------------------------------------------------------------------------
# Cells

def foo():
    return 'Hello!'


# ---------------------------------------------------------------------------
# References

grandpibling = ("Interface", ("....", "Pibling"), "auto")