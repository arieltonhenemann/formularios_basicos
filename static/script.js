// static/script.js

function adicionarCampos() {
  const container = document.getElementById('grupo-campos');
  const novoGrupo = document.createElement('div');
  novoGrupo.classList.add('grupo');
  novoGrupo.innerHTML = `
    <input name="Link[]" placeholder="Link" required>
    <input name="Porta[]" placeholder="Porta" required>
    <input name="nivel_antes[]" placeholder="Nível antes" required>
    <input name="nivel_pos[]" placeholder="Nível pos" required>
  `;
  container.appendChild(novoGrupo);
}
