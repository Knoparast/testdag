import internal_unit_testing


def test_dag_import():
    from . import example_dag

    internal_unit_testing.assert_has_valid_dag(example_dag)
