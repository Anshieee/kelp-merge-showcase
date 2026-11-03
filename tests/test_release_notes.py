from release_notes import release_heading


def test_release_heading():
    assert release_heading("1.2.0") == "Release 1.2.0"
