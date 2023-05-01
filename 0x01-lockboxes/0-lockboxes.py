#!/usr/bin/python3
""" locked box """
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = set(boxes[0])
    while keys:
        key = keys.pop()
        if not unlocked[key]:
            unlocked[key] = True
            keys |= set(boxes[key])
    return all(unlocked)
