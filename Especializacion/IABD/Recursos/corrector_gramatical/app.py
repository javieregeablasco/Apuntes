from utilities_write import LLM_response
from flask import Flask, render_template, request, jsonify
import markdown
 
app = Flask(__name__)
 
MODOS = {
    'corregir': 'Corrección Gramatical',
    'resumir': 'Resumen',
    'mejorar': 'Mejora de Estilo',
    'formalizar': 'Formalizar Texto',
}
 
@app.route('/')
def home():
    return render_template('home.html', modos=MODOS)
 
@app.route('/procesar', methods=['POST'])
def procesar():
    if request.method == 'POST':
        texto = request.form.get('TEXTO', '').strip()
        modo = request.form.get('MODO', 'corregir').strip()
 
        if not texto:
            return jsonify({
                'error': 'Por favor, introduce un texto para procesar.',
                'resultado': None
            })
 
        if modo not in MODOS:
            return jsonify({
                'error': 'Modo no válido.',
                'resultado': None
            })
 
        try:
            resultado = LLM_response(texto, modo)
 
            print("=" * 50)
            print(f"MODO: {MODOS[modo]}")
            print(f"TEXTO ORIGINAL: {texto}")
            print(f"RESULTADO: {resultado}")
            print("=" * 50)
 
            resultado_html = markdown.markdown(
                resultado,
                extensions=['extra', 'nl2br', 'sane_lists']
            )
 
            return jsonify({
                'error': None,
                'resultado': resultado_html,
                'modo_nombre': MODOS[modo]
            })
 
        except Exception as e:
            return jsonify({
                'error': f'Error al procesar el texto: {str(e)}. Por favor, inténtalo de nuevo.',
                'resultado': None
            })
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
