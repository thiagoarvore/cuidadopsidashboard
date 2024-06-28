import requests
import streamlit as st
from login.service import logout


class CalendarsRepository:

    def __init__(self):
        self.__base_url = 'https://www.cuidadopsi.com.br/api/v1/'
        self.__calendars_url = f'{self.__base_url}calendars/'
        self.__status_url = f'{self.__calendars_url}stats/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_calendars(self):
        response = requests.get(
            self.__calendars_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter os perfis. Status code: {response.status_code}')

    def get_calendar_stats(self):
        response = requests.get(
            self.__status_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter os perfis. Status code: {response.status_code}')
