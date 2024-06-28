import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from calendars.service import CalendersService


def show_calendars():
    st.write('Estatísticas de Horários Disponíveis')
    account_service = CalendersService()
    calendars = account_service.get_calendars()
    col1, cols = st.columns(2)
    if calendars:
        calendars_df = pd.json_normalize(calendars)
        calendars_df = calendars_df.drop(columns=['id'], errors='ignore')
        column_order = ['therapist.name', 'week_day', 'schedule', 'is_active']
        calendars_df = calendars_df[column_order]
        column_names = {
            'therapist.name': 'Terapeuta',
            'week_day': 'Dia da semana',
            'schedule': 'Horário',
            'is_active': 'Ativo/Inativo'
        }
        calendars_df = calendars_df.rename(columns=column_names)
        AgGrid(
            data=pd.DataFrame(calendars_df),
            reload_data=True,
            key='calendars_grid'
        )
    else:
        st.warning('Nenhum terapeuta cadastrado')
