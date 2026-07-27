menu = st.sidebar.radio(
    "Select Operation",
    [
        "Dashboard",
        "Add Task",
        "View Tasks",
        "Update Task",
        "Delete Task"
    ]
)


if menu == "Dashboard":

    st.markdown(
        '<div class="main-title">Task Manager</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Organize your work. Track your progress. Stay productive.</div>',
        unsafe_allow_html=True
    )

    total_tasks = len(tasks)

    completed_tasks = 0

    for task in tasks:
        if task["status"].lower() == "completed":
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{total_tasks}</div>
                <div class="stat-label">Total Tasks</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{completed_tasks}</div>
                <div class="stat-label">Completed</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-number">{pending_tasks}</div>
                <div class="stat-label">Pending</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("Recent Tasks")

    if len(tasks) == 0:
        st.info("No tasks available. Add your first task.")

    else:

        for task in tasks[-5:]:

            st.markdown(
                f"""
                <div class="task-card">
                    <div class="task-title">{task["title"]}</div>
                    <div class="task-info">
                        Status: {task["status"]} |
                        Deadline: {task["deadline"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


elif menu == "Add Task":

    st.title("Add New Task")

    task_name = st.text_input("Task Title")

    task_status = st.selectbox(
        "Task Status",
        [
            "Pending",
            "In Progress",
            "Completed"
        ]
    )

    deadline = st.date_input("Deadline")

    if st.button("Add Task"):

        task_exists = False

        for task in tasks:

            if task["title"].lower() == task_name.lower():

                task_exists = True

        if task_exists:

            st.error("This task already exists.")

        elif task_name == "":

            st.warning("Please enter a task title.")

        else:

            task = {
                "title": task_name,
                "status": task_status,
                "deadline": str(deadline)
            }

            tasks.append(task)

            st.success("Task added successfully.")


elif menu == "View Tasks":

    st.title("All Tasks")

    if len(tasks) == 0:

        st.info("No tasks available.")

    else:

        for index, task in enumerate(tasks):

            st.markdown(
                f"""
                <div class="task-card">
                    <div class="task-title">
                        {index + 1}. {task["title"]}
                    </div>

                    <div class="task-info">
                        Status: {task["status"]}
                    </div>

                    <div class="task-info">
                        Deadline: {task["deadline"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


elif menu == "Update Task":

    st.title("Update Task")

    if len(tasks) == 0:

        st.info("No tasks available.")

    else:

        task_titles = []

        for task in tasks:
            task_titles.append(task["title"])

        selected_task = st.selectbox(
            "Select Task",
            task_titles
        )

        selected_index = task_titles.index(selected_task)

        task = tasks[selected_index]

        new_title = st.text_input(
            "Update Title",
            value=task["title"]
        )

        new_status = st.selectbox(
            "Update Status",
            [
                "Pending",
                "In Progress",
                "Completed"
            ]
        )

        new_deadline = st.date_input(
            "Update Deadline"
        )

        if st.button("Update Task"):

            task["title"] = new_title
            task["status"] = new_status
            task["deadline"] = str(new_deadline)

            st.success("Task updated successfully.")


elif menu == "Delete Task":

    st.title("Delete Task")

    if len(tasks) == 0:

        st.info("No tasks available.")

    else:

        task_titles = []

        for task in tasks:
            task_titles.append(task["title"])

        selected_task = st.selectbox(
            "Select Task to Delete",
            task_titles
        )

        if st.button("Delete Task"):

            for task in tasks:

                if task["title"] == selected_task:

                    tasks.remove(task)

                    st.success(
                        f"Task '{selected_task}' deleted successfully."
                    )

                    break
