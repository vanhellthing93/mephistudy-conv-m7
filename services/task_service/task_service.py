from concurrent import futures
import grpc
import task_pb2
import task_pb2_grpc

class TaskService(task_pb2_grpc.TaskServiceServicer):
    def CreateTask(self, request, context):
        task_id = "task_" + request.title
        return task_pb2.TaskResponse(task_id=task_id, title=request.title, description=request.description, user_id=request.user_id)

    def GetTask(self, request, context):
        # Для примера возвращаем фиктивные данные
        return task_pb2.TaskResponse(task_id=request.task_id, title="Sample Task", description="This is a sample task", user_id="user_1")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port('[::]:5002')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
