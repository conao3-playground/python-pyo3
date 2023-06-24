import pyo3_hello

def test_hello():
    assert pyo3_hello.sum_as_string(1, 2) == "3"
