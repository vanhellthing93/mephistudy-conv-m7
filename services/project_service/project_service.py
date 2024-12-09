from concurrent import futures
import grpc
import project_pb2
import project_pb2_grpc

class ProjectService(project_pb2_grpc.ProjectServiceServicer):
    def CreateProject(self, request, context):
        project_id = "project_" + request.name
        return project_pb2.ProjectResponse(project_id=project_id, name=request.name, description=request.description)

    def GetProject(self, request, context):
        # Для примера возвращаем фиктивные данные
        return project_pb2.ProjectResponse(project_id=request.project_id, name="Sample Project", description="This is a sample project")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    project_pb2_grpc.add_ProjectServiceServicer_to_server(ProjectService(), server)
    server.add_insecure_port('[::]:5003')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
