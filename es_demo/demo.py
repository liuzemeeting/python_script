room = [
        {
            "name": "卧室",
            "area": {
                "area": 9,
                "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于9m2"
            },
            "door": {
                "height": 2.00,
                "width": 0.90,
                "rule": "5.8.7"
            },
            "height": {"height": 2.40, "rule": "5.5.2"},
            "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
            "min_part_area": {"min_part_area": 1/3, "rule": "5.5.2"},

        },
        {
            "name": "卧室",
            "area": {
                "area": 5,
                "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于5m2"
            },
            "door": {
                "height": 2.00,
                "width": 0.90,
                "rule": "5.8.7"
            },
            "height": {"height": 2.40, "rule": "5.5.2"},
            "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
            "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
        },
        {
            "name": "兼起居室",
            "area": {
                "area": 12,
                "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于12m2"
            },
            "door": {
                "height": 2.00,
                "width": 0.90,
                "rule": "5.8.7"
            },
            "height": {"height": 2.40, "rule": "5.5.2"},
            "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
            "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
        },
    ]
cook_room = [
        {
            "name": "厨房",
            "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
            "door": {
                "height": 2.00,
                "width": 0.80,
                "rule": "5.8.7"
            },
            "area": {
                "area": 4,
                "rule": "5.3.1厨房的使用面积应符合下列规定: 由卧室、起居厅、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于4.0m2"
            }
        },
        {
            "name": "厨房",
            "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
            "door": {
                "height": 2.00,
                "width": 0.80,
                "rule": "5.8.7"
            },
            "area": {
                "area": 3.5,
                "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
            }
        }
    ]

toliet = [
            {
                "name": "卫生间",
                "height": {"height": 2.20, "rule": "5.5.4"},
                "area": {
                    "area": 2.5,
                    "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
                },
                "door": {
                    "height": 2.00,
                    "width": 0.70,
                    "rule": "5.8.7"
                },
                "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                "bianqi便器": 1,
                "xiyuqi洗浴器": 1,
                "ximianqi洗面器": 1,
            },
            {
                "name": "卫生间",
                "height": {"height": 2.20, "rule": "5.5.4"},
                "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                "area": {
                    "area": 1.8,
                    "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
                },
                "door": {
                    "height": 2.00,
                    "width": 0.70,
                    "rule": "5.8.7"
                },
                "bianqi便器": 1,
                "ximianji洗面器": 1,
            },
            {
                "name": "卫生间",
                "height": {"height": 2.20, "rule": "5.5.4"},
                "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                "area": {
                    "area": 2.0,
                    "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
                },
                "door": {
                    "height": 2.00,
                    "width": 0.70,
                    "rule": "5.8.7"
                },
                "bianqi便器": 1,
                "xiyuqi洗浴器": 1,
            },
            {
                "name": "卫生间",
                "height": {"height": 2.20, "rule": "5.5.4"},
                "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                "area": {
                    "area": 2.0,
                    "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
                },
                "door": {
                    "height": 2.00,
                    "width": 0.70,
                    "rule": "5.8.7"
                },
                "ximianqi洗面器": 1,
                "xiyuqi洗浴器": 1,
            },
            {
                "name": "卫生间",
                "height": {"height": 2.20, "rule": "5.5.4"},
                "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                "area": {
                    "area": 2.0,
                    "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
                },
                "door": {
                    "height": 2.00,
                    "width": 0.70,
                    "rule": "5.8.7"
                },
                "ximianqi洗面器": 1,
                "xiyiji洗衣机": 1,
            },
            {
                "name": "卫生间",
                "height": {"height": 2.20, "rule": "5.5.4"},
                "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                "area": {
                    "area": 2.0,
                    "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
                },
                "door": {
                    "height": 2.00,
                    "width": 0.70,
                    "rule": "5.8.7"
                },
                "bianqi便器": 1,
            }
        ]


windows = [
    {
        "height": 0,
        "width": 1,
    }
]