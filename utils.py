MIN_RUN = 32  # 64


def find_min_run(n: int) -> int:
    """Returns the minimum length of a run from 23 - 64
    so that the len(array)/min_run is less than or equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33, ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r
