## Configurar environment
Crear env
```bash
python -m venv p2env
```

Activar env Linux
```bash
source p2env/bin/activate
```

Activar env Windows
```bash
p2env\bin\Scripts\activate
```

Instalar dependencias
```bash
pip install -r requirements.txt
```

## Probar endpoint de cliente
Correr app
```bash
python main.py
```

Ejecutar en un browser 
```
http://127.0.0.1:5000/cliente?dni=123456
```