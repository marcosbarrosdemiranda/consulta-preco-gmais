import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 48291))
    print(f"==================================================")
    print(f" Servidor Local Gmais — Multi-Loja + Painel Admin ")
    print(f" Endereço Kiosk: http://{host}:{port}")
    print(f" Painel Admin:   http://{host}:{port}/admin")
    print(f" Porta Incomum:  {port}")
    print(f"==================================================")
    uvicorn.main(["main:app", f"--host={host}", f"--port={port}", "--reload"])
