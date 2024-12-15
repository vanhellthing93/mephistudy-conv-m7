import grpc
import order_service_pb2
import order_service_pb2_grpc
from concurrent import futures

class OrderService(order_service_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        # Логика создания заказа
        pass

    def GetOrder(self, request, context):
        # Логика получения заказа
        pass

    def ReceiveMessage(self, request, context):
        print(f"OrderService received message: {request.message}")
        return order_service_pb2.MessageResponse(status="Message received")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_service_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:5002')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()