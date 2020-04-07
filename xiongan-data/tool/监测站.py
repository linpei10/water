#
# 不太好起名字，就用了中文，不知道有没有犯大忌QAQ   you
#
import xlrd
import os
import sys
import codecs
import json
import re

List = ["STNM", "LGTD", "LTTD"]


def excel2json(inputFilePath, outputFilePath):
    # 打开excel文件
    excel = xlrd.open_workbook(inputFilePath)
    # 获取sheet名列表
    # sheet_names = excel.sheet_names()
    # 获取sheet
    # sheet = excel.sheet_by_name(sheet_names[0])
    sheet = excel.sheet_by_index(0)

    # 第一行是表单标题

    row_0 = sheet.row(0)  # 第一行
    nrows = sheet.nrows  # 行号
    ncols = sheet.ncols  # 列号

    result = {}  # 定义json对象
    # result["title"] = inputFilePath  #表单标题
    # result["rows"] = nrows  #行号
    result["data"] = []  # 每一行作为数组的一项

    # 遍历所有行，将excel转化为json对象
    for i in range(1, nrows):
        tmp = {}
        # 遍历所有列
        for j in range(ncols):
            # 获取当前列中文标题
            title_de = str(row_0[j])
            title_cn = title_de.split("'")[1]

            # 获取单元格的值
            if (title_cn in List):
                if sheet.row_values(i)[j] == "":
                    tmp[title_cn] = "N/A"
                    print(i, j, title_cn, type(sheet.row_values(i)[j]))
                tmp[title_cn] = sheet.row_values(i)[j]
        if tmp not in result["data"]:
            result["data"].append(tmp)

    json_data = json.dumps(result, ensure_ascii=False, indent=2)

    output = codecs.open(outputFilePath, 'w', "utf-8")
    output.write(json_data)
    output.close()


if __name__ == "__main__":
    excel2json("监测站.xlsx", "监测站.json")
