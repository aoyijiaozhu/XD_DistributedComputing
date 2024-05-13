import grpc
import studentinfo_pb2
import studentinfo_pb2_grpc

def print_student_info(student):
    print("------------------------")
    print(f"学生ID: {student.id}")
    print(f"姓名: {student.name}")
    print(f"年龄: {student.age}")
    print(f"班级: {student.class_}")
    print("------------------------")


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = studentinfo_pb2_grpc.StudentInfoStub(channel)
        while True:
            print("查询方式：\n"
                      "1.添加学生信息\n"
                      "2.按ID查询\n"
                      "3.按姓名查询\n"
                      "4.按ID删除\n"
                      "q.退出\n")
            a=input("请输入：")

            if(a=='q'):
                print('已退出')
                break
            elif(a=="1"):
                id = input("请输入学生ID：")
                name = input("请输入学生姓名：")
                age = int(input("请输入学生年龄："))
                class_ = input("请输入学生班级：")
                response = stub.Add(studentinfo_pb2.StudentRequest(id=id, name=name, age=age, class_=class_))
                print(response.message)

            elif(a=="2"):
                id = input("请输入学生ID：")
                response = stub.QueryByID(studentinfo_pb2.StudentByIDRequest(id=id))
                print(response)
            elif (a == "3"):
                name = input("请输入学生姓名：")
                response = stub.QueryByName(studentinfo_pb2.StudentByNameRequest(name=name))
                print(response.students)
            elif (a == "4"):
                id = input("请输入学生ID：")
                response = stub.Delete(studentinfo_pb2.StudentByIDRequest(id=id))
                print(response.message)
            else:
                print('error!')

if __name__ == '__main__':
    run()
