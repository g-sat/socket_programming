import asyncio
import websockets
import time

connected_clients = set()
collision_window = 0.5  # length of a slot (seconds)
current_slot_packets = []
slot_start_time = None

async def broadcast(message):
    to_remove = []
    for client in connected_clients:
        try:
            await client.send(message)
        except websockets.ConnectionClosed:
            to_remove.append(client)
    for r in to_remove:
        connected_clients.remove(r)

async def process_slot():
    global current_slot_packets
    if len(current_slot_packets) > 1:
        # Collision occurred in this slot
        for ws, _ in current_slot_packets:
            try:
                await ws.send("COLLISION detected in this slot. Please retry after backoff.")
            except websockets.ConnectionClosed:
                pass
    elif len(current_slot_packets) == 1:
        ws, msg = current_slot_packets[0]
        try:
            await ws.send("ACK: Packet transmitted successfully in slot.")
        except websockets.ConnectionClosed:
            pass
    # Clear slot buffer
    current_slot_packets = []

async def slot_timer():
    global slot_start_time
    while True:
        slot_start_time = time.time()
        # Debug print slot start
        print(f"[Server] Slot started at {slot_start_time:.2f}")
        await asyncio.sleep(collision_window)
        await process_slot()

async def slotted_aloha_server(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"[Server] Received message: {message}")
            now = time.time()
            if slot_start_time is None:
                # Slot timer not started yet, ignore message or you can buffer
                continue
            if now - slot_start_time < collision_window:
                current_slot_packets.append((websocket, message))
            else:
                try:
                    await websocket.send("Packet arrived outside current slot, drop or wait.")
                except websockets.ConnectionClosed:
                    pass
    except websockets.ConnectionClosed:
        print("[Server] Connection closed by client")
    except Exception as e:
        print(f"[Server] Error: {e}")
    finally:
        connected_clients.remove(websocket)

async def main():
    print("Starting Slotted ALOHA server on ws://localhost:8765")
    async with websockets.serve(slotted_aloha_server, "localhost", 8765):
        # Run slot timer concurrently
        asyncio.create_task(slot_timer())
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
