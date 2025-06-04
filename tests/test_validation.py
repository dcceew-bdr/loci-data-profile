from pyshacl import validate
from rdflib import Graph
from pathlib import Path

SHACL_GRAPH = Graph().parse(Path(__file__).parent.parent / "validator.ttl")
DATA_DIR = Path(__file__).parent / "data"
TEST_FILES = sorted([str(f) for f in DATA_DIR.glob("*.ttl")])

def test_validation():
    for test_file in TEST_FILES:

        data_graph = Graph().parse(test_file)
        expected_result = False if "invalid" in test_file else True
        v = validate(data_graph, shacl_graph=SHACL_GRAPH)
        assert v[0] == expected_result, test_file[0] + "ERROR: " + v[2]
