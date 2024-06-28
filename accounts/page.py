import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from st_aggrid import AgGrid
from accounts.service import AccountsService


def show_therapists():
    st.write('Estatísticas de terapeutas')
    account_service = AccountsService()
    therapists = account_service.get_therapists()
    therapist_stats = account_service.get_account_stats()
    col1, col2 = st.columns(2)

    if therapists:
        with col1:
            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=['Sem E-psi', 'Sem treinamento', 'Sem treinamento nem E-psi', 'Total de Terapeutas'],
                y=[therapist_stats['therapist_no_e_psi_count'],
                   therapist_stats['therapist_no_training_count'],
                   therapist_stats['therapist_no_e_psi_training_count'],
                   therapist_stats['total_therapist_accounts']],
                text=[therapist_stats['therapist_no_e_psi_count'],
                      therapist_stats['therapist_no_training_count'],
                      therapist_stats['therapist_no_e_psi_training_count'],
                      therapist_stats['total_therapist_accounts']],
                textposition='auto',
                name='Terapeutas'
            ))

            fig.update_layout(
                title='Estatísticas de Terapeutas',
                xaxis_title='',
                yaxis_title='Quantidade',
                barmode='group'
            )
            st.plotly_chart(fig)
        with col2:
            fig = px.pie(
                therapist_stats['therapists_by_platform'],
                values='count',
                names='platform',
                title='Plataforma preferida'
            )
            st.plotly_chart(fig)
        therapists_df = pd.json_normalize(therapists)
        columns_to_exclude = ['photo', 'id', 'age', 'address', 'complaint', 'emergency_number', 'user', 'psychiatric', 'uf.id', 'city.id', 'city.UF', 'uf', 'city']
        therapists_df = therapists_df.drop(columns=columns_to_exclude, errors='ignore')
        column_names = {
            'name': 'Terapeuta',
            'whatsapp': 'Whatsapp',
            'crp': 'CRP',
            'e_psi': 'Link para o E-psi',
            'platform': 'Plataforma preferida',
            'trained': 'Treinamento',
            'uf.name': 'Estado',
            'city.name': 'Cidade'
        }
        therapists_df = therapists_df.rename(columns=column_names)
        AgGrid(
            data=pd.DataFrame(therapists_df),
            reload_data=True,
            key='therapist_grid'
        )
    else:
        st.warning('Nenhum terapeuta cadastrado')


def show_patients():
    st.write('Estatísticas de pacientes')
    account_service = AccountsService()
    patients = account_service.get_patients()
    patient_stats = account_service.get_account_stats()
    col1, col2 = st.columns(2)
    by_psyco_df = pd.DataFrame(patient_stats['patient_by_psyco'])
    by_psyco_df['psychiatric'] = by_psyco_df['psychiatric'].map({True: 'Sim', False: 'Não'})

    if patients:
        with col1:
            fig = px.pie(
                by_psyco_df,
                values='count',
                names='psychiatric',
                title='Porcentagem de pacientes com<br>acompanhamento psiquiátrico'
            )
            st.plotly_chart(fig)
        with col2:
            fig = px.pie(
                patient_stats['patient_by_age'],
                values='count',
                names='age',
                title='Idade dos pacientes'
            )
            st.plotly_chart(fig)
        patients_df = pd.json_normalize(patients)
        columns_to_exclude = ['photo', 'id', 'crp', 'crp_check', 'e_psi', 'trained', 'user', 'platform', 'uf.id', 'city.id', 'city.UF', 'uf', 'city']
        patients_df = patients_df.drop(columns=columns_to_exclude, errors='ignore')
        column_names = {
            'name': 'Paciente',
            'whatsapp': 'Whatsapp',
            'age': 'Idade',
            'address': 'Endereço',
            'complaint':'Queixas',
            'psychiatric': 'Acompanhamento psiquiátrico',
            'emergency_number': 'Número de emergência',
            'uf.name': 'Estado',
            'city.name': 'Cidade'
        }
        patients_df = patients_df.rename(columns=column_names)
        AgGrid(
            data=pd.DataFrame(patients_df),
            reload_data=True,
            key='patients_grid'
        )
    else:
        st.warning('Nenhum paciente cadastrado')
