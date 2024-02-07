from fastapi import FastAPI,Request, HTTPException
from typing import List
from fastapi.middleware.cors import CORSMiddleware
# from extraction.capture import capture_image as CR
from extraction.capture import print_barCode as printer

from fastapi.responses import JSONResponse
from config.config_parser import config
import json
# from utils.database import db 
from utils.print_barcode import PrintBarcode as PB
from utils import json_load
# from utils.json_file_update import UpdateJsonFile

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mongo_uri = config.get('MongoDb','data_base_url')
# database_name = config.get('MongoDb','data_base')
# collection_reelstock = config.get("MongoDb", "collection_reelstock")
# collection_reelstock = db[collection_reelstock]
json_file_load = json_load.json_file_read()
# json_file_modifier = UpdateJsonFile()
data_extractor_file_path = config.get("JsonFiles","data_extractor_file")
print("Fast Api Server Connected!")

# @app.post("/scanner/")
# async def read_items(request:Request):
#     print("scanner ................")
#     raw_body = await request.body()
#     try:
#         extracted_info = json.loads(raw_body.decode("utf-8"))
#         json_file_load.json_data_write(data_extractor_file_path,extracted_info)
#         info = CR()
#         return {"data": info,"message": "Raw body received successfully"}
#     except Exception as e:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": "There goes my error"},
        # )
    
@app.post("/printer/")
async def read_items(request:Request):
    print('im in printer function')
    raw_body = await request.body()
    try:
        json_data = json.loads(raw_body.decode("utf-8"))
        print("json_data")
        # print("Data Value:", json_data)
        print_barCode = printer(json_data)
        return {"message": "Raw body received successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=404,
            detail=f"{e} not found",
            headers={"X-Error": "There goes my error"},
        )

@app.post("/bin-printer/")
async def read_items(request:Request):
    print('im in Bin-printer function')
    raw_body = await request.body()
    try:
        json_data = json.loads(raw_body.decode("utf-8"))
        print("Recieved Data:", json_data)
        print_barCode = PB.print_bin_qrcode(json_data)
        return {"message": "Raw body received successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=404,
            detail=f"{e} not found",
            headers={"X-Error": "There goes my error"},
        )
