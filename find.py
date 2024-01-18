





from flask import Flask, render_template, request

app = Flask(__name__)

def search_blood_banks(area, blood_group):
    blood_banks = []
    with open('blood_banks.csv', 'r') as csvfile:
        for line in csvfile:
            data = line.strip().split(',')
            if data[1] == area and data[2] == blood_group:
                blood_banks.append({
                    'blood_bank_name': data[0],
                    'area': data[1],
                    'blood_group': data[2],
                    'contact': data[3]
                })
    return blood_banks

@app.route('/', methods=['GET', 'POST'])
def blood_bank_search():
    if request.method == 'POST':
        area = request.form['area']
        blood_group = request.form['bloodgroup']
        blood_banks = search_blood_banks(area, blood_group)
        print("Blood Banks:", blood_banks)
        return render_template('result.html', blood_banks=blood_banks)

    return render_template('find.html')



if __name__ == '__main__':
    app.run(debug=True)
