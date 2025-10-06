import asyncio
import websockets
import time
import random

async def slotted_aloha_client(client_id):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            # Wait until next slot boundary to send
            now = time.time()
            slot_length = 0.5  # same as server
            next_slot = (int(now / slot_length) + 1) * slot_length
            wait_time = max(0, next_slot - now)
            await asyncio.sleep(wait_time)
            
            packet = f"Packet from client {client_id} at slot {int(next_slot)}"
            print(f"Client {client_id} sending: {packet}")
            await websocket.send(packet)
            response = await websocket.recv()
            print(f"Client {client_id} received: {response}")

            if "COLLISION" in response:
                backoff = random.uniform(1, 3)
                print(f"Client {client_id} backing off for {backoff:.2f}s due to collision")
                await asyncio.sleep(backoff)

if __name__ == "__main__":
    client_id = random.randint(1, 100)
    asyncio.run(slotted_aloha_client(client_id))

