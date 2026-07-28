import streamlit as st

from expenses import (
    expenses,
    add_expense,
    show_total,
    update_expense,
    delete_expense
)



st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)


\

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fb;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .dashboard-card {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    .expense-card {
        padding: 15px;
        border-radius: 10px;
        background-color: white;
        border: 1px solid #e5e7eb;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)




st.sidebar.title(" Expense Tracker")

st.sidebar.write("Manage your personal expenses")

st.sidebar.divider()


menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Expense",
        "All Expenses",
        "Update Expense",
        "Delete Expense"
    ]
)


st.sidebar.divider()

st.sidebar.caption("Expense Tracker v1.0")




if menu == "Dashboard":

    st.title("Dashboard")

    st.write("Welcome back! Here's your expense overview.")

    st.divider()


  
    total = show_total()


    
    total_expenses = len(expenses)


   
    categories = set()

    for expense in expenses:

        categories.add(expense["category"])


    total_categories = len(categories)


  

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Total Spent",
            f"${total:,.2f}"
        )


    with col2:

        st.metric(
            "Total Expenses",
            total_expenses
        )


    with col3:

        st.metric(
            "Categories",
            total_categories
        )


    st.divider()


    

    st.subheader("Recent Expenses")


    if len(expenses) == 0:

        st.info(
            "No expenses added yet. "
            "Go to 'Add Expense' to get started."
        )

    else:

        for index, expense in enumerate(
            expenses[-5:],
            start=1
        ):

            st.markdown(
                f"""
                <div class="expense-card">

                <b>{expense['name']}</b>

                <br>

                Category: {expense['category']}

                <br>

                Amount: ${expense['amount']:,.2f}

                </div>
                """,
                unsafe_allow_html=True
            )




elif menu == "Add Expense":

    st.title("Add New Expense")

    st.write("Record a new expense in your tracker.")

    st.divider()


    col1, col2 = st.columns(2)


    with col1:

        name = st.text_input(
            "Expense Name",
            placeholder="e.g. Groceries"
        )


        category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Entertainment",
                "Education",
                "Health",
                "Other"
            ]
        )


    with col2:

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )


    st.divider()


    if st.button(
        "Add Expense",
        type="primary",
        use_container_width=True
    ):


        if name.strip() == "":

            st.warning(
                "Please enter an expense name."
            )


        elif amount <= 0:

            st.warning(
                "Amount must be greater than zero."
            )


        else:

            add_expense(
                name,
                amount,
                category
            )


            st.success(
                "Expense added successfully!"
            )




elif menu == "All Expenses":

    st.title("All Expenses")

    st.write(
        "View all your recorded expenses."
    )

    st.divider()


    if len(expenses) == 0:

        st.info(
            "No expenses added yet."
        )


    else:

        st.dataframe(
            expenses,
            use_container_width=True,
            hide_index=True
        )


        st.divider()


        st.subheader(
            f"Total Spent: ${show_total():,.2f}"
        )



elif menu == "Update Expense":

    st.title("Update Expense")

    st.write(
        "Edit the details of an existing expense."
    )

    st.divider()


    if len(expenses) == 0:

        st.info(
            "No expenses available to update."
        )


    else:

        expense_number = st.selectbox(
            "Select Expense",
            range(len(expenses)),
            format_func=lambda index:
            f"{expenses[index]['name']} "
            f"(${expenses[index]['amount']:,.2f})"
        )


        selected_expense = expenses[
            expense_number
        ]


        st.divider()


        new_name = st.text_input(
            "Expense Name",
            value=selected_expense["name"]
        )


        new_amount = st.number_input(
            "Amount",
            value=float(
                selected_expense["amount"]
            ),
            min_value=0.0,
            step=1.0
        )


        new_category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Entertainment",
                "Education",
                "Health",
                "Other"
            ],
            index=[
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Entertainment",
                "Education",
                "Health",
                "Other"
            ].index(
                selected_expense["category"]
            )
            if selected_expense["category"]
            in [
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Entertainment",
                "Education",
                "Health",
                "Other"
            ]
            else 0
        )


        st.divider()


        if st.button(
            "Save Changes",
            type="primary",
            use_container_width=True
        ):


            if new_name.strip() == "":

                st.warning(
                    "Expense name cannot be empty."
                )


            elif new_amount <= 0:

                st.warning(
                    "Amount must be greater than zero."
                )


            else:

                update_expense(
                    expense_number,
                    new_name,
                    new_amount,
                    new_category
                )


                st.success(
                    "Expense updated successfully!"
                )




elif menu == "Delete Expense":

    st.title("Delete Expense")

    st.write(
        "Remove an expense from your tracker."
    )

    st.divider()


    if len(expenses) == 0:

        st.info(
            "No expenses available to delete."
        )


    else:

        delete_number = st.selectbox(
            "Select Expense to Delete",
            range(len(expenses)),
            format_func=lambda index:

            f"{expenses[index]['name']} "
            f"(${expenses[index]['amount']:,.2f})"
        )


        selected_expense = expenses[
            delete_number
        ]


        st.warning(
            f"You are about to delete: "
            f"**{selected_expense['name']}**"
        )


        if st.button(
            "Delete Expense",
            type="primary",
            use_container_width=True
        ):


            deleted_expense = delete_expense(
                delete_number
            )


            st.success(
                f"{deleted_expense['name']} "
                "deleted successfully!"
            )
