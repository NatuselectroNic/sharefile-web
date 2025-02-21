from flask import Flask, request, render_template, send_file, jsonify
import os
from datetime import datetime, timedelta

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

files = os.listdir(UPLOAD_FOLDER)

@app.route('/')
def index():
    # 每次请求都重新读取文件列表
    current_files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=current_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # 获取 Content-Range 头
        content_range = request.headers.get('Content-Range')
        if content_range:
            # 修正解析逻辑
            range_part = content_range.split(' ')[1]
            range_spec, total_size = range_part.split('/')  # 先按斜杠分割
            range_start, range_end = map(int, range_spec.split('-'))  # 再处理范围部分
            
            with open(file_path, 'ab') as f:
                f.seek(range_start)
                f.write(file.read())
        else:
            file.save(file_path)

        global files
        files = os.listdir(UPLOAD_FOLDER)
        
        return jsonify({'status': 'success'})
    except Exception as e:
        print('上传过程中出现错误:', str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
