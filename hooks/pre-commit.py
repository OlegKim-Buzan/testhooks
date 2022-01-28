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
        if re.fullmatch('dev', line) != 'None' and branch == 'dev' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            print(newresult)
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
        if re.fullmatch('test', line) != 'None' and branch == 'test' :
            h = line.strip()
            l = h.find(' #')
            pieceofline = h[:l]
            newresult = standart
            print(newresult)
            newresult = newresult.replace("@tagName@", pieceofline)
            result += newresult
    else:
        newresult = standart
        print(newresult)
        newresult = newresult.replace("@tagName@", line.strip())
        result += newresult
        
result += connection
result_file.write(result)

result_file.close()
source_file.close()
standart_file.close()