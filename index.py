import streamlit as st

# Função para criar o card de produto
def produto_card(imagem, nome, avaliacao, preco):
    """Cria um dicionário de produto com suas informações."""
    return {"imagem": imagem, "nome": nome, "avaliacao": avaliacao, "preco": preco}

# Função para exibir o card do produto
def exibir_produto(produto):
    """Exibe um card de produto na interface."""
    st.markdown(f"### {produto['nome']}")
    st.image(produto['imagem'], width=200)
    estrelas = '⭐' * produto['avaliacao']
    st.markdown(f"**Avaliação:** {estrelas}")
    st.markdown(f"**Preço:** R$ {produto['preco']:.2f} por kilo")

# Inicializa a sessão do carrinho
if "itens_carrinho" not in st.session_state:
    st.session_state.itens_carrinho = []

# Divisão das colunas
col1, col2 = st.columns([4, 2])

# Coluna da loja
with col1:
    st.markdown("# Loja")
    st.markdown("## ________________________")
    produto = produto_card(
        imagem="sonic dançando.gif",
        nome="sonic dançando muito foda",
        avaliacao=6,
        preco=3000.99
    )
    exibir_produto(produto)
    st.markdown("""
        <style>
            div.stButton > button:first-child {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 0.5em 1em;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }
            div.stButton > button:first-child:hover {
                background-color: #218838;
            }
        </style>
        """, unsafe_allow_html=True)
    if st.button("Comprar"):
        st.session_state.itens_carrinho.append(produto)

# Coluna do carrinho
with col2:
    st.markdown("# Carrinho")
    if st.session_state.itens_carrinho:
        for i, item in enumerate(st.session_state.itens_carrinho):
            st.image(item['imagem'], width=100)
            st.markdown(f"**{item['nome']}**")
            estrelas = '⭐' * item['avaliacao']
            st.markdown(f"**Avaliação:** {estrelas}")
            st.markdown(f"**Preço:** R$ {item['preco']:.2f}")
            # Botão para remover item
            st.markdown("""
                    <style>
                        div.stButton > button:first-child {
                            background-color: #28a745;
                            color: white;
                            border: none;
                            padding: 0.5em 1em;
                            border-radius: 5px;
                            font-size: 16px;
                            cursor: pointer;
                        }
                        div.stButton > button:first-child:hover {
                            background-color: #ff0000;
                        }
                    </style>
                    """, unsafe_allow_html=True)
            if st.button(f"Remover {item['nome']}", key=f"remove_{i}"):
                st.session_state.itens_carrinho.pop(i)
                break
    else:
        st.markdown("Seu carrinho está vazio.")
st.image(produto['imagem'], width=200)