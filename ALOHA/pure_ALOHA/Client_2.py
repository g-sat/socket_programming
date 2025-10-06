import asyncio
import websockets
import random
import time

async def aloha_client(client_id):
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                await asyncio.sleep(random.uniform(1, 5))
                packet = f"Packet from client {client_id} at {int(time.time())}"
                print(f"Client {client_id} sending: {packet}")
                await websocket.send(packet)
                response = await websocket.recv()
                print(f"Client {client_id} received: {response}")
                if "COLLISION" in response:
                    backoff = random.uniform(2, 4)
                    print(f"Client {client_id} backing off for {backoff:.2f}s due to collision")
                    await asyncio.sleep(backoff)
    except websockets.ConnectionClosed:
        print(f"Client {client_id} connection closed by server.")
    except Exception as e:
        print(f"Client {client_id} error: {e}")

if __name__ == "__main__":
    client_id = random.randint(1, 100)
    asyncio.run(aloha_client(client_id))
