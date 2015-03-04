#!/usr/bin/env python
import fileinput


def answer(heights):
    """ Compute total area of standing water given a list of heights.

        Iterate over a list from both ends, keeping track of
        max height on the left, current left index,
        max height on the right, current right index

           X    max_left == 3, max_right == 2
        X  X
        X  X X  max_right is the same as the height in R, so nothing
        XXXXXX  is added to the water volume.
        L    R

        The highest point is on the left, so we'll start
        filling from the right since there are 3 possibilities:
        1) There's a higher point to the right of L
        2) There's a lower point to the right of L
        3) There are equal height points to the right of L

           X
        X  X
        X  X0X      X   0X      X  X0X
        XXXXXX      XXXX0X      XXXXXX
        L   R       L   R       L   R 

        In any of the cases, filling the cell with water up to height
        max_right is correct.
    """
    max_left = 0
    max_right = 0
    left = 0
    right = len(heights) - 1
    volume = 0

    while left < right:
        if max_left < heights[left]:
            max_left = heights[left]
        if max_right < heights[right]:
            max_right = heights[right]
        if max_right >= max_left:
            volume += max_left - heights[left]
            left += 1
        else:
            volume += max_right - heights[right]
            right -= 1

    return volume


def main():
    pass


if __name__ == '__main__':
    main()
