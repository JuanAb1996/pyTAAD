from time import strftime

# These tuples were generated using localtime() and gmtime() in CPython.
INPUT = (
    (2017, 1,  1,  23, 40, 39, 6, 222, 1),
    (2010, 2,  28, 9,  59, 60, 1, 111, 0),
    (2000, 3,  31, 1,  33, 0,  2, 44,  1),
    (2020, 4,  30, 21, 22, 59, 3, 234, 0),
    (1977, 5,  15, 23, 55, 1,  4, 123, 1),
    (1940, 6,  11, 9,  21, 33, 5, 55,  0),
    (1918, 7,  24, 6,  12, 44, 7, 71,  1),
    (1800, 8,  17, 0,  59, 55, 3, 89,  0),
    (2222, 9,  5,  1,  0,  4,  2, 255, 1),
    (2017, 10, 10, 9,  1,  5,  6, 200, 0),
    (2016, 11, 7,  18, 8,  16, 7, 100, 1),
    (2001, 12, 2,  12, 19, 27, 1, 33,  0),
)

# These values were generated using strftime() in CPython.
EXPECTED = (
    ('20170101234039'),
    ('20100228095960'),
    ('20000331013300'),
    ('20200430212259'),
    ('19770515235501'),
    ('19400611092133'),
    ('19180724061244'),
    ('18000817005955'),
    ('22220905010004'),
    ('20171010090105'),
    ('20161107180816'),
    ('20011202121927'),
)

for i in range(len(INPUT)):
    assert strftime("%Y%m%d%H%M%S", INPUT[i]) == EXPECTED[i]
