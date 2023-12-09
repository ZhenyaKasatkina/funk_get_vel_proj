from utils import dicts


def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == 'mercurial'
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", 'test') == 'mercurial'
    assert dicts.get_val({}, "vcs", 'test') == 'test'
    assert dicts.get_val({"vcs": "mercurial"}, "ky_vcs", 'test') == 'test'
    assert dicts.get_val({"vcs": "mercurial"}, "ky_vcs") == 'git'
