from concurrent import futures
import grpc
import comment_pb2
import comment_pb2_grpc

class CommentService(comment_pb2_grpc.CommentServiceServicer):
    def CreateComment(self, request, context):
        comment_id = "comment_" + request.task_id
        return comment_pb2.CommentResponse(comment_id=comment_id, task_id=request.task_id, content=request.content, user_id=request.user_id)

    def GetComment(self, request, context):
        # Для примера возвращаем фиктивные данные
        return comment_pb2.CommentResponse(comment_id=request.comment_id, task_id="task_1", content="This is a sample comment", user_id="user_1")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comment_pb2_grpc.add_CommentServiceServicer_to_server(CommentService(), server)
    server.add_insecure_port('[::]:5004')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
