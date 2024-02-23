import os
import datetime
from jinja2 import Environment, FileSystemLoader

def get_directory_structure(rootdir):
    dir = {
        'name': os.path.basename(rootdir),
        'type': 'directory',
        'children': [],
        'mtime': datetime.datetime.fromtimestamp(os.path.getmtime(rootdir)).strftime('%Y-%m-%d %I:%M:%S %p')
    }
    for item in os.listdir(rootdir):
        full_item = os.path.join(rootdir, item)
        if os.path.isdir(full_item):
            dir['children'].append(get_directory_structure(full_item))
        else:
            if item.endswith(('.tex', '.pdf', '.md','.png','.jpg','.jpeg','.py','.nb','.sh','.txt','ipynb','.json')):
                dir['children'].append({
                    'name': item,
                    'type': 'file',
                    'path': 'file://' + os.path.abspath(full_item),
                    # 'path': '/Visible/'+os.path.relpath(full_item),
                    'mtime': datetime.datetime.fromtimestamp(os.path.getmtime(full_item)).strftime('%Y-%m-%d %I:%M:%S %p')
                })
    return dir

def render_html(directory_structure):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('templates/template.html')
    html = template.render(directory_structure=directory_structure)
    with open('trackerD.html', 'w') as f:
        f.write(html)
    print('trackerD.html generated')

if __name__ == "__main__":
    directory_structure = get_directory_structure('Library')
    render_html(directory_structure)