
import modelx as mx
import pytest

@pytest.mark.skip
def test_del_defined_base():
    """
    A <- B <- C
    |    |    |
    X    X    X*
    |    |    |
    M    M*N  M*N*

    delete B.X

    A <- B <- C
    |    |    |
    X    X*   X*
    |    |    |
    M    M*   M*
    """
    m = mx.new_model()
    m.new_space("A").new_space("X").new_cells("M")
    m.new_space("B").new_space("X").new_cells("N")
    m.B.add_bases(m.A)
    m.new_space("C", bases=m.B)

    assert hasattr(m.B.X, "M")
    assert hasattr(m.B.X, "N")
    assert hasattr(m.C.X, "M")
    assert hasattr(m.C.X, "N")

    del m.B.X

    assert hasattr(m.B.X, "M")
    assert not hasattr(m.B.X, "N")
    assert hasattr(m.C.X, "M")
    assert not hasattr(m.C.X, "N")

    m._impl._check_sanity()
    m.close()

@pytest.mark.parametrize("base_name", ["Base"])   # TODO: Fix when base is Child
def test_del_base_in_model(base_name):
    """
        m---Base---Child---foo
          |  |
          |  +--bar
          |
          +-Sub(Base)

    """
    m, base = mx.new_model(), mx.new_space("Base")
    child = base.new_space("Child")
    cells = base.new_cells("bar")
    child.new_cells("foo")
    base = base if base_name == "Base" else child

    m.new_space("Sub", bases=base)

    del m.Base

    assert not m.Sub.cells
    assert not m.Sub.spaces

    m._impl._check_sanity()
    m.close()