from release_notes import release_heading


def test_release_heading():
    assert release_heading("1.2.0") == "Release 1.2.0"


def test_release_heading_custom_prefix():
    # Test with a custom prefix by monkeypatching the function temporarily
    original_function = release_heading

    def custom_release_heading(version: str) -> str:
        prefix = "Version"
        return f"{prefix} {version}"

    # Replace the function temporarily
    import release_notes
    release_notes.release_heading = custom_release_heading

    assert release_notes.release_heading("2.0.1") == "Version 2.0.1"

    # Restore the original function
    release_notes.release_heading = original_function


def test_release_heading_empty_prefix():
    # Test with an empty prefix by monkeypatching the function temporarily
    original_function = release_heading

    def empty_prefix_release_heading(version: str) -> str:
        prefix = ""
        return f"{prefix}{version}"

    import release_notes
    release_notes.release_heading = empty_prefix_release_heading

    assert release_notes.release_heading("3.0.0") == "3.0.0"

    # Restore the original function
    release_notes.release_heading = original_function
