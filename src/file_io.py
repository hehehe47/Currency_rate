def write_in(l, file_name, col_set):
    '''
    写入xlsx
    :arg: (list)l:[{'name':bank,'rate':rate}]
    :return: None
    '''
    import openpyxl
    import time
    workbook = openpyxl.load_workbook(file_name)  # 加载xlsx
    sheet = workbook.get_sheet_by_name('cr')  # 获取sheet
    n_col = sheet.max_column  # 获取当前最大列
    col = col_set[n_col]  # 获取列字符串 A列为0 所以最大列即插入列
    sheet[col + str(1)] = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))  # 第一行插入时间
    for ind, br in enumerate(l):
        sheet[col + str(ind + 2)] = br['rate']
    workbook.save('..\\log\\currency_rate.xlsx')
