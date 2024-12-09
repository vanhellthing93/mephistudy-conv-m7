from concurrent import futures
import grpc
import notification_pb2
import notification_pb2_grpc

class NotificationService(notification_pb2_grpc.NotificationServiceServicer):
    def SendNotification(self, request, context):
        notification_id = "notification_" + request.user_id
        return notification_pb2.NotificationResponse(notification_id=notification_id, user_id=request.user_id, message=request.message)

    def GetNotification(self, request, context):
        # Для примера возвращаем фиктивные данные
        return notification_pb2.NotificationResponse(notification_id=request.notification_id, user_id="user_1", message="This is a sample notification")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notification_pb2_grpc.add_NotificationServiceServicer_to_server(NotificationService(), server)
    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
