import streamlit as st
import plotly.express as px
from accounts.service import AccountsService
from calendars.service import CalendersService
from treatments.service import TreatmentsService


def show_home():
    def create_card(title, content):
        card_html = f"""
        <div style="background-color:#f9f9f9;padding:20px;border-radius:10px;
             box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2);margin:10px;">
            <h4 style="color:#333;">{title}</h4>
            <h3 class="text-center" style="color:#777;">{content}</h3>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

    account_service = AccountsService()
    account_stats = account_service.get_account_stats()
    calendar_service = CalendersService()
    calendar_stats = calendar_service.get_calendar_stats()
    treatment_service = TreatmentsService()
    treatment_stats = treatment_service.get_treatment_stats()

    st.title('Cuidado Psi em Rede')
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        with st.container():
            create_card('Total de Terapeutas cadastrados', f'{account_stats["total_therapist_accounts"]}')
        with st.container():
            create_card('Total de horários disponíveis', f'{calendar_stats["total_calendars"]}')

    with col2:
        with st.container():
            create_card('Total de pacientes cadastrados', f'{account_stats["total_patient_accounts"]}')
        with st.container():
            create_card('Total de tratamentos realizados', f'{treatment_stats["total_treatments"]}')
