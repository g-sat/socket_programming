<!--
   _____             _        _     _   _                                      
  / ____|           | |      | |   | | (_)                                     
 | (___   ___  _   _| |_ __ _| |__ | |_ _ _ __   __ _                          
  \___ \ / _ \| | | | __/ _` | '_ \| __| | '_ \ / _` |                         
  ____) | (_) | |_| | || (_| | | | | |_| | | | | (_| |                         
 |_____/ \___/ \__,_|\__\__,_|_| |_|\__|_|_| |_|\__, |                         
                                               __/ |                         
                                              |___/                          
-->
# 🚦 SOCKET PROGRAMMING PROJECTS 🚦

> **NOTICE:**  
> This repository is for educational and experimental use only.  
> ⚠️ Use at your own risk! Collisions, chaos, and learning ahead! ⚠️

---

## 🌐 CONTENTS

```
socket_programming/
├── ALOHA/
│   ├── pure_ALOHA/
│   │   ├── Client.py
│   │   ├── Server.py
│   │   └── README.md
│   ├── slotted_ALOHA/
│   │   ├── Client.py
│   │   ├── Server.py
│   │   └── README.md
│   └── README.md
├── README.md  # (this file)
└── (add your own protocols!)
```

- **ALOHA**
  - `pure_ALOHA`: Classic Pure ALOHA protocol simulation.
  - `slotted_ALOHA`: Improved Slotted ALOHA protocol simulation.

---

## 🤖 ABOUT

This repo is a digital playground for classic network protocol simulations using Python's `asyncio` and `websockets`.  
Each protocol is implemented with a server and multiple clients to simulate real-world network behavior, including **collisions** and **retransmissions**.

---

## 🚀 HOW TO USE

1. **Pick a protocol:**  
   Navigate to `pure_ALOHA` or `slotted_ALOHA`.

2. **Read the README:**  
   Each protocol folder has its own README with instructions.

3. **Install dependencies:**  
   ```bash
   pip install websockets
   ```

4. **Run the server:**  
   ```bash
   python3 Server.py
   ```

5. **Run one or more clients (in separate terminals):**  
   ```bash
   python3 Client.py
   ```

---

## ⚙️ REQUIREMENTS

- Python 3.7 or higher
- `websockets` Python package

---

## ⚡ WARNINGS & NOTICES

- 🧪 **For learning only!** Not for production use.
- 💥 **Collisions are simulated**—expect chaos!
- 🛠️ **Tweak parameters** in the code to experiment with protocol performance.
- 📚 **Extend this repo** with your own protocols and experiments!

---

## 🏗️ FUTURE IDEAS

- Add more protocols (CSMA/CD, Token Ring, etc.)
- Visualize collisions and throughput
- Add logging and analytics

---

> **"Plug in, power up, and let the packets fly!"**

