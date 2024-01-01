import os
import fnmatch

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
    f.write("    font-weight: bold;\n")  # Updated: Added font-weight property
    f.write("    font-size: 24px;\n")  # Updated: Increased font size
    f.write("}\n")
    f.write("a:hover {\n")
    f.write("    color: #666;\n")
    f.write("}\n")
    f.write("h1 {\n")
    f.write("    font-size: 36px;\n")
    f.write("    font-weight: bold;\n")
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
    for file_path in file_list:
        file_name = file_path.replace("/Users/rajeshkumar/XXX/GIT/", "")  # Updated: Remove path name
        f.write(f'<li><a href="{file_name}">{file_name}</a></li>\n')  # Updated: Use modified file name
    f.write("</ul>\n")
    f.write("</body>\n")
    f.write("</html>\n")

print("HTML file generated:", output_file)
