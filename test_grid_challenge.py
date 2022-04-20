from grid_challenge import bomberPlane


def test_bomberPlane_1second_multiple_rows():
    assert bomberPlane(1, ["OOO.OOO", "OO...OO", "OOO...O", "..OO.OO", "...OOOO", "...OOOO"]) == [
        "OOO.OOO",
        "OO...OO",
        "OOO...O",
        "..OO.OO",
        "...OOOO",
        "...OOOO",
    ]


def test_bomberPlane_1seconds_1_row():
    assert bomberPlane(1, ["O..OO.O"]) == ["O..OO.O"]


def test_bomberPlane_0seconds_1_row():
    assert bomberPlane(0, ["O..OO.O"]) == ["O..OO.O"]


def test_bomberPlane_0seconds_multiple_rows():
    assert bomberPlane(0, ["OOO.OOO", "OO...OO", "OOO...O", "..OO.OO", "...OOOO", "...OOOO"]) == [
        "OOO.OOO",
        "OO...OO",
        "OOO...O",
        "..OO.OO",
        "...OOOO",
        "...OOOO",
    ]


def test_bomberPlane_2seconds_1_row():
    assert bomberPlane(2, ["O..OO.O"]) == ["OOOOOOO"]


def test_bomberPlane_2seconds_2_row_1_col():
    assert bomberPlane(2, ["O", "."]) == ["O", "O"]


def test_bomberPlane_2seconds_multiple_rows():
    assert bomberPlane(2, ["OOO.OOO", "OO...OO", "OOO...O", "..OO.OO", "...OOOO", "...OOOO"]) == [
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
        "OOOOOOO",
    ]


def test_bomberPlane_3seconds_1_row():
    assert bomberPlane(3, ["O..OO.O"]) == ["......."]


def test_bomberPlane_3seconds_multiple_rows():
    assert bomberPlane(3, ["OOO.OOO", "OO...OO", "OOO...O", "..OO.OO", "...OOOO", "...OOOO"]) == [
        ".......",
        "...O...",
        "....O..",
        ".......",
        "OO.....",
        "OO.....",
    ]


def test_bomberPlane_3seconds_multiple_rows():
    assert bomberPlane(3, [".......", "...O...", "....O..", ".......", "OO.....", "OO....."]) == [
        "OOO.OOO",
        "OO...OO",
        "OOO...O",
        "..OO.OO",
        "...OOOO",
        "...OOOO",
    ]
