DATABASE = "/home/zuplex/.usr/academic/engentrance/engdote/build/db/data.db"
MODEL_TEST_NUMBER = 160
TOKEN = "0l8ya1twx3nERISvSzreGcSZ213uutMGsWhzLwFYLteK7zyIyNNqrtyKLbuP" #tokendeep
TOKEN = "o5hXj22yc7hV1sUtSHdcbCA0USBkv1AoBTVuqdt7Bcrb35encsS7eP1rNjcb"
DAILY_TEST_URI = "https://api.engineeringdote.com/daily-test/start-exam"
MODEL_TEST_URI = "https://api.engineeringdote.com/model-test/start-exam/{}".format(
    MODEL_TEST_NUMBER
)
MOCK_TEST_URI = "https://api.engineeringdote.com/mock-test/start-exam"
QBANK_URI = "https://api.engineeringdote.com/qbank/start-exam"
QUESTION_URI = "https://api.engineeringdote.com/exam/questions"

QBANK_DATA = {
    "familiarity": "all",
    "noOfQuestions": "100",
    "marks": "0",
    "examType": "practice",
    "chapters": "",
}

MOCK_TEST_DATA = {"university": "ioe"}

HEADERS = {
    "Connection": "keep-alive",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96"',
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "sec-ch-ua-mobile": "?0",
    "Authorization": "Bearer {}".format(TOKEN),
    "sec-ch-ua-platform": '"Linux"',
    "Content-Type": "application/json",
    "Origin": "https://engineeringdote.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://engineeringdote.com/",
    "Accept-Language": "en-US,en;q=0.9",
}

CHAPTER_IDS = [
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    71,
    74,
    77,
    80,
    83,
    84,
    140,
    141,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    142,
    143,
    229,
    92,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    121,
    122,
    144,
    145,
    146,
    101,
    102,
    147,
    228,
    107,
    108,
    109,
    110,
    111,
    230,
    148,
    149,
    150,
    151,
    152,
    153,
    154,
    155,
    156,
    157,
    2,
    20,
    24,
    31,
    32,
    34,
    38,
    41,
    120,
    218,
    220,
    47,
    48,
    219,
    221,
    58,
    59,
    60,
    61,
    62,
    51,
    52,
    56,
    57,
    12,
    13,
    14,
    15,
    16,
    50,
    207,
    1,
    17,
    18,
    19,
    22,
    23,
    25,
    26,
    112,
    124,
    205,
    206,
    208,
    210,
    211,
    212,
    213,
    215,
    216,
    217,
    42,
    43,
    44,
    45,
    28,
    29,
    30,
    117,
    128,
    231,
    232,
    233,
    234,
    236,
    237,
    240,
    241,
    242,
    243,
    238,
    239,
    168,
    169,
    170,
    171,
    172,
    173,
    174,
    175,
    179,
    180,
    181,
    182,
    183,
    184,
    188,
    189,
    190,
    191,
    192,
    193,
    194,
    195,
    196,
    197,
    198,
    199,
    200,
    201,
]
