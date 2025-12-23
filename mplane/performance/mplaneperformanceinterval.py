from utils.imports import *

import mplane.notification_service_pb2 as notification_service_pb2
import mplane.notification_service_pb2_grpc as notification_service_pb2_grpc
import mplane.performance.payload as payload

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

class NotificationService(notification_service_pb2_grpc.NotificationService):
    
    def SubscribeNotifications(self, request, context):
        print(f"Client-ID: {request.client_id}")
        
        self._active = True
        
        def send_notifications():
            while self._active and context.is_active():
                try:
                    response = notification_service_pb2.NotificationRequest(
                        type="performance",
                        payload=payload.generate_performance_payload()
                    )
                    yield response
                    time.sleep(config['MPLANEPERFORMANCE']['MESSAGE_FREQUENCY'])
                except Exception as e:
                    print(f"Error sending notification: {e}")
                    break
        
        def on_rpc_done():
            self._active = False
            print("Client disconnected")
        
        context.add_callback(on_rpc_done)
        
        return send_notifications()

def mplane_performance_interval():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
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