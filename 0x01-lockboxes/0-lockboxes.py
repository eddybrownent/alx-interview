#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Tell if all boxes can be opened.

    Args:
        boxes (list of lists): Each box is numbered from 0 to (n - 1)
                             each box may contain keys to the other boxes

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes or type(boxes) is not list:
        return False
    # opened boxes
    opened_boxes = set()
    # first box is unlocked
    opened_boxes.add(0)

    # Iterate through boxes
    for box_num, keys in enumerate(boxes):
        # If the current box is opened, add its keys to the set
        if box_num in opened_boxes:
            opened_boxes.update(keys)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
