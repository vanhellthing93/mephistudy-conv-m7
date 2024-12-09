from concurrent import futures
import grpc
import user_pb2
import user_pb2_grpc

class UserService(user_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        user_id = "user_" + request.email
        return user_pb2.UserResponse(user_id=user_id, name=request.name, email=request.email)

    def GetUser(self, request, context):
        # Для примера возвращаем фиктивные данные
        return user_pb2.UserResponse(user_id=request.user_id, name="John Doe", email="john.doe@example.com")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
