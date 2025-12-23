from utils.imports import *

import mplane.notification_service_pb2 as notification_service_pb2
import mplane.notification_service_pb2_grpc as notification_service_pb2_grpc
import mplane.performance.payload as payload

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

class NotificationService(notification_service_pb2_grpc.NotificationService):
    def __init__(self):
        self.active_clients = 0
    
    def SubscribeNotifications(self, request, context):
        client_id = request.client_id
        self.active_clients += 1
        print(f"Active clients: {self.active_clients}")
        
        message_count = 0
        
        def send_notifications():
            nonlocal message_count
            for i in range(config['MPLANEPERFORMANCE']['MESSAGE_IN_LIMIT']):
                if not context.is_active():
                    print(f"Client {client_id} cancelled at {message_count}")
                    return
                try:
                    response = notification_service_pb2.NotificationRequest(
                        type="performance",
                        payload=payload.generate_performance_payload()
                    )
                    message_count += 1
                    yield response
                except Exception as e:
                    print(f"Client {client_id} error at {message_count}: {e}")
                    return
            
            print(f"Client {client_id} completed {message_count} messages")
        
        def on_rpc_done():
            nonlocal message_count
            self.active_clients -= 1
            print(f"Client {client_id} disconnected: {message_count} msgs, "
                  f"{self.active_clients} active remaining")
        
        context.add_callback(on_rpc_done)
        return send_notifications()
  
def mplane_performance_limit():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    notification_service_pb2_grpc.add_NotificationServiceServicer_to_server(
        NotificationService(), server
    )
    server.add_insecure_port(f"[::]:{config['MPLANEPERFORMANCE']['PORT']}")
    server.start()
    print("Notification Server started on port 50052")
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped")