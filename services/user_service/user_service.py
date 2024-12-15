import grpc
import user_service_pb2
import user_service_pb2_grpc
from concurrent import futures

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        # Логика создания пользователя
        pass

    def GetUser(self, request, context):
        # Логика получения пользователя
        pass

    def SendMessage(self, request, context):
        with grpc.insecure_channel('order_service:5002') as channel:
            stub = order_service_pb2_grpc.OrderServiceStub(channel)
            response = stub.ReceiveMessage(order_service_pb2.MessageRequest(message=request.message))
            print(f"UserService sent message: {request.message}")
            return user_service_pb2.MessageResponse(status="Message sent")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()