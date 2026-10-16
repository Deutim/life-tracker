from fastapi import FastAPI

app = FastAPI()


@app.get("/habitos")
def listar_habitos():
    return [
        {"id": 1, "nome": "Arrumar a cama"},
        {"id": 2, "nome": "Oração AM"},
        {"id": 3, "nome": "Higiene"}
    ]