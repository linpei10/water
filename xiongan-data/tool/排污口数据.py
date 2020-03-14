# 
# 排污口数据.xlsx 的转换
# 因为经纬度坐标的格式不是很统一，就把格式比较奇怪的都忽略了
# 不太好起名字，就用了中文，不知道有没有犯大忌QAQ
# 有几项没有放进去，如果需要的话可以在for循环中更改
# 

import xlrd
import os
import sys
import codecs
import json
import re

def excel2json(inputFilePath, outputFilePath):
    # 打开excel文件
    excel = xlrd.open_workbook(inputFilePath)
    # 获取sheet名列表
    # sheet_names = excel.sheet_names()
    # 获取sheet
    # sheet = excel.sheet_by_name(sheet_names[0])
    sheet = excel.sheet_by_index(0)
    # 第一行是表单标题
    row_0 = sheet.row(0)  #第一行
    nrows = sheet.nrows  # 行号
    ncols = sheet.ncols  # 列号

    result = {}  #定义json对象
    # result["title"] = inputFilePath  #表单标题
    # result["rows"] = nrows  #行号
    result["data"] = []  #每一行作为数组的一项

    # 遍历所有行，将excel转化为json对象
    for i in range(nrows):
        if i == 0:
            continue
        tmp = {}
        # 遍历所有列
        for j in range(ncols):
            # 获取当前列中文标题
            title_de = str(row_0[j])
            title_cn = title_de.split("'")[1]

            # 获取单元格的值
            if (title_cn == "id"):
                tmp[title_cn] = int(sheet.row_values(i)[j])

            if (title_cn == "pdo_cd"):
                '''
                if (sheet.row_values(i)[j] == ''):
                    # tmp[title_cn] = "无数据"
                    break
                elif (sheet.row_values(i)[j] == '/'):
                    # tmp[title_cn] = '/'
                    break
                else:
                    tmp[title_cn] = int(sheet.row_values(i)[j])
                '''
                continue

            if (title_cn == "city"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "country"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "town"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "location"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "lgtd_lttd"):
                # "116°01′30.36″,38°49′39.69″"
                # tmp[title_cn] = sheet.row_values(i)[j]
                # if (re.match('^[0-9]+[°][0-9]+[′]', sheet.row_values(i)[j])):
                #     position = sheet.row_values(i)[j].split(',')
                #     x = float(position[0].split('°')[0])
                #     y = float(position[0].split('°')[1].split('′')[0])
                #     z = float(position[0].split('′')[1].split('″')[0])
                #     lng = round(x + y / 60 + z / 3600, 6)
                #     x = float(position[1].split('°')[0])
                #     y = float(position[1].split('°')[1].split('′')[0])
                #     z = float(position[1].split('′')[1].split('″')[0])
                #     lat = round(x + y / 60 + z / 3600, 6)
                #     tmp[title_cn] = {
                #         "lng": lng,
                #         "lat": lat,
                #     }
                # else:
                #     break
                continue

            if (title_cn == "lgtd"):
                tmp[title_cn] = round(sheet.row_values(i)[j], 5)
            
            if (title_cn == "lttd"):
                tmp[title_cn] = round(sheet.row_values(i)[j], 5)

            if (title_cn == "dwb"):
                '''
                if (sheet.row_values(i)[j] == ''):
                    # tmp[title_cn] = 0
                    break
                else:
                    tmp[title_cn] = int(sheet.row_values(i)[j])
                '''
                continue

            if (title_cn == "dwb_nm"):
                # tmp[title_cn] = sheet.row_values(i)[j]
                continue

            if (title_cn == "branch"):
                # tmp[title_cn] = sheet.row_values(i)[j]
                continue

            if (title_cn == "monitor_online"):
                if (sheet.row_values(i)[j] == "是"):
                    tmp[title_cn] = True
                elif (sheet.row_values(i)[j] == "否"):
                    tmp[title_cn] = False

            if (title_cn == "pdo_sr"):
                # tmp[title_cn] = sheet.row_values(i)[j]
                continue

            if (title_cn == "eng_man_nm"):
                # tmp[title_cn] = sheet.row_values(i)[j]
                continue

            if (title_cn == "stat_time"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "ph"):
                if (re.match('^[-+]?[0-9]+\\.?[0-9][0-9]*$', sheet.row_values(i)[j])):
                    tmp[title_cn] = float(sheet.row_values(i)[j])
                    if (tmp[title_cn] == 0):
                        break
                elif (sheet.row_values(i)[j] == ''):
                    tmp[title_cn] = "无数据"
                else:
                    tmp[title_cn] = sheet.row_values(i)[j]
                    
            if (title_cn == "cod"):
                if (re.match('^[-+]?[0-9]+\\.?[0-9][0-9]*$', sheet.row_values(i)[j])):
                    tmp[title_cn] = float(sheet.row_values(i)[j])
                    if (tmp[title_cn] == 0):
                        break
                elif (sheet.row_values(i)[j] == ''):
                    tmp[title_cn] = "无数据"
                else:
                    tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "nh3n"):
                if (re.match('^[-+]?[0-9]+\\.?[0-9][0-9]*$', sheet.row_values(i)[j])):
                    tmp[title_cn] = float(sheet.row_values(i)[j])
                    if (tmp[title_cn] == 0):
                        break
                elif (sheet.row_values(i)[j] == ''):
                    tmp[title_cn] = "无数据"
                else:
                    tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "tp"):
                if (re.match('^[-+]?[0-9]+\\.?[0-9][0-9]*$', sheet.row_values(i)[j])):
                    tmp[title_cn] = float(sheet.row_values(i)[j])
                    if (tmp[title_cn] == 0):
                        break
                elif (sheet.row_values(i)[j] == ''):
                    tmp[title_cn] = "无数据"
                else:
                    tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "tn"):
                if (re.match('^[-+]?[0-9]+\\.?[0-9][0-9]*$', sheet.row_values(i)[j])):
                    tmp[title_cn] = float(sheet.row_values(i)[j])
                    if (tmp[title_cn] == 0):
                        break
                elif (sheet.row_values(i)[j] == ''):
                    tmp[title_cn] = "无数据"
                else:
                    tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "wt"):
                continue

            if (title_cn == "par_plu2"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "par_plu1"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "standards"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "standard_yn"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "remark"):
                tmp[title_cn] = sheet.row_values(i)[j]

            if (title_cn == "status"):
                if (sheet.row_values(i)[j] == ''):
                    tmp[title_cn] = "无数据"
                else:
                    tmp[title_cn] = int(sheet.row_values(i)[j])

            if (title_cn == "year_month"):
                tmp[title_cn] = sheet.row_values(i)[j]
                result["data"].append(tmp)

    json_data = json.dumps(result, ensure_ascii=False, indent=2)
    
    output = codecs.open(outputFilePath, 'w', "utf-8")
    output.write(json_data)
    output.close()

if __name__ == "__main__":
    excel2json("排污口数据.xlsx","排污口数据.json")