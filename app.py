from Bio.SeqUtils import ProtParam
from flask import Flask, request, jsonify, render_template
from Bio.Seq import Seq
from Bio import SeqIO
import os
from flask_cors import CORS
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate_sequence():
    sequence = None
    sequence_type = None

    if 'sequence' in request.form and request.form['sequence']:
        sequence = request.form['sequence']
        sequence_type = request.form['type']
    else:
        fasta_file = request.files.get('file')
        if fasta_file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], fasta_file.filename)
            fasta_file.save(filepath)

            with open(filepath, 'r') as f:
                for record in SeqIO.parse(f, "fasta"):
                    sequence = str(record.seq)
            os.remove(filepath)
            sequence_type = request.form.get('type', default='dna')

    if not sequence:
        return jsonify({'error': 'No sequence provided'}), 400

    seq_obj = Seq(sequence)

    if sequence_type.lower() == 'dna':
        protein = str(seq_obj.translate(to_stop=True))
    else:
        protein = str(seq_obj.transcribe().translate(to_stop=True))

    X = ProtParam.ProteinAnalysis(protein)

    aa_freq = X.get_amino_acids_percent()
    mol_weight = X.molecular_weight()
    iso_point = X.isoelectric_point()

    return jsonify({
        'protein': protein,
        'protein_data': {
            'amino_acid_frequency': aa_freq,
            'molecular_weight': mol_weight,
            'isoelectric_point': iso_point
        }
    })


@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
