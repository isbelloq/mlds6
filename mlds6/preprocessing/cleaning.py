"""Cleaning module for Secop Data
"""
import pandas as pd
def cc_filter(secop_i : pd.DataFrame)-> pd.DataFrame:
    """Filter cuantia contrato and valor contrato con adiciones with values greater than 0

    Args:
        secop_i (pd.DataFrame): 
            Secop dataframe  
            
    Returns:
        pd.DataFrame: 
            Filtered dataframe
    """
    return secop_i.query("cuantia_contrato > 0 & valor_contrato_con_adiciones > 0") 

def department_transform(secop_i : pd.DataFrame) -> pd.DataFrame:
    """Transform department column for secop dataframe

    Args:
        secop_i (pd.DataFrame): 
            Secop Dataframe

    Returns:
        pd.DataFrame: 
    """
    secop_i['departamento_entidad'] = secop_i['departamento_entidad'].str.upper()
    return secop_i

def nit_clean(secop_i : pd.DataFrame) -> pd.DataFrame:
    """Clean rows without entity ID

    Args:
        secop_i (pd.DataFrame):  
            Secop Dataframe

    Returns:
        pd.DataFrame: 
    """
    secop_i = secop_i[secop_i['nit_de_la_entidad'] != 'No Definido']
    return secop_i
    
def overrun(secop_i : pd.DataFrame)-> pd.DataFrame:
    """Generate an overrun aditional param

    Args:
        secop_i (pd.DataFrame):
            Secop Dataframe
    Returns:
        pd.DataFrame: 
    """
    secop_i['sobrecosto'] =  (secop_i['valor_total_de_adiciones']/secop_i['cuantia_contrato'] > 0.2 ).astype(int)
    return secop_i
    
    
def drop_empty_values(secop_i : pd.DataFrame):
    """Drop empty and duplicate values

    Args:
        secop_i (pd.DataFrame): 
            Secop Dataframe
    """
    secop_i.dropna(inplace=True)
    secop_i.drop_duplicates(inplace=True)
    
def cop_currency(secop_i : pd.DataFrame) -> pd.DataFrame:
    """sorts only by colombian peso in the moneda column

    Args:
        secop_i (pd.DataFrame): 
            Secop Dataframe

    Returns:
        pd.DataFrame: 
    """
    return secop_i.query("moneda == 'Peso Colombiano'")
    