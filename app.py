from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>CT Review Tool</title></head>
<body>
    <h1>CT Review Tool</h1>
    <p>Upload a document to begin analysis</p>
    <input type="file" id="file" accept=".docx">
    <button onclick="upload()">Upload</button>
    <div id="result"></div>
    <script>
        function upload() {
            document.getElementById('result').innerHTML = 'Document analysis feature coming soon...';
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)