import asyncio
import websockets
import time

connected_clients = set()
packet_queue = []
collision_window = 0.5  # seconds

async def aloha_server(websocket):
    global packet_queue
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            now = time.time()
            packet_queue.append((now, websocket, message))
            collisions = [p for p in packet_queue if now - p[0] < collision_window]
            if len(collisions) > 1:
                for _, ws, _ in collisions:
                    try:
                        await ws.send("COLLISION detected. Please retry after random backoff.")
                    except websockets.ConnectionClosed:
                        pass
                packet_queue = []
            else:
                await asyncio.sleep(collision_window)
                if packet_queue and packet_queue[0][1] == websocket:
                    try:
                        await websocket.send("ACK: Packet transmitted successfully!")
                    except websockets.ConnectionClosed:
                        pass
                    packet_queue = []
    except websockets.ConnectionClosed:
        pass
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        connected_clients.remove(websocket)

async def main():
    print("Starting ALOHA server on ws://localhost:8765")
    async with websockets.serve(aloha_server, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
