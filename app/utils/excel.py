import pandas as pd
from fastapi.responses import FileResponse
import os

def excel_response(filename: str, columns: list, data):

    df = pd.DataFrame(data, columns=columns)
    # if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
    
    filepath = os.path.join("exports", filename)
    os.makedirs("exports", exist_ok=True)  # Ensure the directory exists
    df.to_excel(filepath, index=False)

    return FileResponse(
        path=filepath,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )