import db
sql = """SELECT id, unit_class_id from mobile_order_region where grade_id=0 and user_type=3"""
data = db.base.fetch_all(sql)
print(data)