import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
import numpy as np
import pandas as pd

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    content = bucket.blob(file_path).download_as_string().decode("utf-8")
    return content

bucket_name = "app_recomenda"
file_path = "servicos_com_id.csv"

content = read_file(bucket_name, file_path)
st.write(content.dtype)
#st.dataframe(content[0,:])

# import streamlit as st
import numpy as np
import pandas as pd
# import json

# with open('../servicos.txt') as json_file:
#     data = json.load(json_file)

# dados = pd.DataFrame.from_dict(data['resposta'])
# digitais = dados.loc[(dados.servicoDigital),'nome'].sort_values()


# st.write("Painel para visualização das recomendações de um serviço")

# cooc_final = np.load('../coocorrencia101000.npy')
# tabela_servicos = pd.read_csv('../servicos_com_id.csv',sep=";")

# #number = st.number_input('Escolha a id do serviço',value=60)

# servico = st.selectbox('Escolha o serviço',digitais)

# servico_indice = tabela_servicos[tabela_servicos['nome']==servico].index[0]
# #servico_nome = tabela_servicos.iloc[servico_indice,1]
# st.write("O serviço escolhido foi: " + servico)

# st.write("Os serviços recomendados são:")

# aa = cooc_final[servico_indice,].argsort()[::-1][1:10]
# st.write(tabela_servicos.iloc[aa,1])
