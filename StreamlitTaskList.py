import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Task List App")
def add_task():
    task = st.text_input("Enter a new task:", key="new_task_input")
    if st.button("Add Task"):
        if task.strip():
            st.session_state.tasks.append({"Text: ":task, "done" : False})
            st.rerun()
        else:
            st.warning("Please enter a task!", icon="⚠️")


st.subheader("Task List: ")
def show_tasks():
    if not st.session_state.tasks:
        st.info("No tasks added yet!")
        return

    for i, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.05, 0.80, 0.05])
        with cols[0]:
            task["done"] = st.checkbox("", value=task["done"], key=f"done_{i}")
        with cols[1]:
            text = task["Text: "]
            st.markdown(text)
        with cols[2]:
            if st.button("Delete", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

if __name__ == "__main__":
    add_task()
    show_tasks()