## 📌 Visão Geral do Projeto

O projeto é dividido em dois módulos principais que consomem dados de datasets em CSV de livros e avaliações de clientes:

### 1. Dashboard Principal (`app.py`)
- **Filtro de Preço Dinâmico:** Controle via barra deslizante (*slider*) para filtrar a base de dados em tempo real pelo valor máximo configurado.
- **Gráfico de Lançamentos:** Gráfico de barras indicando a quantidade de livros publicados por ano.
- **Distribuição de Preços:** Histograma detalhado com a variação de valores dos livros filtrados.
- **Tabela Geral:** Exibição da base de dados completa de avaliações dos usuários.

### 2. Visão Detalhada do Livro (`pages/book review.py`)
- **Navegação por Livro:** Seleção individual de qualquer título da base através do menu lateral.
- **Métricas do Livro:** Painel com informações essenciais como preço, avaliação média, ano de publicação e gênero.
- **Feed de Avaliações:** Interface em estilo *chat* exibindo o nome do avaliador, nota dada e comentário deixado.

---

## 📁 Estrutura do Repositório

```text
├── datasets/
│   ├── customer reviews.csv
│   └── Top-100 Trending Books.csv
├── pages/
│   └── book review.py
├── app.py
├── runner.py
└── requirements.txt
🚀 Como Executar Localmente
Clone o repositório:

Bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
Instale as dependências requeridas:

Bash
pip install -r requirements.txt
Inicie a aplicação:

Bash
streamlit run app.py
