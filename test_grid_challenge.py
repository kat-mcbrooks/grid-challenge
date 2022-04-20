from grid_challenge import bomberPlane


def test_bomberPlane_2seconds_1_row():
    assert bomberPlane(2, ["O..OO.O"]) == ["OOOOOOO"]


def test_bomberPlane_2seconds_multiple_rows():
    assert bomberPlane(2, ["OOO.OOO", "OO...OO", "OOO...O", "..OO.OO", "...OOOO", "...OOOO"]) == [
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
    ]
