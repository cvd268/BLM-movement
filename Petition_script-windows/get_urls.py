file1 = open('urls.txt', 'r') 
file2 = open('change_urls.txt', 'w')
Lines = file1.readlines() 

for line in Lines:
    if '.change.org' in line:
        new_line = line.split('%26amp;sa%3DD%26amp;')[0] +'\n'
        file2.writelines(new_line)

file1.close()
file2.close()