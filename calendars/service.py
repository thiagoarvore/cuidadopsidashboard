import streamlit as st
from calendars.repository import CalendarsRepository


class CalendersService:

    def __init__(self):
        self.calendars_repository = CalendarsRepository()

    def get_calendars(self):
        if 'calendars' in st.session_state:
            return st.session_state.calendars
        calendars = self.calendars_repository.get_calendars()
        st.session_state.calendars = calendars
        return calendars

    def get_calendar_stats(self):
        if 'calendar_stats' in st.session_state:
            return st.session_state.calendar_stats
        calendar_stats = self.calendars_repository.get_calendar_stats()
        st.session_state.calendar_stats = calendar_stats
        return calendar_stats
