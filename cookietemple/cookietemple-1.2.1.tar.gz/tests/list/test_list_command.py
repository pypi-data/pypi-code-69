import pytest
from cookietemple.list.list import TemplateLister

"""
This test class is for testing the list subcommand:

Syntax: cookietemple list
"""


def test_non_empty_output(capfd):
    """
    Verifies that the list command does indeed have content

    :param capfd: pytest fixture -> capfd: Capture, as text, output to file descriptors 1 and 2.
    """
    # Capture stdout
    lister = TemplateLister()
    lister.list_available_templates()
    out, err = capfd.readouterr()

    assert not err
    assert out


@pytest.mark.skip(reason="Again here, check how to check rich output of a Table")
def test_header(capfd):
    """
    Verifies that the list command does have the following header
    Name    Handle   Version (Short Description and Available Libs are rendered different)

    :param capfd: pytest fixture -> capfd: Capture, as text, output to file descriptors 1 and 2.
    """
    # Capture stdout
    lister = TemplateLister()
    lister.list_available_templates()
    out, err = capfd.readouterr()
    # We skip the COOKIETEMPLE autogenerated lines (0-2)
    header = set(out.split('\n')[4].split())

    assert 'Name' in header and 'Handle' in header
