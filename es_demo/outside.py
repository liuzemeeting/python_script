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

out_data = {
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

rule = []
safe_exit_data = out_data["safe_exit"]
safe_data_stand = common_part["safe_exit"]
if safe_exit_data["outside"] < 11:
    safe_outside_stand = safe_data_stand["outside"].get(10)
elif safe_exit_data["outside"] < 19:
    safe_outside_stand = safe_data_stand["outside"].get(18)
else:
    safe_outside_stand = safe_data_stand["outside"].get(19)

# 比较安全出口和楼层之间的关系
if safe_exit_data["bulid_area"] < safe_outside_stand["build_area"] or safe_exit_data["safe_distince"] < safe_outside_stand["safe_distince"]:
    if safe_exit_data["safe_count"] < safe_exit_data["safe_count"]:
        out_data["safe_exit"]["status"] = 1
        rule.append(safe_data_stand["rule"])

if safe_exit_data["safe_out_distince"] < safe_data_stand["safe_out_distince"]["safe_out_distince"]:
    out_data["safe_exit"]["status"] = 1
    rule.append(safe_data_stand["safe_out_distince"]["rule"])

if safe_exit_data["stairs_anterroom_door_safe"] < safe_data_stand["stairs_anterroom_door_safe"]["stairs_anterroom_door_safe"]:
    out_data["safe_exit"]["status"] = 1
    rule.append(safe_data_stand["stairs_anterroom_door_safe"]["rule"])


# 比较楼梯
stair_data = out_data["stair"]
stair_data_stand = common_part["stair"]
if stair_data["stair_floor"] < 7:
    stair_floor_data = stair_data_stand["staircase_ladder"].get(6)
else:
    stair_floor_data = stair_data_stand["staircase_ladder"].get(7)
if stair_data["staircase_ladder"]["width"] < stair_floor_data["width"]:
    rule.append(stair_floor_data["rule"])
