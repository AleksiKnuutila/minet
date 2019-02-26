# =============================================================================
# Minet Range Set Collection
# =============================================================================
#
# Simplistic implementation of a range set in python relying on a sorted list of
# contiguous intervals. It is very useful to represent a set of dense intervals
# using very little memory & is used across the task-resuming schemes of the
# CLI tool.
#
# It takes a lot of inspiration from the inversion list data structure.
#
from bisect import bisect_left


class RangeSet(object):
    def __init__(self):
        # TODO: replace this by `blist` if not performany enough
        self.intervals = []

    def add(self, point):

        interval = (point, point)
        N = len(self.intervals)

        # Set is empty
        if N == 0:
            self.intervals.append(interval)
            return

        # Finding insertion point
        index = bisect_left(self.intervals, interval)

        if index >= N:
            self.intervals.append(interval)
            return

        matched_interval = self.intervals[index]

        if point == matched_interval[0] - 1:
            self.intervals[index] = (point, matched_interval[1])

            if index != 0:
                previous_interval = self.intervals[index - 1]

                if point == previous_interval[1] + 1:
                    self.intervals[index] = (previous_interval[0], matched_interval[1])
                    self.intervals.pop(index - 1)

            return

        if point < matched_interval[0]:
            self.intervals.insert(index, interval)
            return
