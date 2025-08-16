from flask import Flask, render_template, request, redirect, url_for
import uuid  # Para gerar IDs únicos

app = Flask(__name__)
cards = []

@app.route('/')
def home():
    return render_template('base.html')  # ou redirecionar para uma página inicial

@app.route('/cto', methods=['GET', 'POST'])
def cto():
    if request.method == 'POST':
        dados = {
            'id': str(uuid.uuid4()),  # ID único
            'codigo_os': request.form['codigo_os'],
            'cto': request.form['cto'],
            'regiao': request.form['regiao'],
            'upc_apc': request.form['upc_apc'],
            'splitter': request.form['splitter'],
            'nivel_antes': request.form['nivel_antes'],
            'nivel_pos': request.form['nivel_pos'],
            'problema': request.form['problema'],
            'resolucao': request.form['resolucao'],
            'material': request.form['material'],
            'endereco': request.form['endereco'],
            'localizacao': request.form['localizacao']
        }
        cards.append(dados)
        return redirect(url_for('cto'))
    return render_template('cto.html', cards=cards)

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    card = next((c for c in cards if c['id'] == id), None)
    if not card:
        return "Card não encontrado", 404

    if request.method == 'POST':
        card.update({
            'codigo_os': request.form['codigo_os'],
            'cto': request.form['cto'],
            'regiao': request.form['regiao'],
            'upc_apc': request.form['upc_apc'],
            'splitter': request.form['splitter'],
            'nivel_antes': request.form['nivel_antes'],
            'nivel_pos': request.form['nivel_pos'],
            'problema': request.form['problema'],
            'resolucao': request.form['resolucao'],
            'material': request.form['material'],
            'endereco': request.form['endereco'],
            'localizacao': request.form['localizacao']
        })
        return redirect(url_for('cto'))

    return render_template('editar.html', card=card)

@app.route('/encerrar/<id>', methods=['POST'])
def encerrar(id):
    global cards
    cards = [c for c in cards if c['id'] != id]
    return redirect(url_for('cto'))

@app.route('/pon', methods=['GET', 'POST'])
def pon():
    if request.method == 'POST':
        dados = {
            'id': str(uuid.uuid4()),  # ID único
            'codigo_os': request.form['codigo_os'],
            'pon': request.form['pon'],
            'cliente_afetado': request.form['cliente_afetado'],
            'media_nivel': request.form['media_nivel'],
            'problema': request.form['problema'],
            'resolucao': request.form['resolucao'],
            'material': request.form['material'],
            'splitter_primaria': request.form['splitter_primaria'],
            'localizacao': request.form['localizacao']
        }
        cards.append(dados)
        return redirect(url_for('pon'))
    return render_template('pon.html', cards=cards)

@app.route('/editar_pon/<id>', methods=['GET', 'POST'])
def editar_pon(id):
    card = next((c for c in cards if c['id'] == id), None)
    if not card:
        return "Card não encontrado", 404

    if request.method == 'POST':
        card.update({
            'codigo_os': request.form['codigo_os'],
            'pon': request.form['pon'],
            'cliente_afetado': request.form['cliente_afetado'],
            'media_nivel': request.form['media_nivel'],
            'problema': request.form['problema'],
            'resolucao': request.form['resolucao'],
            'material': request.form['material'],
            'splitter_primaria': request.form['splitter_primaria'],
            'localizacao': request.form['localizacao']
        })
        return redirect(url_for('pon'))

    return render_template('editar_pon.html', card=card)

@app.route('/encerrar_pon/<id>', methods=['POST'])
def encerrar_pon(id):
    global cards
    cards = [c for c in cards if c['id'] != id]
    return redirect(url_for('pon'))

@app.route('/link', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        dados = {
            'id': str(uuid.uuid4()),  # ID único
            'codigo_os': request.form['codigo_os'],
            'Link': request.form['Link'],
            'Porta': request.form['Porta'],
            'nivel_antes': request.form['nivel_antes'],
            'nivel_pos': request.form['nivel_pos'],
            'problema': request.form['problema'],
            'resolucao': request.form['resolucao'],
            'material': request.form['material'],
        }
        cards.append(dados)
        return redirect(url_for('link'))
    return render_template('link.html', cards=cards)


@app.route('/editar_link/<id>', methods=['GET', 'POST'])
def editar_link(id):
    card = next((c for c in cards if c['id'] == id), None)
    if not card:
        return "Card não encontrado", 404

    if request.method == 'POST':
        card.update({
            'codigo_os': request.form['codigo_os'],
            'Link': request.form['Link'],
            'Porta': request.form['Porta'],
            'nivel_antes': request.form['nivel_antes'],
            'nivel_pos': request.form['nivel_pos'],
            'problema': request.form['problema'],
            'resolucao': request.form['resolucao'],
            'material': request.form['material'],
        })
        return redirect(url_for('link'))

    return render_template('editar_link.html', card=card)

@app.route('/encerrar_link/<id>', methods=['POST'])
def encerrar_link(id):
    global cards
    cards = [c for c in cards if c['id'] != id]
    return redirect(url_for('link'))



if __name__ == '__main__':
    app.run(debug=True)
