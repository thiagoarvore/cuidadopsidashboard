import streamlit as st
from accounts.page import show_patients, show_therapists
from treatments.page import show_treatments
from calendars.page import show_calendars
from login.page import show_login
from home.page import show_home


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início', 'Terapeutas', 'Pacientes', 'Horários', 'Tratamentos']
        )
        if menu_option == 'Início':
            show_home()
        if menu_option == 'Terapeutas':
            show_therapists()
        if menu_option == 'Pacientes':
            show_patients()
        if menu_option == 'Horários':
            show_calendars()
        if menu_option == 'Tratamentos':
            show_treatments()


if __name__ == '__main__':
    main()
