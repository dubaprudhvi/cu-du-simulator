from utils.imports import *

import mplane.notification_service_pb2 as notification_service_pb2
import mplane.notification_service_pb2_grpc as notification_service_pb2_grpc


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
                        payload=self.generate_performance_payload()
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
 
    def generate_performance_payload(self):
        
        hostname = random.choice(config['MPLANEPERFORMANCE']['NODE'])
        ru_id = random.choice(config['MPLANEPERFORMANCE']['RU_ID_LIST'])
        
        payload= {
            "hostname": hostname,
            "o-ran-performance-management:rx-window-stats": [
            {
            "eaxc-measured-result": [
                {
                "count": "0",
                "eaxc-id": 0,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 1,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 2,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 3,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 12,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 13,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 14,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 15,
                "transport-name": "element1"
                }
            ],
            "end-time": "2025-12-15T07:39:15+00:00",
            "measurement-object": "RX_EARLY",
            "start-time": "2025-12-15T07:38:45+00:00"
            },
            {
            "eaxc-measured-result": [
                {
                "count": "0",
                "eaxc-id": 0,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 1,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 2,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 3,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 12,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 13,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 14,
                "transport-name": "element1"
                },
                {
                "count": "0",
                "eaxc-id": 15,
                "transport-name": "element1"
                }
            ],
            "end-time": "2025-12-15T07:39:15+00:00",
            "measurement-object": "RX_CORRUPT",
            "start-time": "2025-12-15T07:38:45+00:00"
            }
        ],
        "o-ran-performance-management:transceiver-stats": [
            {
            "end-time": "2025-12-15T07:39:15+00:00",
            "measurement-object": "RX_POWER",
            "start-time": "2025-12-15T07:38:45+00:00",
            "transceiver-measurement-result": [
                {
                "first": {
                    "time": "2025-12-15T07:38:45+00:00",
                    "value": "1.327"
                },
                "latest": {
                    "time": "2025-12-15T07:38:45+00:00",
                    "value": "1.3113"
                },
                "max": {
                    "time": "2025-12-15T07:38:48+00:00",
                    "value": "1.3532"
                },
                "min": {
                    "time": "2025-12-15T07:38:57+00:00",
                    "value": "1.2895"
                },
                "object-unit-id": 1
                }
            ]
            },
            {
            "end-time": "2025-12-15T07:39:15+00:00",
            "measurement-object": "TEMPERATURE",
            "start-time": "2025-12-15T07:38:45+00:00",
            "transceiver-measurement-result": [
                {
                "first": {
                    "time": "2025-12-15T07:38:46+00:00",
                    "value": "41.5156"
                },
                "latest": {
                    "time": "2025-12-15T07:38:46+00:00",
                    "value": "41.4023"
                },
                "max": {
                    "time": "2025-12-15T07:38:46+00:00",
                    "value": "41.5469"
                },
                "min": {
                    "time": "2025-12-15T07:39:13+00:00",
                    "value": "41.3633"
                },
                "object-unit-id": 1
                }
            ]
            }
        ],
        "ru_id": ru_id
        }
        print(payload)
        return json.dumps(payload)

def mplane_performance():
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

