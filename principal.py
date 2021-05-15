from flask import Flask,render_template,request,redirect,url_for,flash
from operaciones import suma,resta,raiz
correos = []
contrasenas = []
telefonos = []
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apartamentos', methods=['GET','POST'])
def apartamentos():
    if request.method=='POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        sum = suma(n1,n2)
        rest = resta(n1,n2)
        raizz = raiz(n1,n2)
        return render_template('apartamentos.html',n1=n1,n2=n2,sum=sum,rest=rest,raizz=raizz)

    return render_template('apartamentos.html')

@app.route('/contactanos',methods=['POST'])
def contactanos():
    if request.method=='POST':
        correo = request.form['correo']
        contras = request.form['contras']
        tel = request.form['tel']
        correos.append(correo)
        tam = len(correos)
        contrasenas.append(contras)
        telefonos.append(tel)
        return render_template('contactanos.html',correos=correos,contrasenas=contrasenas,telefonos=telefonos,tam=tam)
   
    return render_template('contactanos.html')


if __name__ == '__main__':
    app.run(debug=True)

