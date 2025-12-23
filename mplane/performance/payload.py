from utils.imports import *

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

def generate_performance_payload():       
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
