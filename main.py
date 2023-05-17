import view.zooView as zooView
import streamlit as st

if __name__ == '__main__':
    st.set_page_config(
        page_title="zoo MAVA",
        page_icon="🐼",
        layout="wide"
    )
    view = zooView.zooView()
    view.prueba()
    #view.menu_principalV()

