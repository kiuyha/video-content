import os
import pandas as pd
import pdfkit

#untuk membaca spreadsheet dan list path foto
foto = 'Foto teman'
biodata = 'Biodata Angkatan 24 Sada.xlsx'
teman_list = os.listdir(foto)
data = pd.read_excel(biodata,0).drop('Unnamed: 4',axis=1)

def generate_htmlfoto(images):
    # Untuk menambhkan style ke foto yang akan di buat menjadi pdf
    html_template = '''
<style>
    body {
        display: flex;
        flex-wrap: wrap;
        justify-content: left; 
        width: 21cm; 
        height: 29.7cm; 
        background-color: #ffffff;
    }
    img {
        margin: 3px;
        object-fit: cover;
    }
</style>
</head>
<body>'''
    for image in images:
        html_template += image
    html_template += """</body>
</html>"""
    
    return html_template

def ConvertImageToHTML():
    # untuk mengubah path foto menjadi bentuk HTML
    Image_list = []
    for teman in teman_list:
        Image_path = os.path.join(foto,teman)
        ImageHTML = f'<img src="{Image_path}" style="width: 4cm; height: 6cm;">'
        Image_list.append(ImageHTML)
    return Image_list

def new_df():
    #membuat dataframe baru yang berisi tabel biodata
    new_data = pd.DataFrame()
    images = ConvertImageToHTML()
    biodata_kosong = []
    image_list = []
    for teman, image in zip(teman_list,images):
        teman = teman.replace('.jpg','')
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')     
            search = data[data['i'].str.contains(teman, case=False, na=False)]
            if search.empty:
                print(f"{teman} is not found do you want to skip it or change the name: ")
                user_input = input("'s' to skip and just write name if you want to change the search: ").lower()
                if user_input == 's':
                    biodata_kosong.append((teman,image))
                    break
                else:
                    teman = user_input
            else:
                if len(search) > 1:
                    print(f"{teman} memiliki {len(search)} pilihan")
                    print(search)
                    user_input = int(input("what the row you want to return: "))
                    search = data.iloc[[user_input]]
                image_list.append(image)
                break
        new_data = pd.concat([new_data, search])
    new_data.insert(0,'Foto',image_list)
    df_empty = pd.DataFrame(biodata_kosong, columns= ['i','Foto'])
    new_data = pd.concat([new_data, df_empty])
    new_data.insert(0,'No',range(1,len(new_data)+1))
    return new_data, image_list

def write_file(dataframe, path):
    # menyimpan HTML untuk data yang difilter dalam bentuk HTML
    html_style ='''
<style>
    table {
        width: 100%; /* Full width */
        border-collapse: collapse; /* Collapse borders */
        margin: 20px 0; /* Space around the table */
    }
    th, td {
        border: 1px solid #dddddd; /* Border for cells */
        text-align: center; /* Center text */
        padding: 12px; /* Padding inside cells */
    }
    th {
        background-color: #f2f2f2; /* Light gray background for headers */
    }
    tr:hover {
        background-color: #f5f5f5; /* Change background on hover */
    }
</style>
    '''
    html_df = dataframe.to_html(escape=False, index=False)
    html = html_style + html_df
    with open(f'{path}.html','w') as file:
        file.write(html)

def main():
    filtered_data_path = 'Biodata teman'
    filtered_data, image_list = new_df()
    html_images = generate_htmlfoto(image_list)
    write_file(filtered_data,filtered_data_path)
    with open('foto.html','w') as file:
        file.write(html_images)
    file.close() #memastikan file ditutup karena biasanya error
    pdfkit.from_file('foto.html','foto.pdf',options={"enable-local-file-access": ""}) #mengubah file html menjadi pdf

if __name__ == '__main__':
    main()