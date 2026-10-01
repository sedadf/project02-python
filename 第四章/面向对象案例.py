#学生类
class Student(object):
    def __init__(self, name, chinese,math,english):
        self.name = name
        self.chinese=chinese
        self.math=math
        self.english=english
def __str__(self):
    return f"姓名：{self.name}| 语文：{self.chinese}| 数学：{self.math}| 英语：{self.english}，总分{self.chinese+self.math+self.english}"


#修改学生成绩
def update_score(self,chinese=None,math=None,english=None):
    if chinese is not None:
        self.chinese=chinese
    if math is not None:
        self.math=math
    if english is not None:
        self.english=english



#教务管理系统
class EduMangement(object):
    system_version="1.0"
    system_name="教务管理系统"
    def __init__(self):
        self.student_list=[]

    #添加
    def add_student(self):
        name=input("姓名")

        #判断，如果存在则失败
        for s in self.student_list:
            if s.name==name:
                print("该学生已经存在")
                return
        chinese=int(input("语文"))
        math=int(input("数学"))
        english=int(input("英语"))
        #判断分数是否在0-100
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu=Student(name,chinese,math,english)
            self.student_list.append(stu)
        else:
            print("分数错误")


    #修改
    def update_student(self):
        name = input("姓名")
        for s in self.student_list:
            if s.name==name:
                print(f"当前成绩{s}")
                chinese = int(input("修改的语文"))
                math = int(input("修改的数学"))
                english = int(input("修改的英语"))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功")
                    print(f"当前成绩{s}")
                    return
                else:
                    print("分数错误")
                    return
        print("未找到该学生，修改失败")
    #删除
    def delete_student(self):
        name = input("姓名")
        for s in self.student_list:
            if s.name==name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("未找到该学生，删除失败")

    #查询
    def query_student(self):
        name = input("姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息{s}")
                return
        print("未找到该学生，查询失败")
    #展示所有学生
    def list_student(self):
        for s in self.student_list:
            print(s)
    #运行系统
    def run(self):
        print(f"欢迎使用{EduMangement.system_version}")


        while True:
            print()
            print("#"*20)
            print("1添加，2修改，3删除，4查询指定，5查询所有，6退出")
            print("#"*20)
            choice=input("请选择操作")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("拜拜")
                        break
                    case _:
                        print("输入错误")
            except Exception :
                print("输入数据有问题,请重新输入")
            except Exception :
                print("程序运行出错，请重新选择")

