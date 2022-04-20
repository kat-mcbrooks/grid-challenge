from grid_challenge import bomberPlane


def test_bomberPlane_2seconds_1_row():
    assert bomberPlane(2, ["O..OO.O"]) == ["OOOOOOO"]
