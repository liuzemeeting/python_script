#coding:utf-8
from py2neo import Graph, Node, Relationship


# 连接noe4j数据库 
graph = Graph('http://192.168.99.100:7474', username="neo4j", password="123456")
# nodes = Graph.nodes
if __name__ == "__main__":
    # 创建结点
    wall = Node('House', name="residence")
    nodes = graph.nodes
    data = nodes.match("Build_Test", name="门")
    door = Node('Build_Test', name="门口")
    graph.create(door)
    door_belong_door = Relationship(door, "属于", data)
    data = graph.run('START n=node(1) RETURN n')
    data = graph.data(f'MATCH (r) WHERE id(r) = 60 RETURN r')
    print("data", data)
    graph.run('match(p:Build_Test{id:100}) detach  delete p')
    graph.run('MATCH (r) WHERE id(r) = 100 DELETE r')
    graph.create(door_belong_door)
    for i in nodes:
        print(i)
    relations = graph.relationships.match("Build_Test", name="属于")
    print(relations)
    for item in graph.relationships:
        print(item)
    door = Node('Build_Test', name="门")
    window = Node('Build_Test', name="窗户")
    room = Node('Build_Test', name="房间")
    graph.create(wall)
    graph.create(door)
    graph.create(window)
    graph.create(room)
    wall_belong_room = Relationship(wall, "属于", room)
    door_belong_room = Relationship(door, "属于", room)
    window_belong_room = Relationship(window, "属于", room)
    graph.create(wall_belong_room)
    graph.create(door_belong_room)
    graph.create(window_belong_room)


# test_node_3 = Node('Family', name="小明孙", age="20")
#
# graph.create(test_node_1)
# graph.create(test_node_2)
# # graph.create(test_node_3)
# print("graph", graph)
# print("test_node_1", test_node_1)
#
#
# # 创建关系
# node_1_zhangfu_node_1 = Relationship(test_node_1, "爱人", test_node_2)
# node_2_qizi_node_1 = Relationship(test_node_2, "爱人", test_node_1)
# node_1_zhangfu_node_11 = Relationship(test_node_1, "夫妻", test_node_2)
# node_2_qizi_node_11 = Relationship(test_node_2, "夫妻", test_node_1)
# node_1_zhangfu_node_111 = Relationship(test_node_1, "男朋友", test_node_2)
# node_2_qizi_node_111 = Relationship(test_node_2, "女朋友", test_node_1)
# node_1_zhangfu_node_1211 = Relationship(test_node_1, "丈夫", test_node_2)
# node_2_qizi_node_1121 = Relationship(test_node_2, "妻子", test_node_1)
#
# # node_1_qizi_node_3 = Relationship(test_node_1, "grandfather", test_node_3)
# # node_3_qizi_node_1 = Relationship(test_node_3, "grandson", test_node_1)
# # node_2_qizi_node_3 = Relationship(test_node_2, "brother", test_node_3)
# # node_3_qizi_node_2 = Relationship(test_node_3, "mother", test_node_2)
# graph.create(node_1_zhangfu_node_1)
# graph.create(node_2_qizi_node_1)
# graph.create(node_1_zhangfu_node_11)
# graph.create(node_2_qizi_node_11)
# graph.create(node_1_zhangfu_node_111)
# graph.create(node_2_qizi_node_111)
# graph.create(node_1_zhangfu_node_1211)
# graph.create(node_2_qizi_node_1121)
# print("node_2_qizi_node_1", node_2_qizi_node_1, type(node_2_qizi_node_1))
#
# print(graph.run("MATCH(p:Person) return p").data())
# nodes = graph.nodes
# n = nodes.match("Home_Test", name="men")
# print(n)
# for i in n:
#     print("ffffffff")
#     print(i, type(i))
#     name = i["age"]
#     print(name)


# b=list(nodematcher.match(age=3))[0]