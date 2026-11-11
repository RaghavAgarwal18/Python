"""
Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
Compared to a cyclic redundancy check of the same length, it trades reliability for
speed (preferring the latter).
Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
Fletcher-32.[2]

source: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(plain_text: str) -> int:
    """
    Function implements adler-32 hash.
    Adler-32 is defined over bytes, so the text is first encoded as UTF-8 and
    a new value is evaluated for each byte.

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122

    >>> adler32('')
    1

    Non-ASCII characters span several UTF-8 bytes and must match zlib:

    >>> adler32('café')
    114885271

    >>> import zlib
    >>> adler32('naïve 日本語') == zlib.adler32('naïve 日本語'.encode('utf-8'))
    True
    """
    a = 1
    b = 0
    for byte in plain_text.encode("utf-8"):
        a = (a + byte) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
