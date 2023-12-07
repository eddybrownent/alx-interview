#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists): Each box is numbered sequentially from 0 to n - 1,
                             and each box may contain keys to the other boxes.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    if not boxes or type(boxes) is not list:
        return False

    # opened boxes
    opened_boxes = set([0])

    # List of new keys
    new_keys = [0]

    while new_keys:
        current_box = new_keys.pop()

        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # If key opens new box and the box is not opened yet
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                new_keys.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
