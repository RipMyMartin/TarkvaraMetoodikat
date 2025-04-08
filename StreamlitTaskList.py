import streamlit as st

def initSession():
    if "tasks" not in st.sessionState:
        st.sessionState.tasks = []

def addTasks():
    with st.form("add_task"):
        newTaks = st.text_input("💡 Kirjutage uue Ylesanne")
        submitted = st.form_submit_button("Lisada")
        if submitted and newTaks:
            st.sessionState.tasks.append(newTaks)
            st.success("Ylesanne lisatud!")

def showTasks():
    if not st.sessionState.tasks:
        st.info("Pole Ylesandeid, lisa ylesanne!")
        return

    st.subheader("📋 Ylesannete list")
    for i, task in enumerate(st.sessionState.tasks):
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.write(f"{i + 1}. {task}")
        with col2:
            if st.button("❌", key=f"delete_{i}"):
                st.sessionState.tasks.pop(i)
                return deleteTask()
            
def deleteTask():
    pass

def main():
    st.title("📝 Tasks list")
    initSession()
    addTasks()
    showTasks()

if __name__ == "__main__":
    main()
