import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

st.image("logo.png", width=200)

st.title("Product Management")


# Auxiliary function to get more details about errors
def show_response_message(response):
    if response.status_code == 200:
        st.success("Succes! Operation completed.")
    else:
        try:
            data = response.json()
            if "detail" in data:
                # If the error is a list, extract each error details
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Error: {errors}")
                else:
                    # Caso contrário, mostre a mensagem de erro diretamente
                    st.error(f"Error: {data['detail']}")
        except ValueError:
            st.error("Unknown error. It was not possible to transcribe the message.")


# Adicionar Produto
with st.expander("Add New Product"):
    with st.form("new_product"):
        name = st.text_input("Product Name")
        description = st.text_area("Product Description")
        price = st.number_input("Price", min_value=0.01, format="%f")
        category = st.selectbox(
            "Category",
            ["Eletronic", "Eletrodomestic", "Forniture", "Clothes", "Shoes"],
        )
        vendor_email = st.text_input("Vendor e-mail")
        submit_button = st.form_submit_button("Add Product")

        if submit_button:
            response = requests.post(
                "http://backend:8000/products/",
                json={
                    "name": name,
                    "description": description,
                    "price": price,
                    "category": category,
                    "vendor_email": vendor_email
                },
            )
            show_response_message(response)
# Visualizar Produtos
with st.expander("Show Product"):
    if st.button("Show all products"):
        response = requests.get("http://backend:8000/products/")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame(product)

            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "vendor_email",
                    "created_at",
                ]
            ]

            # Exibe o DataFrame sem o índice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Obter Detalhes de um Produto
with st.expander("Get Product Details"):
    get_id = st.number_input("Product ID", min_value=1, format="%d")
    if st.button("Search Product"):
        response = requests.get(f"http://backend:8000/products/{get_id}")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame([product])

            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "vendor_email",
                    "created_at",
                ]
            ]

            # Exibe o DataFrame sem o índice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Deletar Produto
with st.expander("Delete Product"):
    delete_id = st.number_input("The ID of Product to be deleted", min_value=1, format="%d")
    if st.button("Delete Product"):
        response = requests.delete(f"http://backend:8000/products/{delete_id}")
        show_response_message(response)

# Atualizar Produto
with st.expander("Update Product"):
    with st.form("update_product"):
        update_id = st.number_input("Product ID", min_value=1, format="%d")
        new_name = st.text_input("New Product Name")
        new_description = st.text_area("New Product Description")
        new_price = st.number_input(
            "New Price",
            min_value=0.01,
            format="%f",
        )
        new_categoria = st.selectbox(
            "New Category",
            ["Eletronic", "Eletrodomestic", "Forniture", "Clothes", "Shoes"],
        )
        new_email = st.text_input("New Vendor Email")

        update_button = st.form_submit_button("Update Product")

        if update_button:
            update_data = {}
            if new_name:
                update_data["name"] = new_name
            if new_description:
                update_data["description"] = new_description
            if new_price > 0:
                update_data["price"] = new_price
            if new_email:
                update_data["vendor_email"] = new_email
            if new_categoria:
                update_data["category"] = new_categoria

            if update_data:
                response = requests.put(
                    f"http://backend:8000/products/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("No product information was informed to be updated")