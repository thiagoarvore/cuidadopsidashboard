import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from treatments.service import TreatmentsService


def show_treatments():
    st.write('Estatísticas de tratamentos')
    treatment_service = TreatmentsService()
    treatments = treatment_service.get_treatments()
    treatments_stats = treatment_service.get_treatment_stats()

    def create_card(title, content):
        card_html = f"""
        <div style="background-color:#f9f9f9;padding:20px;border-radius:10px;
             box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2);margin:10px;">
            <h4 style="color:#333;">{title}</h4>
            <h3 class="text-center" style="color:#777;">{content}</h3>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        create_card('Tratamentos em andamento', treatments_stats['ongoing_treatments'])
    with col2:
        pass
    if treatments:
        treatments_df = pd.json_normalize(treatments)
        treatments_df = treatments_df.drop(columns=['id'], errors='ignore')
        column_order = ['therapist.name', 'patient.name', 'schedule.week_day', 'schedule.schedule', 'is_active']
        treatments_df = treatments_df[column_order]
        column_names = {
            'therapist.name': 'Terapeuta',
            'patient.name': 'Paciente',
            'schedule.week_day': 'Dia da semana',
            'schedule.schedule': 'Horário',
            'is_active': 'Ativo/Inativo'
        }
        treatments_df = treatments_df.rename(columns=column_names)
        AgGrid(
            data=pd.DataFrame(treatments_df),
            reload_data=True,
            key='treatments_grid'
        )
    else:
        st.warning('Nenhum terapeuta cadastrado')
