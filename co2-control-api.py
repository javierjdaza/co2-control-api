from fastapi import FastAPI, Path,HTTPException,status
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from db import fetch_all_co2_data,put_data_co2

class Medicion(BaseModel):
    key : str
    aula : str
    datetime : str
    edificio : str
    medicion : int
    piso : int
    sensor : str


app = FastAPI( title="Co2 Control",
                description="REST API to manage Co2 Data Base connecion \n@Author: Ivan Daniel Maestre Muza",
                version="0.0.1",
                # openapi_tags = [
                #                 {
                #                     "name": "Find Cars",
                #                     "description": "users endpoint"
                #                 }]
                )

@app.get("/fetch/all")
def fetch_all_data():
    all_data_list = fetch_all_co2_data()
    return all_data_list

@app.get('/')
def home():
    html_content = """
                    
                    <html>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
                        <head>
                            <title>CO2 API REST</title>
                        </head>
                        <body>
                            <figure class="text-center">
                                <br>
                                <br>
                                <br>
                                <br>
                                <br>
                                <h1>
                                    <br><strong>CO2 API REST</strong><br>
                                </h1>
                                <h3>
                                    Manage Data Base connection
                                </h3>
                                <br>
                                <h5>
                                    @Authors: Ivan Daniel Maestre Muza
                                </h5>
                            </figure>
                        </body>
                    </html>
                    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/load/data")
def post_message(medicion: Medicion):
    key = medicion.key
    all_data = fetch_all_co2_data()
    all_keys_str = [ i['key'] for i in all_data]
    all_keys_int = [ int(i['key']) for i in all_data]
    max_key = max(all_keys_int)

    if key in all_keys_str:
        raise HTTPException(status_code=404, detail=f"el ultimo valor de key es de: {max_key}, por favor escoge un numero mayor")
    else:
        error_flag = put_data_co2(dict(medicion))
        return 'la medicion ha sido guardada correctamente'
        