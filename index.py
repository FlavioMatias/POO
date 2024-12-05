import streamlit as st

# Função para criar o card de produto
def produto_card(imagem, nome, avaliacao, preco):
    st.markdown(f"### {nome}")
    
    # Exibe a imagem do produto
    st.image(imagem, width=200)
    
    # Exibe a avaliação com estrelas
    estrelas = '⭐' * avaliacao
    st.markdown(f"**Avaliação:** {estrelas}")
    
    # Exibe o preço
    st.markdown(f"**Preço:** R$ {preco:.2f}")

# Usando a função para criar o card com os dados do produto
produto_card(
    imagem="shurimp.png",  # Substitua com a URL da imagem do seu produto
    nome="shrimp",
    avaliacao=4,  # Avaliação de 1 a 5
    preco=129.90
)
