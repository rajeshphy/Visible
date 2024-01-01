import json

def generate_html(button_data):
    html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Department Of Physics</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f2f2f2;
      margin: 0;
      padding: 0;
    }

    .container {
      max-width: 800px;
      margin: 20px auto;
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      text-align: center;  /* Center-align the content */
    }

    .premium-heading {
      background-color: #001F3F; /* Deep blue for heading */
      color: white;
      padding: 10px;
      margin-bottom: 20px;
      border-radius: 5px;
    }

    h1 {
      font-size: 36px;
      font-weight: bold;
      margin: 0;
    }

    .button-container {
      margin: 10px 0;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
    }

    .main-button {
      background-color: #333;
      color: white;
      padding: 10px;
      margin: 5px;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      transition: background-color 0.3s;
    }

    .main-button:hover {
      background-color: #555;
    }

    .nested-buttons {
      display: none;
      margin-top: 10px;
      width: 100%;
    }

    .nested-button {
      background-color: #ddd;
      color: #333;
      padding: 10px;
      margin: 5px;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      transition: background-color 0.3s;
    }

    .nested-button:hover {
      background-color: #ccc;
    }

    .nested-box {
      display: none;
      padding: 10px;
      border: 1px solid #ddd;
      background-color: #f9f9f9;
      border-radius: 5px;
      margin-top: 5px;
    }

    .nested-link {
      display: block;
      margin: 5px;
      color: #0066cc;
      text-decoration: none;
      font-size: 18px;
    }

    .footer {
      margin-top: 20px;
      padding: 10px;
      background-color: #FFD700; /* Subtle gold for footer */
      color: #333;
      border-radius: 5px;
    }
  </style>
</head>
<body>
<div class="container">
<div class="premium-heading">
  <h1>Physics</h1>
</div>
"""

    for button_number, button_name, nested_buttons in button_data:
        html_code += f"""
<!-- {button_name} -->
<div class="button-container">
  <button class="main-button" onclick="toggleNestedButtons({button_number})">{button_name}</button>
  
  <div class="nested-buttons" id="nestedButtons{button_number}">
"""

        for index, nested_button_info in enumerate(nested_buttons):
            nested_button_name, notes_links = nested_button_info['name'], nested_button_info['links']
            html_code += f"""
    <button class="main-button nested-button" onclick="toggleNestedBox({button_number}, {index})">
      {nested_button_name.strip()}
    </button>
"""

            html_code += f"""
    <div class="nested-box" id="nestedBox{button_number}_{index}">
"""
            a = 0
            for link in notes_links:
                a += 1
                html_code += f"""
      <a class="nested-link" href="{link['url']}" target="_blank">{link['name']}</a>
"""

            html_code += """
    </div>
"""

        html_code += """
  </div>
</div>
"""

    html_code += """
<div class="footer">
  <div class="footer-content">
    <p class="credit">&#169; 2023 design by <a href="https://rajeshphy.github.io" target="_blank">Rajesh Kumar</a></p>
  </div>
</div>

<script>
  function toggleNestedButtons(buttonNumber) {
    var nestedButtons = document.getElementById('nestedButtons' + buttonNumber);

    // Toggle the display property
    if (nestedButtons.style.display === 'none') {
      nestedButtons.style.display = 'block';
    } else {
      nestedButtons.style.display = 'none';
    }
  }

  function toggleNestedBox(mainButton, nestedButton) {
    var nestedBox = document.getElementById('nestedBox' + mainButton + '_' + nestedButton);

    // Toggle the display property
    if (nestedBox.style.display === 'none') {
      nestedBox.style.display = 'block';
    } else {
      nestedBox.style.display = 'none';
    }
  }
</script>

</body>
</html>
"""

    return html_code

# Rest of the code remains the same...


def read_button_data(file_path):
    button_data = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for entry in data:
                button_data.append((entry['number'], entry['name'], entry['nested_buttons']))
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return button_data


def main():
    input_file_path = 'button_data.json'  # Change this to the path of your input file
    output_file_path = 'physics.html'  # Change this to the desired output file path

    button_data = read_button_data(input_file_path)
    if button_data:
        html_code = generate_html(button_data)

        with open(output_file_path, 'w') as output_file:
            output_file.write(html_code)

        print(f"HTML code generated and saved to {output_file_path}")


if __name__ == "__main__":
    main()


'''
button_data.json file format:

[
  {
    "number": 1,
    "name": "MAIN BUTTON 1",
    "nested_buttons": [
      {"name": "Nested Button 1", "links": [{"name": "Link 1", "url": "URL1"}, {"name": "Link 2", "url": "URL2"}]},
      {"name": "Nested Button 2", "links": [{"name": "Link 3", "url": "URL3"}, {"name": "Link 4", "url": "URL4"}]}
    ]
  },
  {
    "number": 2,
    "name": "MAIN BUTTON 2",
    "nested_buttons": [
      {"name": "Nested Button 3", "links": [{"name": "Link 5", "url": "URL5"}, {"name": "Link 6", "url": "URL6"}]},
      {"name": "Nested Button 4", "links": [{"name": "Link 7", "url": "URL7"}, {"name": "Link 8", "url": "URL8"}]}
    ]
  }
  // ... More main buttons ...
]
'''


