from flask import Flask, render_template

app = Flask(__name__)
application = app

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts


roses_list = convert_to_dict("roses.csv")

pairs_list = []
for r in roses_list:
    pairs_list.append((r['Rose'], r['Name']) )

@app.route('/')
def index():
  return render_template('index.html', pairs = pairs_list, the_title="Rose Index")

@app.route('/rose/<num>')
def detail(num):
    try:
        rose_dict = roses_list[int(num)-1]
    except:
        return f"<h1>Invalid value for roses: {num}</h1>"
    return render_template('rose.html', rose=rose_dict, the_title=rose_dict['Name'])

if __name__ == '__main__':
  app.run(debug=True)
