import os

def create_index_files(curdir):
    if not os.path.isdir(curdir):
        return
    file_list = os.listdir(curdir)
    html = ''
    for file_folder in file_list:
        if os.path.isdir(file_folder):
            file_folder += '/'
        html += '<a href="' + file_folder + '">' + file_folder + '</a>'
    if os.path.exists(os.path.join(curdir, 'index.htm')):
        print('error path exists')
    with open(os.path.join(curdir, 'index.htm'),'w') as fo:
        fo.write('<html><head>'
                '<link rel="stylesheet" href="style.css" />'
                '</head><body>'+ html + '</body></html>')

create_index_files('.')


