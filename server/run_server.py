import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    print(f"==================================================")
    print(f" Iniciando Servidor Local - Consulta Preço Gmais  ")
    print(f" Endereço: http://{host}:{port}")
    print(f" API RP Info Host: {os.getenv('RP_HOST', 'http://servicosflex.rpinfo.com.br:9000')}")
    print(f"==================================================")
    uvicorn.main(["main:app", f"--host={host}", f"--port={port}", "--reload"])
