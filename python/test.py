# A random dataset of nested arrays is given with n levels
# Method count_edges should return number of all arrays with no more nested elements
#
# Example dataset:
#
dataset = [
    [
        [
            [
                []
            ],
            [
                [
                    []
                ]
            ]
        ]
    ],
    [],
    [
        [
            [],
            []
        ]
    ]
]


# [[],[[]]] -> 2

def count_edges(data):



assert 5 == count_edges(dataset)
