from concurrent import futures
import grpc
import studentinfo_pb2
import studentinfo_pb2_grpc

class StudentInfoServicer(studentinfo_pb2_grpc.StudentInfoServicer):
    def __init__(self):
        self.db = {}

    def Add(self, request, context):
        self.db[request.id] = request
        return studentinfo_pb2.StudentResponse(message="Student added successfully")

    def QueryByID(self, request, context):
        student = self.db.get(request.id, None)
        if student is None:
            return studentinfo_pb2.StudentResponse(message="Student not found")
        else:
            return student

    def QueryByName(self, request, context):
        students = [s for s in self.db.values() if s.name == request.name]
        return studentinfo_pb2.StudentsResponse(students=students)

    def Delete(self, request, context):
        if request.id in self.db:
            del self.db[request.id]
            return studentinfo_pb2.StudentResponse(message="Student deleted successfully")
        else:
            return studentinfo_pb2.StudentResponse(message="Student not found")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    studentinfo_pb2_grpc.add_StudentInfoServicer_to_server(StudentInfoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':

    serve()
