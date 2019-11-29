from es_demo.common import ElasticSearchClass
from datetime import datetime

obj = ElasticSearchClass("192.168.99.107", "9200", "", "")


if __name__ == "__main__":
    # for i in ["AW6lg9OR-XfAA_GYpeXj"]:
    #     dd = obj.delete(indexname='apartment', doc_type='text', id=i)
    # response = obj.searchindex(index="apartment")
    # print(response["hits"]["hits"][0]["_source"]["any"]["body"])
    # data = {
    #     "name": "一室一厅一厨一卫",
    #     "height": {"heigh": 2.80, "rule": "5.5.1"},
    #     "rooms": {
    #         "room": [
    #             {
    #                 "name": "卧室",
    #                 "area": {
    #                     "area": 9,
    #                     "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于9m2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.90,
    #                     "rule": "5.8.7"
    #                 },
    #                 "height": {"height": 2.40, "rule": "5.5.2"},
    #                 "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
    #                 "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
    #
    #             },
    #             {
    #                 "name": "卧室",
    #                 "area": {
    #                     "area": 5,
    #                     "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于5m2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.90,
    #                     "rule": "5.8.7"
    #                 },
    #                 "height": {"height": 2.40, "rule": "5.5.2"},
    #                 "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
    #                 "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
    #             },
    #             {
    #                 "name": "兼起居室",
    #                 "area": {
    #                     "area": 12,
    #                     "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于12m2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.90,
    #                     "rule": "5.8.7"
    #                 },
    #                 "height": {"height": 2.40, "rule": "5.5.2"},
    #                 "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
    #                 "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
    #             },
    #         ],
    #         "rule": "5.2.1"
    #     },
    #     "cook_room": {
    #         "cook_room": [
    #             {
    #                 "name": "厨房",
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.80,
    #                     "rule": "5.8.7"
    #                 },
    #                 "area": {
    #                     "area": 4,
    #                     "rule": "5.3.1厨房的使用面积应符合下列规定: 由卧室、起居厅、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于4.0m2"
    #                 }
    #             },
    #             {
    #                 "name": "厨房",
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.80,
    #                     "rule": "5.8.7"
    #                 },
    #                 "area": {
    #                     "area": 3.5,
    #                     "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
    #                 }
    #             },
    #         ],
    #         "rule": "5.3.1"
    #     },
    #     "toliet": {
    #         "toliet": [
    #             {
    #                 "name": "卫生间",
    #                 "height": {"height": 2.20, "rule": "5.5.4"},
    #                 "area": {
    #                     "area": 2.5,
    #                     "rule": "5.4.1"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.70,
    #                     "rule": "5.8.7"
    #                 },
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "bianqi便器": 1,
    #                 "xiyuqi洗浴器": 1,
    #                 "ximianqi洗面器": 1,
    #             },
    #             {
    #                 "name": "卫生间",
    #                 "height": {"height": 2.20, "rule": "5.5.4"},
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "area": {
    #                     "area": 1.8,
    #                     "rule": "5.4.2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.70,
    #                     "rule": "5.8.7"
    #                 },
    #                 "bianqi便器": 1,
    #                 "ximianji洗面器": 1,
    #             },
    #             {
    #                 "name": "卫生间",
    #                 "height": {"height": 2.20, "rule": "5.5.4"},
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "area": {
    #                     "area": 2.0,
    #                     "rule": "5.4.2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.70,
    #                     "rule": "5.8.7"
    #                 },
    #                 "bianqi便器": 1,
    #                 "xiyuqi洗浴器": 1,
    #             },
    #             {
    #                 "name": "卫生间",
    #                 "height": {"height": 2.20, "rule": "5.5.4"},
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "area": {
    #                     "area": 2.0,
    #                     "rule": "5.4.2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.70,
    #                     "rule": "5.8.7"
    #                 },
    #                 "ximianqi洗面器": 1,
    #                 "xiyuqi洗浴器": 1,
    #             },
    #             {
    #                 "name": "卫生间",
    #                 "height": {"height": 2.20, "rule": "5.5.4"},
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "area": {
    #                     "area": 2.0,
    #                     "rule": "5.4.2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.70,
    #                     "rule": "5.8.7"
    #                 },
    #                 "ximianqi洗面器": 1,
    #                 "xiyiji洗衣机": 1,
    #             },
    #             {
    #                 "name": "卫生间",
    #                 "height": {"height": 2.20, "rule": "5.5.4"},
    #                 "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                 "area": {
    #                     "area": 2.0,
    #                     "rule": "5.4.2"
    #                 },
    #                 "door": {
    #                     "height": 2.00,
    #                     "width": 0.70,
    #                     "rule": "5.8.7"
    #                 },
    #                 "bianqi便器": 1,
    #             }
    #         ],
    #         "rule": "5.4.1"
    #     }
    # }

    # data = {
    #     "name": "一室一厅一厨一卫",
    #     "height": {"heigh": 2.80},
    #     "apartment": {
    #         "name": "一室一厅一厨一卫",
    #         "height": {"heigh": 2.80, "rule": "5.5.1"},
    #         "rooms": {
    #             "room": [
    #                     {
    #                         "name": "卧室",
    #                         "area": {
    #                             "area": 9,
    #                             "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于9m2"
    #                         },
    #                         "door": {
    #                             "height": 2.00,
    #                             "width": 0.90,
    #                             "rule": "5.8.7"
    #                         },
    #                         "height": {"height": 2.40, "rule": "5.5.2"},
    #                         "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
    #                         "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
    #
    #                     },
    #                     {
    #                         "name": "卧室",
    #                         "area": {
    #                             "area": 5,
    #                             "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于5m2"
    #                         },
    #                         "door": {
    #                             "height": 2.00,
    #                             "width": 0.90,
    #                             "rule": "5.8.7"
    #                         },
    #                         "height": {"height": 2.40, "rule": "5.5.2"},
    #                         "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
    #                         "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
    #                     },
    #                     {
    #                         "name": "兼起居室",
    #                         "area": {
    #                             "area": 12,
    #                             "rule": "5.2.1卧室的使用面积应符合下列规定：单双卧室不应小于12m2"
    #                         },
    #                         "door": {
    #                             "height": 2.00,
    #                             "width": 0.90,
    #                             "rule": "5.8.7"
    #                         },
    #                         "height": {"height": 2.40, "rule": "5.5.2"},
    #                         "min_part_height": {"min_part_height": 2.10, "rule": "5.5.2"},
    #                         "min_part_area": {"min_part_area": 1 / 3, "rule": "5.5.2"},
    #                     },
    #                 ],
    #             "rule": "5.2.1"
    #         },
    #         "cook_rooms": {
    #             "cook_room": [
    #                 {
    #                     "name": "厨房",
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.80,
    #                         "rule": "5.8.7"
    #                     },
    #                     "area": {
    #                         "area": 4,
    #                         "rule": "5.3.1厨房的使用面积应符合下列规定: 由卧室、起居厅、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于4.0m2"
    #                     }
    #                 },
    #                 {
    #                     "name": "厨房",
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.80,
    #                         "rule": "5.8.7"
    #                     },
    #                     "area": {
    #                         "area": 3.5,
    #                         "rule": "5.3.1厨房的使用面积应符合下列规定: 由兼起居室的卧室、厨房卫生间等组成的住宅套型的厨房使用面积，不应小于3.5m2"
    #                     }
    #                 }
    #             ],
    #             "rule": "5.3.1"
    #         },
    #         "toliets": {
    #             "toliet": [
    #                 {
    #                     "name": "卫生间",
    #                     "height": {"height": 2.20, "rule": "5.5.4"},
    #                     "area": {
    #                         "area": 2.5,
    #                         "rule": "5.4.1"
    #                     },
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.70,
    #                         "rule": "5.8.7"
    #                     },
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "bianqi便器": 1,
    #                     "xiyuqi洗浴器": 1,
    #                     "ximianqi洗面器": 1,
    #                 },
    #                 {
    #                     "name": "卫生间",
    #                     "height": {"height": 2.20, "rule": "5.5.4"},
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "area": {
    #                         "area": 1.8,
    #                         "rule": "5.4.2"
    #                     },
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.70,
    #                         "rule": "5.8.7"
    #                     },
    #                     "bianqi便器": 1,
    #                     "ximianji洗面器": 1,
    #                 },
    #                 {
    #                     "name": "卫生间",
    #                     "height": {"height": 2.20, "rule": "5.5.4"},
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "area": {
    #                         "area": 2.0,
    #                         "rule": "5.4.2"
    #                     },
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.70,
    #                         "rule": "5.8.7"
    #                     },
    #                     "bianqi便器": 1,
    #                     "xiyuqi洗浴器": 1,
    #                 },
    #                 {
    #                     "name": "卫生间",
    #                     "height": {"height": 2.20, "rule": "5.5.4"},
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "area": {
    #                         "area": 2.0,
    #                         "rule": "5.4.2"
    #                     },
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.70,
    #                         "rule": "5.8.7"
    #                     },
    #                     "ximianqi洗面器": 1,
    #                     "xiyuqi洗浴器": 1,
    #                 },
    #                 {
    #                     "name": "卫生间",
    #                     "height": {"height": 2.20, "rule": "5.5.4"},
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "area": {
    #                         "area": 2.0,
    #                         "rule": "5.4.2"
    #                     },
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.70,
    #                         "rule": "5.8.7"
    #                     },
    #                     "ximianqi洗面器": 1,
    #                     "xiyiji洗衣机": 1,
    #                 },
    #                 {
    #                     "name": "卫生间",
    #                     "height": {"height": 2.20, "rule": "5.5.4"},
    #                     "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
    #                     "area": {
    #                         "area": 2.0,
    #                         "rule": "5.4.2"
    #                     },
    #                     "door": {
    #                         "height": 2.00,
    #                         "width": 0.70,
    #                         "rule": "5.8.7"
    #                     },
    #                     "bianqi便器": 1,
    #                 }
    #             ],
    #             "rule": "5.4.1"
    #         }
    #     },
    #     "environment": {
    #
    #     }
    # }
    apartment = {
        "name": "户型",
        "height": {"heigh": 2.80, "rule": "5.5.1"},
        "rooms": {
            "room": [
                {
                    "name": "卧室",
                    "area": {
                        "area": 9,
                        "rule": "5.2.1"
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
                    "name": "卧室",
                    "area": {
                        "area": 5,
                        "rule": "5.2.1"
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
                        "rule": "5.2.1"
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
            ],
            "rule": "5.2.1"
        },
        "cook_rooms": {
            "cook_room": [
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
                        "rule": "5.3.1"
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
                        "rule": "5.3.1"
                    }
                }
            ],
            "rule": "5.3.1"
        },
        "toliets": {
            "toliet": [
                {
                    "name": "卫生间",
                    "height": {"height": 2.20, "rule": "5.5.4"},
                    "area": {
                        "area": 2.5,
                        "rule": "5.4.1"
                    },
                    "door": {
                        "height": 2.00,
                        "width": 0.70,
                        "rule": "5.8.7"
                    },
                    "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                    "bianqi": 1,
                    "xiyuqi": 1,
                    "ximianqi": 1,
                    "xiyiji": 0,
                },
                {
                    "name": "卫生间",
                    "height": {"height": 2.20, "rule": "5.5.4"},
                    "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                    "area": {
                        "area": 1.8,
                        "rule": "5.4.2"
                    },
                    "door": {
                        "height": 2.00,
                        "width": 0.70,
                        "rule": "5.8.7"
                    },
                    "bianqi": 1,
                    "ximianqi": 1,
                    "xiyuqi": 0,
                    "xiyiji": 0,
                },
                {
                    "name": "卫生间",
                    "height": {"height": 2.20, "rule": "5.5.4"},
                    "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                    "area": {
                        "area": 2.0,
                        "rule": "5.4.2"
                    },
                    "door": {
                        "height": 2.00,
                        "width": 0.70,
                        "rule": "5.8.7"
                    },
                    "bianqi": 1,
                    "xiyuqi": 1,
                    "ximianqi": 0,
                    "xiyiji": 0,
                },
                {
                    "name": "卫生间",
                    "height": {"height": 2.20, "rule": "5.5.4"},
                    "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                    "area": {
                        "area": 2.0,
                        "rule": "5.4.2"
                    },
                    "door": {
                        "height": 2.00,
                        "width": 0.70,
                        "rule": "5.8.7"
                    },
                    "ximianqi": 1,
                    "xiyuqi": 1,
                    "bianqi": 0,
                    "xiyiji": 0,
                },
                {
                    "name": "卫生间",
                    "height": {"height": 2.20, "rule": "5.5.4"},
                    "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                    "area": {
                        "area": 2.0,
                        "rule": "5.4.2"
                    },
                    "door": {
                        "height": 2.00,
                        "width": 0.70,
                        "rule": "5.8.7"
                    },
                    "ximianqi": 1,
                    "xiyiji": 1,
                    "bianqi": 0,
                    "xiyuqi": 0,
                },
                {
                    "name": "卫生间",
                    "height": {"height": 2.20, "rule": "5.5.4"},
                    "water_distince": {"water_distince": 1.90, "rule": "5.5.5"},
                    "area": {
                        "area": 2.0,
                        "rule": "5.4.2"
                    },
                    "door": {
                        "height": 2.00,
                        "width": 0.70,
                        "rule": "5.8.7"
                    },
                    "bianqi": 1,
                    "xiyuqi": 0,
                    "ximianqi": 0,
                    "xiyiji": 0,
                }
            ],
            "rule": "5.4.1"
        }
    }
    common_part = {
        # 安全出口
        "safe_exit": {
            "outside": {
                10: {"bulid_area": 650, "safe_distince": 15, "safe_count": 2, "rule": "6.2.1"},
                18: {"bulid_area": 650, "safe_distince": 10, "safe_count": 2, "rule": "6.2.2"},
                19: {"bulid_area": 0, "safe_distince": 0, "safe_count": 2, "rule": "6.2.3"},
            },
            "safe_out_distince": {"safe_out_distince": 5, "rule": "6.2.4"},
            "stairs_anterroom_door_safe": {"status": 1, "rule": "6.2.5"}
        },
        # 楼梯
        "stair": {
            # 楼梯梯段净宽
            "staircase_ladder": {
                6: {"width": 1.0, "rule": "6.3.1"},
                7: {"width": 1.10, "rule": "6.3.1"}
            },
            # 楼梯水平栏杆的长度
            "stair_level_long": {
                1.05: {"longth": 0.50, "height": 1.05, "rule": "6.3.2"},
                0.90: {"longth": 0.50, "height": 0.90, "rule": "6.3.2"}
            },
            # 楼梯限制
            "stair_step": {"width": 0.26, "heigh": 0.175, "rule": "6.3.2"},
            # 楼梯平台
            "staircase_platform": {"width": 1.20, "distance_sidewalk": 2.00, "distince_bacheground": 0.10},
            # 剪刀梯
            "scissor_stair": {"status": 1, "staircase_platform_width": 1.30, "rule": "6.3.4"},
            # 楼梯井
            "stairwall": {"status": 1, "width": 0.11, "rule": "6.3.5"}
        },
        # 电梯
        "loft": {
            # 查看电梯是否是安全出口
            "safe_out": {"status": 1, "rule": "6.9.1"},
            # 电梯设置规定
            "loft_type": {
                "loft_type": {
                    "residence":
                        {
                            "single_station": {"lager_loft": 1, "depth": 1.50},
                            "multiple_unilateral": {"lager_loft": 1, "depth": 1.80},
                            "multiple_sides": {"lager_loft": 1, "depth": 3.50}
                        },
                    "public_building":
                        {
                            "single_station": {"lager_loft": 1, "depth": 1.80},
                            "multiple_unilateral": {"lager_loft": 1, "depth": 2.00},
                            "multiple_sides": {"lager_loft": 1, "depth": 4.50}
                        },
                    "hospital":
                        {
                            "single_station": {"lager_loft": 1},
                            "multiple_unilateral": {"lager_loft": 1},
                            "multiple_sides": {"lager_loft": 1}
                        }
                },
                "rule": "6.9.1"
            },
            # 12层以上的电梯廊
            "apart_gallery": {"floor": 12, "count": 1, "width": 1.00, "height": 1.10, "gallery_up_down": 5,
                              "rule": "6.4.4"},
            # 电梯
            "loft_exist": {"height": 16, "floor": 6, "rule": "6.4.1", "status": 1},
            "loft_count": {"loft_count": {12: 1, 13: 2}, "rule": "6.4.2"},
            # 候梯厅深度
            "wait_loft": {"degree": 1.50, "status": 0, "rule": "6.4.6"}
        }
    }
    obj.insertDocument(index="common_part", type='text',
                       body={"any": {"body": common_part}, "timestamp": datetime.now()})
