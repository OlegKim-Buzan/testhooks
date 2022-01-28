import re

branch = 'dev'

result_file = open("python\.bindings.txt", "w")
source_file = open("python\.bindings.queue.txt", "r")
standart_file = open("python\.bindings.standart.txt", "r")
connection_file = open("python\.bindings.connection.txt", "r")


result = ''
standart = standart_file.read()
lines = source_file.readlines()
connection = connection_file.read()

for line in lines:
    if "#" in line:
        if re.search('dev', line) is not None and branch == 'dev' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if re.search('test', line) is not None and branch == 'test' :
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
        
result += connection
result_file.write(result)

result_file.close()
source_file.close()
standart_file.close()
connection_file.close()