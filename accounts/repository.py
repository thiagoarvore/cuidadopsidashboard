import requests
import streamlit as st
from login.service import logout


class AccountsRepository:

    def __init__(self):
        self.__base_url = 'https://www.cuidadopsi.com.br/api/v1/'
        self.__accounts_url = f'{self.__base_url}accounts/'
        self.__stats_url = f'{self.__accounts_url}stats/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_therapists(self):
        response = requests.get(
            self.__accounts_url,
            headers=self.__headers,
        )
        therapist_list = []
        for therapist in response.json():
            if therapist['crp'] != None:
                therapist_list.append(therapist)
        if response.status_code == 200:
            return therapist_list
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter os perfis. Status code: {response.status_code}')

    def get_patients(self):
        response = requests.get(
            self.__accounts_url,
            headers=self.__headers,
        )
        patient_list = []
        for patients in response.json():
            if patients['age'] != None:
                patient_list.append(patients)
        if response.status_code == 200:
            return patient_list
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter os perfis. Status code: {response.status_code}')

    def get_account_stats(self):
        response = requests.get(
            self.__stats_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter os perfis. Status code: {response.status_code}')
