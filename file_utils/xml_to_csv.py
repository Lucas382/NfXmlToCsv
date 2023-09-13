import os
import time

import xmltodict
import pandas as pd


def get_xlsx_infos(caminho_da_pasta, nome_arquivo, valores):
    with open(f"{caminho_da_pasta}\\{nome_arquivo}", "r") as file_xml:
        dic_file = xmltodict.parse(file_xml.read())

        if "NFe" in dic_file:
            infos_nf = dic_file["NFe"]["infNFe"]
        else:
            infos_nf = dic_file["nfeProc"]["NFe"]["infNFe"]
        num_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf["emit"]["xNome"]
        nome_cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"]["enderDest"]

        if "vol" in infos_nf["transp"]:
            peso_bruto = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso_bruto = "Peso não informado"

        valores.append([num_nota, empresa_emissora, nome_cliente, endereco, peso_bruto])


class XlsxToCsvConverter:
    def make_xlsx(self, caminho_da_pasta, nome_do_arquivo, lista_xlsx):
        colunas = ["num_nota", "empresa_emissora", "nome_cliente", "endereco", "peso_bruto"]
        valores = []

        if lista_xlsx:
            for arquivo in lista_xlsx:
                get_xlsx_infos(caminho_da_pasta, arquivo, valores)

            tabela = pd.DataFrame(columns=colunas, data=valores)

            if "/" in nome_do_arquivo:
                os.makedirs(nome_do_arquivo.rsplit("/", 1)[0])
            tabela.to_excel(f"{nome_do_arquivo}.xlsx", index=False)

        else:
            print("Nenhum arquivo Xlsx encontrado")
