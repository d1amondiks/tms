import xlsxwriter

workbook = xlsxwriter.Workbook('homeworks.xlsx')

expenses = ('Name','PRlink','Note')
expenses2 = ([1,u'Дмитрий Горский'],
[2, u'Екатерина Гучек'],
[3, u'Роман Завадский'],
[4, u'Денис Копейкин'],
[5, u'Дмитрий Лис'],
[6, u'Дмитрий Прусевич'],
[7, u'Дарья Силантьева'],
[8, u'Вячеслав Станкевич'],)
row, col = 0, 0

for i in range(6):
    worksheet = workbook.add_worksheet()
for i in range(16):
    row, col = 0, 0
    worksheet = workbook.add_worksheet()
    for item in (expenses):
        worksheet.write(row, col, item)
        col += 1
    row,col=1,0
    for number, fio in (expenses2):
        worksheet.write(row, col, fio)
        row+=1


workbook.close()
