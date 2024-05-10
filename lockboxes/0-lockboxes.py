#!/usr/bin/env python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """Can unlock all  function to unlock all boxes"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
