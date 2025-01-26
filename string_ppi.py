# -*- coding: UTF-8 -*-
"""
@Project: Deconformer
@File   : get_ppi_score.py
@IDE    : PyCharm
@Author : staryu
@Date   : 2024/9/27 下午6:04
@Doc    : 
"""
import requests  ## python -m pip install requests
import pandas as pd


##
## Construct the request
##


def get_ppi_score(genes_list, all_ppi=True):
    string_api_url = "https://version-12-0.string-db.org/api"
    output_format = "tsv-no-header"
    method = "interaction_partners"

    request_url = "/".join([string_api_url, output_format, method])

    res = pd.DataFrame()

    step = len(genes_list) // 2000
    for i in range(0, len(genes_list), 2000):
        print('Step ' + str(i // 2000) + '/' + str(step) + '...')
        if i + 2000 < len(genes_list):
            my_genes = genes_list[i:i + 2000]
        else:
            my_genes = genes_list[i:]

        temp_res = pd.DataFrame()

        if all_ppi:
            params = {

                "identifiers": "%0d".join(my_genes),  # your protein
                "species": 9606,  # species NCBI identifier
                "caller_identity": "www.awesome_app.org"  # your app name

            }

            ##
            ## Call STRING
            ##

            response = requests.post(request_url, data=params)

            temp_res['stringId_A'] = [j.strip().split("\t")[0] for j in response.text.strip().split("\n")]
            temp_res['stringId_B'] = [j.strip().split("\t")[1] for j in response.text.strip().split("\n")]
            temp_res['preferredName_A'] = [j.strip().split("\t")[2] for j in response.text.strip().split("\n")]
            temp_res['preferredName_B'] = [j.strip().split("\t")[3] for j in response.text.strip().split("\n")]
            temp_res['ncbiTaxonId'] = [j.strip().split("\t")[4] for j in response.text.strip().split("\n")]
            temp_res['combined_score'] = [j.strip().split("\t")[5] for j in response.text.strip().split("\n")]
            temp_res['nscore'] = [j.strip().split("\t")[6] for j in response.text.strip().split("\n")]
            temp_res['fscore'] = [j.strip().split("\t")[7] for j in response.text.strip().split("\n")]
            temp_res['pscore'] = [j.strip().split("\t")[8] for j in response.text.strip().split("\n")]
            temp_res['ascore'] = [j.strip().split("\t")[9] for j in response.text.strip().split("\n")]
            temp_res['escore'] = [j.strip().split("\t")[10] for j in response.text.strip().split("\n")]
            temp_res['dscore'] = [j.strip().split("\t")[11] for j in response.text.strip().split("\n")]
            temp_res['tscore'] = [j.strip().split("\t")[12] for j in response.text.strip().split("\n")]

        else:
            params = {

                "identifiers": "%0d".join(my_genes),  # your protein
                "species": 9606,  # species NCBI identifier
                "limit": 20,
                "caller_identity": "www.awesome_app.org"  # your app name

            }

            response = requests.post(request_url, data=params)

            temp_res['stringId_A'] = [j.strip().split("\t")[0] for j in response.text.strip().split("\n")]
            temp_res['stringId_B'] = [j.strip().split("\t")[1] for j in response.text.strip().split("\n")]
            temp_res['preferredName_A'] = [j.strip().split("\t")[2] for j in response.text.strip().split("\n")]
            temp_res['preferredName_B'] = [j.strip().split("\t")[3] for j in response.text.strip().split("\n")]
            temp_res['ncbiTaxonId'] = [j.strip().split("\t")[4] for j in response.text.strip().split("\n")]
            temp_res['combined_score'] = [j.strip().split("\t")[5] for j in response.text.strip().split("\n")]
            temp_res['nscore'] = [j.strip().split("\t")[6] for j in response.text.strip().split("\n")]
            temp_res['fscore'] = [j.strip().split("\t")[7] for j in response.text.strip().split("\n")]
            temp_res['pscore'] = [j.strip().split("\t")[8] for j in response.text.strip().split("\n")]
            temp_res['ascore'] = [j.strip().split("\t")[9] for j in response.text.strip().split("\n")]
            temp_res['escore'] = [j.strip().split("\t")[10] for j in response.text.strip().split("\n")]
            temp_res['dscore'] = [j.strip().split("\t")[11] for j in response.text.strip().split("\n")]
            temp_res['tscore'] = [j.strip().split("\t")[12] for j in response.text.strip().split("\n")]

        res = pd.concat([res, temp_res], axis=0)

    return res


# data_names = ['monaco_pbmc', 'sdy67', 'sdy67_tpm', 'microarray']
# for name in data_names:
#     print('Dealing with ' + name + ' data...')
#     data = pd.read_csv('/home/dell/disks/ghj/scBERT/data/test/' + name + '_test.txt', sep='\t', index_col=0)
#
#     # 只保留基因名，不保留表头
#     genes_list = pd.DataFrame(data.columns)
#
#     genes_list = genes_list.iloc[:, 0].tolist()
#
#     all_ppi = True
#     res = get_ppi_score(genes_list, all_ppi=True)
#
#     if all_ppi:
#         res.to_csv('./resource/ppi/' + name + '_ppi_score.txt', sep='\t', index=False)
#     else:
#         res.to_csv('./resource/ppi/' + name + '_ppi_score.txt', sep='\t', index=False)

data = pd.read_csv('/home/dell/disks/ghj/Deconformer/data/test_gene.txt', sep='\t', index_col=0)
genes_list = pd.DataFrame(data.index)

genes_list = genes_list.iloc[:, 0].tolist()

res = get_ppi_score(genes_list, all_ppi=True)

res.to_csv('./resource/ppi/' + 'test' + '_ppi_score.txt', sep='\t', index=False)

