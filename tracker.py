import os
import fnmatch
import time
from datetime import datetime

def list_files_with_extension(directory, extension):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list

directory = os.getcwd()  # BEGIN: Updated code
extension = ".pdf"
file_list = list_files_with_extension(directory, extension)

output_file = "tracker.html"
with open(output_file, "w") as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<style>\n")
    f.write("body {\n")
    f.write("    font-family: 'Times New Roman', Times, serif;\n")
    f.write("    margin: 20px;\n")
    f.write("}\n")
    f.write("a {\n")
    f.write("    text-decoration: none;\n")
    f.write("    color: #333;\n")
    f.write("    font-weight: bold;\n")
    f.write("    font-size: 24px;\n")
    f.write("}\n")
    f.write("a:hover {\n")
    f.write("    color: #666;\n")
    f.write("}\n")
    f.write("h1 {\n")
    f.write("    font-size: 36px;\n")
    f.write("    font-weight: bold;\n")
    f.write("    text-align: center;\n")
    f.write("    color: brown;\n")
    f.write("}\n")
    f.write(".premium-button {\n")
    f.write("    background-color: #333;\n")
    f.write("    color: #fff;\n")
    f.write("    padding: 10px 20px;\n")
    f.write("    border-radius: 20px;\n")
    f.write("    text-decoration: none;\n")
    f.write("}\n")

    # Mobile-friendly styles
    f.write("@media (max-width: 600px) {\n")
    f.write("    body {\n")
    f.write("        margin: 10px;\n")
    f.write("    }\n")
    f.write("    a {\n")
    f.write("        font-size: 18px;\n")
    f.write("    }\n")
    f.write("    h1 {\n")
    f.write("        font-size: 24px;\n")
    f.write("    }\n")
    f.write("}\n")

    f.write("</style>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<h1>File Tracker</h1>\n")
    f.write("<ul>\n")

    # Segment href based on commonness of directory
    dir_segments = set()
    for file_path in file_list:
        dir_path = os.path.dirname(file_path)
        dir_segments.add(dir_path)
    current_dir = os.getcwd()
    print("Current directory:", current_dir)
    
    # Sort dir_segments in alphabetical order
    dir_segments = sorted(dir_segments)
    
    for dir_segment in dir_segments:
        f.write('<div style="border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; border-radius: 10px; box-shadow: 2px 2px 5px #888;">\n')  # Added box, shading, and round edges
        dir_nam = dir_segment.replace(str(current_dir), "")
        modified_time = time.ctime(os.path.getmtime(dir_segment))
        modified_time = datetime.strptime(modified_time, "%a %b %d %H:%M:%S %Y")
        modified_time = modified_time.strftime("%a %b %d %I:%M:%S %p")
        f.write(f'<h2 style="background-color: #333; color: #fff; padding: 5px; border-radius: 10px;">{dir_nam} - <span style="color: #ff0000;">{modified_time.split()[0]}</span> <span style="color: #00ff00;">{modified_time.split()[1]}</span> <span style="color: white;">{modified_time.split()[2]}</span> <span style="color: #ff00ff;">{modified_time.split()[3]}</span></h2>\n')  # Added background color, round edges, and file modification time with contrasting colors
        f.write("<ul>\n")
        for file_path in file_list:
            if os.path.dirname(file_path) == dir_segment:
                file_name = os.path.basename(file_path)
                f.write(f'<li><a href="{file_path}" style="background-color: #f9f9f9;">{file_name}</a></li>\n')  # Added contrast background color to href link
        f.write("</ul>\n")
        f.write("</div>\n")  # Added box and shading

    f.write("</ul>\n")
    f.write("</body>\n")
    f.write("</html>\n")

print("HTML file generated:", output_file)
