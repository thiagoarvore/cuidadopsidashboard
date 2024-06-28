import streamlit as st
from treatments.repository import TreatmentsRepository


class TreatmentsService:

    def __init__(self):
        self.treatments_repository = TreatmentsRepository()

    def get_treatments(self):
        if 'treatments' in st.session_state:
            return st.session_state.treatments
        treatments = self.treatments_repository.get_treatments()
        st.session_state.treatments = treatments
        return treatments

    def get_treatment_stats(self):
        if 'treatments_stats' in st.session_state:
            return st.session_state.treatments_stats
        treatments_stats = self.treatments_repository.get_treatment_stats()
        st.session_state.treatments_stats = treatments_stats
        return treatments_stats
