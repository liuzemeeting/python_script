from sql_common import db


if __name__ == '__main__':
    sql = """
    select concat("line ",Pointsp," ",Pointep,"  ",
        "-text ",TRUNCATE((convert(SUBSTRING_INDEX(Pointsp,",",1),decimal(16,4))+convert(SUBSTRING_INDEX(Pointep,",",1),decimal(16,4)))/2,4),",",
        TRUNCATE((convert(SUBSTRING_INDEX(Pointsp,",",-1),decimal(16,4))+convert(SUBSTRING_INDEX(Pointep,",",-1),decimal(16,4)))/2,4)," 50 0 ",ele_id," ") 
        from S_Line where ele_id not like 'C:%' and ele_id not like 'U:%' and ele_id not like 'M:%'
    """