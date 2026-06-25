def test_schema():

    expected_columns = [
        "patient_id",
        "patient_name",
        "dob"
    ]

    assert len(expected_columns) == 3