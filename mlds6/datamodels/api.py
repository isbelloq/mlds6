from pydantic import BaseModel
from typing import Dict, List


    
class ApiParams(BaseModel):
    """
    Class for API parameters

    Atributes
    ----------
    URL : str
        url where will get the data
    headers: str
        headers of the request
    params: Dict
        aditional params
    """
    URL:str
    headers:Dict[str,str]
    params: Dict
    
    
