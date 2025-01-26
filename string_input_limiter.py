# -*- coding: UTF-8 -*-
"""
@Project: pythonProject
@File   : string_input_limiter.py
@IDE    : PyCharm
@Author : staryu
@Date   : 2025/1/26 19:06
@Doc    : 处理String 网站下载的PPI文件数据
"""
import pandas as pd

ppi_file = r"D:\PycharmProjects\pythonProject\data\9606.protein.links.full.v12.0.txt"
ESNP2name_file = r"D:\PycharmProjects\pythonProject\data\9606.protein.info.v12.0.txt"

# 读取蛋白质互作数据
ppi_data = pd.read_csv(ppi_file, sep=" ")
ESNP2name = pd.read_csv(ESNP2name_file, sep="\t")
ESNP2name_dict = dict(zip(ESNP2name["#string_protein_id"], ESNP2name["preferred_name"]))

ppi_data["protein1"] = ppi_data["protein1"].map(ESNP2name_dict)
ppi_data["protein2"] = ppi_data["protein2"].map(ESNP2name_dict)

# 保存处理后的数据
ppi_data.to_csv("PPI_data.txt", sep="\t", index=False)