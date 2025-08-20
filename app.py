from flask import Flask, render_template, request, redirect, url_for
import uuid  # Para gerar IDs únicos

app = Flask(__name__)

# Listas separadas para cada tipo de card
cto_cards = []
pon_cards = []
link_cards = []
ativacao_cards = []

@app.route('/')
def home():
    return render_template('index.html')

# CTO
@app.route('/cto', methods=['GET', 'POST'])
def cto():
    if request.method == 'POST':
        dados = {
            'id': str(uuid.uuid4()),
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
        cto_cards.append(dados)
        return redirect(url_for('cto'))
    return render_template('cto.html', cards=cto_cards)

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    card = next((c for c in cto_cards if c['id'] == id), None)
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
    global cto_cards
    cto_cards = [c for c in cto_cards if c['id'] != id]
    return redirect(url_for('cto'))

# PON
@app.route('/pon', methods=['GET', 'POST'])
def pon():
    if request.method == 'POST':
        dados = {
            'id': str(uuid.uuid4()),
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
        pon_cards.append(dados)
        return redirect(url_for('pon'))
    return render_template('pon.html', cards=pon_cards)

@app.route('/editar_pon/<id>', methods=['GET', 'POST'])
def editar_pon(id):
    card = next((c for c in pon_cards if c['id'] == id), None)
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
    global pon_cards
    pon_cards = [c for c in pon_cards if c['id'] != id]
    return redirect(url_for('pon'))

# LINK
@app.route('/link', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        links = request.form.getlist('link[]')
        portas = request.form.getlist('porta[]')
        niveis_antes = request.form.getlist('nivel_antes[]')
        niveis_pos = request.form.getlist('nivel_pos[]')
        for link, porta, nivel_antes, nivel_pos in zip(links, portas, niveis_antes, niveis_pos):
            dados = {
                'id': str(uuid.uuid4()),
                'codigo_os': request.form['codigo_os'],
                'link': link,
                'porta': porta,
                'nivel_antes': nivel_antes,
                'nivel_pos': nivel_pos,
                'problema': request.form['problema'],
                'resolucao': request.form['resolucao'],
                'material': request.form['material'],
            }
            link_cards.append(dados)
        return redirect(url_for('link'))
    return render_template('link.html', cards=link_cards)

@app.route('/editar_link/<id>', methods=['GET', 'POST'])
def editar_link(id):
    card = next((c for c in link_cards if c['id'] == id), None)
    if not card:
        return "Card não encontrado", 404

    if request.method == 'POST':
        card.update({
            'codigo_os': request.form['codigo_os'],
            'link': request.form['link'],
            'porta': request.form['porta'],
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
    global link_cards
    link_cards = [c for c in link_cards if c['id'] != id]
    return redirect(url_for('link'))

#ATIVAÇÃO
@app.route('/ativacao', methods=['GET', 'POST'])
def ativacao():
    if request.method == 'POST':
        dados = {
            'id': str(uuid.uuid4()),
            'tecnico': request.form['tecnico'],
            'cto': request.form['cto'],
            'cliente': request.form['cliente'],
            'lacre': request.form['lacre'],
            'portas_livres': request.form['portas_livres'],
            'equipamento': request.form['equipamento'],
        }
        ativacao_cards.append(dados)
        return redirect(url_for('ativacao'))
    return render_template('ativacao.html', cards=ativacao_cards)

@app.route('/editar_ativacao/<id>', methods=['GET', 'POST'])
def editar_ativacao(id):
    card = next((c for c in ativacao_cards if c['id'] == id), None)
    if not card:
        return "Card não encontrado", 404

    if request.method == 'POST':
        card.update({
            'tecnico': request.form['tecnico'],
            'cto': request.form['cto'],
            'cliente': request.form['cliente'],
            'lacre': request.form['lacre'],
            'portas_livres': request.form['portas_livres'],
            'equipamento': request.form['equipamento'],
        })
        return redirect(url_for('ativacao'))

    return render_template('editar_ativacao.html', card=card)

@app.route('/encerrar_ativacao/<id>', methods=['POST'])
def encerrar_ativacao(id):
    global ativacao_cards
    ativacao_cards = [c for c in ativacao_cards if c['id'] != id]
    return redirect(url_for('ativacao'))


if __name__ == '__main__':
    app.run(debug=True)
