import re

branch = 'dev'

result_file = open("python\.bindings.txt", "w")
source_file = open("python\.bindings.queue.txt", "r")
standart_file = open("python\.bindings.standart.txt", "r")
connection_file = open("python\.bindings.connection.txt", "r")


result = ''
standart = standart_file.read()
lines = source_file.readlines()

for line in lines:
    if "#" in line:
        if "#>" in line:
            h = line.strip()
            l = h.find(' #>')
            result += '\n' + h[l:] + '\n'
        if re.search(r'.*#.*dev.*' , line) is not None and branch == 'dev' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if (re.search(r'.*#.*test\n.*', line) is not None or re.search(r'.*#.*test,.*', line) is not None) and branch == 'test' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if (re.search(r'.*#.*prod\n', line) is not None or re.search(r'.*#.*prod,', line) is not None) and branch == 'prod' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if re.search(r'.*#.*qf.*', line) is not None and branch == 'qf' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if re.search(r'.*#.*prodlike2.*', line) is not None and branch == 'prodlike2' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if re.search(r'.*#.*test2.*', line) is not None and branch == 'test2' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if (re.search(r'.*#.*prodlike\n.*', line) is not None or re.search(r'.*#.*prodlike,.*', line) is not None) and branch == 'prodlike' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
    else:
        newresult = standart
        newresult = newresult.replace("@tagName@", line.strip())
        result += newresult
result = result + '\n'
curLineBranch = ''
conlines = connection_file.readlines()
for conline in conlines: 
    if "#" in conline:
        curLineBranch = conline
    else:
        if branch in curLineBranch or curLineBranch == '':
            result += conline

result_file.write(result)

result_file.close()
source_file.close()
standart_file.close()
connection_file.close()