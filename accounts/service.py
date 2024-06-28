from accounts.repository import AccountsRepository
import streamlit as st


class AccountsService():

    def __init__(self):
        self.accounts_repository = AccountsRepository()

    def get_therapists(self):
        if 'therapists' in st.session_state:
            return st.session_state.therapists
        therapists = self.accounts_repository.get_therapists()
        st.session_state.therapists = therapists
        return therapists

    def get_patients(self):
        if 'patients' in st.session_state:
            return st.session_state.patients
        patients = self.accounts_repository.get_patients()
        st.session_state.patients = patients
        return patients

    def get_account_stats(self):
        if 'account_stats' in st.session_state:
            return st.session_state.accounts_stats
        accounts_stats = self.accounts_repository.get_account_stats()
        st.session_state.accounts_stats = accounts_stats
        return accounts_stats
