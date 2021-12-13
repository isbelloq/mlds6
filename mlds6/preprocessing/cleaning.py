"""Cleaning module for Secop Data
"""
import pandas as pd


def __set_type_person(contractor_id: str) -> str:
    """set the type category

    Parameters
    ----------
    contractor_id: str
        category of the contractor

    Returns
    -------
    contractor_type
        the contractor type (natural or jurídica)
    """
    PERSONA_NATURAL = ('Carné Diplomático',
                       'Cédula de Ciudadanía',
                       'Cédula de Extranjería',
                       'Nit de Persona Natural',
                       'Número de Fideicomiso',
                       'Nuip',
                       'Pasaporte',
                       'Tarjeta de Identidad')
    PERSONA_JURIDICA = ('Nit de Extranjería',
                        'Nit de Persona Jurídica',
                        'Sociedades Extranjeras'
                        )
    if contractor_id in PERSONA_NATURAL:
        return "Persona natural"
    elif contractor_id in PERSONA_JURIDICA:
        return "Persona jurídica"
    else:
        return "No definido"


def preprocess_pipe(secop_i: pd.DataFrame) -> pd.DataFrame:
    """Preprocess pipeline for the secop dataset

    Parameters
    ----------
    secop_i : pd.DataFrame
        Raw dataframe

    Returns
    -------
    clean_secop_df = pd.DataFrame
        Preprocessed dataset
    """
    clean_secop_df = (
        secop_i
        .query("moneda == 'Peso Colombiano'\
                & nit_de_la_entidad != 'No Definido'\
                & cuantia_contrato > 0\
                & valor_contrato_con_adiciones > 0")
        .assign(
            sobrecosto=lambda df: (
                df['valor_total_de_adiciones']/df['cuantia_contrato'] > 0.2).astype('int'),
            departamento_entidad=lambda df: (df['departamento_entidad']
                                             .str
                                             .upper()
                                             ),
            Tipo_persona=lambda df: df['tipo_identifi_del_contratista'].map(
                __set_type_person)
        )
        .dropna()
        .drop_duplicates()
    )
    return clean_secop_df
