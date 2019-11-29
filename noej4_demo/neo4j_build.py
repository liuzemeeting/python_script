#coding:utf-8
from py2neo import Graph, Node, Relationship


# 连接noe4j数据库
graph = Graph('http://192.168.99.100:7474', username="neo4j", password="123456")
# nodes = Graph.nodes
if __name__ == "__main__":
    # 创建住宅
    residence = Node('House', name="住宅")
    graph.create(residence)
    # 创建套型
    jacket_space = Node("Build", name="套内空间")   # 套内空间
    betroom = Node("room", name="卧室")               # 卧室
    living_room = Node("room", name="起居厅")       # 起居厅
    Kitchen = Node("Kitchen", name="厨房")            # 厨房
    toilet = Node("toilet", name="卫生间")               # 卫生间
    door = Node("door", name="门")                     # 门
    window = Node("window", name="窗户")               # 窗户
    # 创建公共部分
    public_space = Node("Build", name="公共部分")   # 公共部分
    floor = Node("public", name="楼层")                # 楼层
    Stairs = Node("public", name="楼梯")              # 楼梯
    Aisle = Node("public", name="过道")                # 过道
    lift = Node("public", name="电梯")                  # 电梯
    # 室内环境
    room_environment = Node("Build", name="室内环境")  # 室内环境
    sunshine = Node("environment", name="光线")            # 光线
    wind = Node("environment", name="通风")                    # 通风
    for item in [jacket_space, betroom, living_room, Kitchen, toilet, Aisle, door, window, public_space, floor, Stairs,
                 lift, room_environment, sunshine, wind]:
        graph.create(item)
    # 创建关系
    # 住宅之间的关系
    residence_relation_jacket = Relationship(residence, "包含", jacket_space)
    residence_relation_public = Relationship(residence, "包含", public_space)
    residence_relation_environment = Relationship(residence, "包含", room_environment)
    # 创建套型与其他关系
    jacket_relation_residence = Relationship(jacket_space, "属于", residence)
    jacket_relation_betroom = Relationship(jacket_space, "包含", betroom)
    jacket_relation_living = Relationship(jacket_space, "包含", living_room)
    jacket_relation_kitchen = Relationship(jacket_space, "包含", Kitchen)
    jacket_relation_toilet = Relationship(jacket_space, "包含", toilet)
    jacket_relation_door = Relationship(jacket_space, "包含", door)
    jacket_relation_window = Relationship(jacket_space, "包含", window)
    # 创建房间与其他关系
    betroom_relation_jacket = Relationship(betroom, "属于", jacket_space)
    betroom_relation_living = Relationship(betroom, "相对", living_room)
    betroom_relation_Kitchen = Relationship(betroom, "相对", Kitchen)
    betroom_relation_toilet = Relationship(betroom, "相对", toilet)
    betroom_relation_Aisle = Relationship(betroom, "相对", Aisle)
    betroom_relation_door = Relationship(betroom, "包含", door)
    betroom_relation_window = Relationship(betroom, "包含", window)
    betroom_relation_sunshine = Relationship(betroom, "相对", sunshine)
    betroom_relation_wind = Relationship(betroom, "相对", wind)
    # 创建客厅与其他关系
    living_relation_jacket = Relationship(living_room, "属于", jacket_space)
    living_relation_betroom = Relationship(living_room, "相对", betroom)
    living_relation_Kitchen = Relationship(living_room, "属于", Kitchen)
    living_relation_Aisle = Relationship(living_room, "相对", Aisle)
    living_relation_toilet = Relationship(living_room, "属于", toilet)
    living_relation_door = Relationship(living_room, "包含", door)
    living_relation_window = Relationship(living_room, "包含", window)
    # 创建厨房与其他关系
    Kitchen_living_jacket = Relationship(Kitchen, "属于", jacket_space)
    Kitchen_relation_door = Relationship(Kitchen, "包含", door)
    Kitchen_relation_window = Relationship(Kitchen, "包含", window)
    Kitchen_relation_sunshine = Relationship(betroom, "相对", sunshine)
    Kitchen_relation_wind = Relationship(betroom, "相对", wind)
    # 创建卫生间与其他关系
    toilet_living_jacket = Relationship(Kitchen, "属于", jacket_space)
    toilet_relation_door = Relationship(Kitchen, "包含", door)
    toilet_relation_window = Relationship(Kitchen, "包含", window)
    toilet_relation_sunshine = Relationship(betroom, "相对", sunshine)
    toilet_relation_wind = Relationship(betroom, "相对", wind)
    # 创建公共部分楼层之间的关系
    public_relation_floor = Relationship(public_space, "包含", floor)
    public_relation_Aisle = Relationship(public_space, "包含", Aisle)
    public_relation_Stairs = Relationship(public_space, "包含", Stairs)
    public_relation_lift = Relationship(public_space, "包含", lift)

    floor_relation_public = Relationship(floor, "属于", public_space)
    floor_relation_Aisle = Relationship(floor, "相对", Aisle)
    floor_relation_Stairs = Relationship(floor, "相对", Stairs)
    floor_relation_lift = Relationship(floor, "相对", lift)

    Aisle_relation_public = Relationship(Aisle, "属于", public_space)
    Aisle_relation_floor = Relationship(Aisle, "相对", floor)
    Aisle_relation_Stairs = Relationship(Aisle, "相对", Stairs)
    Aisle_relation_lift = Relationship(Aisle, "相对", lift)

    Stairs_relation_public = Relationship(Stairs, "属于", public_space)
    Stairs_relation_floor = Relationship(Stairs, "相对", floor)
    Stairs_relation_Aisle = Relationship(Stairs, "相对", Aisle)
    Stairs_relation_lift = Relationship(Stairs, "相对", lift)

    lift_relation_public = Relationship(lift, "属于", public_space)
    lift_relation_floor = Relationship(lift, "相对", floor)
    lift_relation_Aisle = Relationship(lift, "相对", Aisle)
    lift_relation_Stairs = Relationship(lift, "相对", Stairs)
    # 环境部分
    environment_relation_sunshine = Relationship(room_environment, "包含", sunshine)
    environment_relation_wind = Relationship(room_environment, "包含", wind)

    sunshine_relation_environment = Relationship(sunshine, "包含", room_environment)
    wind_relation_environment = Relationship(wind, "包含", room_environment)
    for item in [wind_relation_environment, sunshine_relation_environment, environment_relation_wind,
                 environment_relation_sunshine, lift_relation_Stairs, Stairs_relation_Aisle, Stairs_relation_floor,
                 Stairs_relation_public, Aisle_relation_lift, Aisle_relation_Stairs, floor_relation_Aisle,
                 floor_relation_public, public_relation_lift, public_relation_Stairs, public_relation_Aisle,
                 public_relation_floor,toilet_living_jacket,  toilet_relation_door, toilet_relation_window,
                 toilet_relation_sunshine, toilet_relation_wind, Kitchen_living_jacket, Kitchen_relation_door,
                 Kitchen_relation_window, Kitchen_relation_sunshine, Kitchen_relation_wind,living_relation_window,
                 living_relation_door, living_relation_toilet, living_relation_Aisle, living_relation_Kitchen,
                 living_relation_betroom, living_relation_jacket, betroom_relation_wind, betroom_relation_sunshine,
                 betroom_relation_window, betroom_relation_door, betroom_relation_Aisle, betroom_relation_toilet,
                 betroom_relation_Kitchen, betroom_relation_living, betroom_relation_jacket, jacket_relation_residence,
                 jacket_relation_betroom, jacket_relation_living, jacket_relation_kitchen, jacket_relation_toilet,
                 jacket_relation_door, jacket_relation_window, residence_relation_jacket, residence_relation_public,
                 residence_relation_environment]:
        graph.create(item)








