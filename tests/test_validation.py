from pyshacl import validate
from rdflib import Graph
from pathlib import Path

SHACL_GRAPH = Graph().parse(Path(__file__).parent.parent / "validator.ttl")
DATA_DIR = Path(__file__).parent / "data"

TESTS = [
    (str(DATA_DIR / "01-basic-valid.ttl"), True),
    (str(DATA_DIR / "02-nodataset-invalid.ttl"), False),
    (str(DATA_DIR / "03-basic-fcs-fs-valid.ttl"), True),
    (str(DATA_DIR / "04-empty-invalid.ttl"), False),
    (str(DATA_DIR / "05-isPartOf-valid.ttl"), True),
    (str(DATA_DIR / "06-hasPart-valid.ttl"), True),
]


def test_validation():
    for test in TESTS:
        data_graph = Graph().parse(test[0])
        v = validate(data_graph, shacl_graph=SHACL_GRAPH)
        assert v[0] == test[1], test[0]
