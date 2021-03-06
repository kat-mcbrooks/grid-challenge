from grid_challenge import bomberPlane


# def test_bomberPlane_testcase13():
#     assert bomberPlane(
#         181054341,
#         [
#             "O..OO........O..O........OO.O.OO.OO...O.....OOO...OO.O..OOOOO...O.O..O..O.O..OOO..O..O..O....O...O....O...O..O..O....O.O.O.O.....O.....OOOO..O......O.O.....OOO....OO....OO....O.O...O..OO....OO..O...O"
#         ],
#     ) == [
#         "OOOOO........OOOO........OOOOOOOOOO...O.....OOO...OOOOOOOOOOO...OOOOOOOOOOOOOOOOOOOOOOOOO....O...O....O...OOOOOOO....OOOOOOO.....O.....OOOOOOO......OOO.....OOO....OO....OO....OOO...OOOOO....OOOOO...O"
#     ]


def test_bomberPlane_3seconds_4by3_grid():
    assert bomberPlane(3, ["O..O", ".O..", "...."]) == ["....", "....", "O.OO"]


# after 4 seconds, fill the grid. bombs labelled 4 are the new bombs so bombs labelled O are the ones that will detonate after 5 seconds
# ["4444", "4444", "O4OO"]
def test_bomberPlane_5seconds_4by3_grid():
    assert bomberPlane(5, ["O..O", ".O..", "...."]) == ["OOOO", ".O..", "...."]


def test_bomberPlane_7seconds_4by3_grid():
    assert bomberPlane(7, ["O..O", ".O..", "...."]) == ["....", "....", "O.OO"]


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


# after 4:
#       "OOO4OOO",
#       "OO444OO",
#       "OOO444O",
#       "44OO4OO",
#       "444OOOO",
#       "444OOOO",


def test_bomberPlane_5seconds_multiple_rows_B():
    assert bomberPlane(5, [".......", "...O...", "....O..", ".......", "OO.....", "OO....."]) == [
        ".......",
        "...O...",
        "....O..",
        ".......",
        "OO.....",
        "OO.....",
    ]


def test_bomberPlane_3seconds_multiple_rows_pre_5seconds():
    assert bomberPlane(3, [".......", "...O.O.", "....O..", "..O....", "OO...OO", "OO.O..."]) == [
        "OOO.O.O",
        "OO.....",
        "OO....O",
        ".......",
        ".......",
        ".......",
    ]


def test_bomberPlane_5seconds_multiple_rows_A():
    assert bomberPlane(5, [".......", "...O.O.", "....O..", "..O....", "OO...OO", "OO.O..."]) == [
        ".......",
        "...O.O.",
        "...OO..",
        "..OOOO.",
        "OOOOOOO",
        "OOOOOOO",
    ]


# after 4 secs:
#       "OOO4O4O",
#       "OO44444",
#       "OO4444O",
#       "4444444",
#       "4444444",
#       "4444444",
# after 5 secs:
