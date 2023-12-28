import websocket
import threading

"""
docker pull shapr3d/data-engineer-homework
docker run --rm -p 8765:8765 shapr3d/data-engineer-homework
Then run this script.
"""


def on_message(ws, message):
    print(f"Received message: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_open(ws):
    print("Connection opened")


def start_websocket_client():
    websocket_url = "ws://0.0.0.0:8765"  # Replace with your WebSocket URL

    # Create a WebSocket connection
    ws = websocket.WebSocketApp(
        websocket_url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open

    # Start a separate thread for the WebSocket connection
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.daemon = True
    ws_thread.start()

    try:
        # Keep the main thread running to capture KeyboardInterrupt (Ctrl+C)
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping WebSocket client...")
        ws.close()


if __name__ == "__main__":
    start_websocket_client()


