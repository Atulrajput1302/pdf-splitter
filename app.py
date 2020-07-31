from flask import Flask, render_template, request, send_file
import pdfsplitter


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/success', methods=['POST'])
def success():
    #creating global varibales ---ensures we can acces this variables globally
    global start
    global end
    global file

    start = int(request.form['first'])

    end = int(request.form['last'])


    #for file type input we use --->   request.files['<file-nametag>']
    f=request.files['file']
    file=f.filename
    f.save(file)

#returning the templates
    return render_template('success.html',
                            start = start,
                            end = end,
                            name = file)



@app.route('/convert')
def cropper():
    pdfsplitter.cropper(start, end, file)
    return render_template('download.html')



@app.route('/download')
def download():
    filename = file.split(".")[0] +"cropped.pdf"
    return send_file(filename, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
