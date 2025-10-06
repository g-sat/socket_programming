import asyncio
import websockets
import time
import random

async def slotted_aloha_client(client_id):
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            print(f"[Client {client_id}] Connected to server")
            while True:
                # Wait until next slot boundary
                now = time.time()
                slot_length = 0.5  # same as server
                next_slot = (int(now / slot_length) + 1) * slot_length
                wait_time = max(0, next_slot - now)
                await asyncio.sleep(wait_time)

                packet = f"Packet from client {client_id} at slot {int(next_slot)}"
                print(f"[Client {client_id}] Sending: {packet}")
                await websocket.send(packet)

                try:
                    response = await asyncio.wait_for(websocket.recv(), timeout=5)
                    print(f"[Client {client_id}] Received: {response}")
                    if "COLLISION" in response:
                        backoff = random.uniform(1, 3)
                        print(f"[Client {client_id}] Backing off for {backoff:.2f}s due to collision")
                        await asyncio.sleep(backoff)
                except asyncio.TimeoutError:
                    print(f"[Client {client_id}] Timeout waiting for server response")
    except websockets.ConnectionClosed:
        print(f"[Client {client_id}] Connection closed")
    except Exception as e:
        print(f"[Client {client_id}] Error: {e}")


if __name__ == "__main__":
    import random
    client_id = random.randint(1, 100)
    asyncio.run(slotted_aloha_client(client_id))
