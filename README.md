# sharefile-web
运行在网页端的一个局域网内文件共享工具，客户端仅需在同一网络下打开网页即可上传下载文件

# 文件共享系统

基于Flask的轻量级文件共享解决方案，支持断点续传和自动刷新功能，适合局域网内快速搭建文件共享服务。

![界面预览](screenshot.png)

## 主要功能

### 文件管理
- 📤 拖拽上传文件
- ⏯️ 支持上传暂停/恢复
- 📥 直接下载文件
- 🔄 自动刷新文件列表（每30秒）
- 🗑️ 文件列表实时更新

### 上传功能
- 🧩 分块上传（每块1MB）
- 📊 实时进度显示
- ⚡ 断点续传支持
- ⚠️ 上传失败自动提示

## 快速开始

### 环境要求
- Python 3.6+
- Flask 2.0+

### 安装步骤
1. 克隆仓库
   ```bash
   git clone https://github.com/NatuselectroNic/sharefile-web.git
   cd file-share
   ```
2. 安装依赖
   ```bash
   pip install flask
   ```
3. 创建上传目录
   ```bash
   mkdir uploads
   ```

### 启动服务
```bash
# Windows
start.bat

# Linux/Mac
python app.py
```
访问 http://localhost:5000

### 停止服务
```bash
# Windows
stop.bat

# Linux/Mac
Ctrl+C
```

## 技术细节

### 后端实现
- 使用Flask处理HTTP请求
- 分块上传处理逻辑：
  ```python
  # app.py
  content_range = request.headers.get('Content-Range')
  if content_range:
      range_part = content_range.split(' ')[1]
      range_spec, total_size = range_part.split('/')
      range_start, range_end = map(int, range_spec.split('-'))
      # 写入文件对应区块
  ```

### 前端实现
- 原生JavaScript实现分块上传
- 进度条动态更新
- 自动刷新机制：
  ```javascript
  setInterval(() => {
      fetch('/').then(response => response.text())
      .then(html => {
          // 更新文件列表
      });
  }, 30000);
  ```

## 项目结构
```
file-share/
├── app.py            # Flask主程序
├── start.bat         # Windows启动脚本
├── stop.bat          # Windows停止脚本
├── uploads/          # 上传文件存储目录
└── templates/
    └── index.html    # 前端界面
```

## 常见问题

Q: 上传大文件时卡顿怎么办？  
A: 这是正常现象，程序采用分块上传机制，大文件需要较长时间处理。

Q: 如何修改上传目录？  
A: 修改app.py中的`UPLOAD_FOLDER`变量路径。

Q: 支持多用户同时使用吗？  
A: 当前版本为单机版，适合小范围使用，如需多用户支持需添加认证功能。
```

需要我添加部署到生产环境的说明吗？或者需要补充其他方面的内容？</think>

好的，用户让我帮忙写一个详细的README文件，用于他们的GitHub仓库。他们已经开发了一个基于Flask的文件共享系统，支持断点续传和自动刷新功能。用户希望这个README能全面介绍项目的功能、安装步骤、技术细节等，方便其他用户理解和使用。

首先，我需要回顾用户提供的代码和之前的对话，确保理解所有功能点。用户提到了分块上传、断点续传、自动刷新、前端界面等。同时，他们可能有隐藏命令行窗口和关闭脚本的需求，但后来回退到简单版本，所以README需要反映当前的实际配置。

接下来，考虑README的结构。通常包括项目简介、功能列表、安装步骤、使用说明、技术细节、项目结构、常见问题等部分。需要确保每个部分都详细且清晰，尤其是安装和启动步骤，避免用户遇到问题。

然后，要检查技术细节部分是否正确。例如，后端处理分块上传的代码片段是否准确，前端自动刷新的JavaScript代码是否正确引用。同时，项目结构需要与实际文件结构一致，包括app.py、start.bat、stop.bat、uploads目录等。

用户可能希望README有良好的格式，比如使用适当的Markdown标签、代码块、列表等，使文档易读。可能需要添加截图或示例图片，但用户暂时没有提供，所以用占位符代替。

另外，考虑到用户之前遇到的问题，比如关闭脚本的安全性，虽然在README中可能不需要详细说明，但可以在常见问题部分简要提及，或者确保提供的停止脚本是最终安全的版本。

最后，需要确认所有步骤在最新版本的代码中有效，例如启动脚本是否已经回退到不隐藏窗口的版本，停止脚本是否使用安全的方法终止进程。确保README中的命令和说明与当前代码一致，避免用户按照文档操作时出现错误。

总结来说，需要将用户提供的所有信息整合成一个结构清晰、内容详实的README文档，涵盖项目介绍、功能、安装、使用、技术实现和常见问题，确保用户和贡献者能够顺利使用和了解项目。
</think>

这里是为你的文件共享系统准备的完整README文档，包含部署说明和更多技术细节：

```markdown:README.md
# FileShare 文件共享系统

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

一个基于Flask的轻量级局域网文件共享解决方案，支持大文件分块上传和断点续传。

## 功能亮点 ✨

- 🚀 **分块上传** - 支持大文件分割上传（默认1MB/块）
- ⏯ **断点续传** - 网络中断后可恢复上传
- 📊 **实时进度** - 可视化上传进度条
- 🔄 **自动同步** - 30秒自动刷新文件列表
- 🛠 **简单部署** - 单文件即可运行，无需数据库

## 快速入门 🚪

### 环境准备
- Python 3.6+
- Flask 2.0+

```bash
# 克隆仓库
git clone https://github.com/NatuselectroNic/sharefile-web.git
cd fileshare-system

# 安装依赖
pip install flask

# 创建上传目录 (Windows跳过)
mkdir uploads
```

### 启动服务
```bash
# Windows
双击 start.bat

# Linux/Mac
python app.py
```
访问 ➡️ [http://localhost:5000](http://localhost:5000)

### 停止服务
```bash
# Windows
双击 stop.bat

# Linux/Mac
Ctrl + C
```

## 技术架构 🛠️

### 后端设计
```python
# 分块上传处理
@app.route('/upload', methods=['POST'])
def upload_file():
    content_range = request.headers.get('Content-Range')
    if content_range:
        # 解析范围头 bytes 0-99999/100000
        range_part = content_range.split(' ')[1]
        range_spec, total_size = range_part.split('/')
        start, end = map(int, range_spec.split('-'))
        # 定位写入位置
        with open(file_path, 'ab') as f:
            f.seek(start)
            f.write(file.read())
```

### 前端实现
```javascript
// 分块上传核心逻辑
function uploadChunk() {
    const chunk = file.slice(start, end);
    let formData = new FormData();
    formData.append('file', chunk);
    
    xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.setRequestHeader('Content-Range', `bytes ${start}-${end-1}/${file.size}`);
    
    // 更新进度条
    xhr.upload.onprogress = function(e) {
        const percent = ((start + e.loaded) / file.size * 100).toFixed(2);
        progressBar.style.width = percent + '%';
    };
}
```

## 高级配置 ⚙️

### 修改上传参数
在 `app.py` 中调整配置：
```python
UPLOAD_FOLDER = 'custom_uploads'  # 修改上传目录
CHUNK_SIZE = 1024 * 1024 * 2      # 改为2MB分块
```

### 生产环境部署
推荐使用Waitress作为生产服务器：
```bash
pip install waitress
waitress-serve --port=5000 app:app
```

## 项目结构 📂
```
.
├── app.py                 # Flask主程序
├── start.bat              # Windows启动脚本
├── stop.bat               # Windows停止脚本
├── README.md              # 说明文档
├── uploads/               # 上传文件存储目录
└── templates/
    └── index.html         # 前端界面
```

## 常见问题 ❓

### 上传速度慢怎么办？
- 尝试增大分块大小（修改CHUNK_SIZE）
- 确保服务器和客户端在同一局域网

### 如何限制上传文件类型？
在 `app.py` 的upload_file函数中添加：
```python
allowed_ext = {'txt', 'pdf', 'png'}
if '.' in filename and filename.rsplit('.', 1)[1].lower() not in allowed_ext:
    return '文件类型不支持', 400
```

## 贡献指南 🤝
欢迎提交Issue和PR！建议步骤：
1. Fork仓库
2. 创建特性分支 (`git checkout -b feature/awesome`)
3. 提交修改 (`git commit -m 'Add awesome feature'`)
4. 推送分支 (`git push origin feature/awesome`)
5. 新建Pull Request

## 许可证 📄
本项目采用 MIT 许可证 - 详情见 [LICENSE](LICENSE) 文件
```

这个README包含：
1. 徽章展示项目状态
2. 分步安装指南
3. 核心代码片段
4. 生产环境部署建议
5. 可扩展配置说明
6. 贡献指南
7. 完整的文档结构

