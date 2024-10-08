# AI_novel_generator
一个用于ai生成小说的web工具，基于本地ollama部署的模型进行小说生成。对硬件配置没有太高的要求。

![小说生成器示例图片](image/1.png)

## 部署步骤

### 1. 安装Ollama并启动服务器

首先，你需要安装Ollama并在本地启动服务器。请按照Ollama的官方文档进行安装和配置。

### 2. 下载所需模型

下载你需要的模型，例如Llama2、Mistral等。使用以下命令下载Llama2模型：

```bash
ollama pull llama2
```

### 3. 启动服务
启动服务，使用以下命令运行Python脚本：
``` bash
python main.py
```
#### 4. 访问默认地址
服务启动后，你可以通过访问默认地址来使用小说生成器：
```http
http://127.0.0.1:5000
```
## 使用方法
访问上述地址后，你将看到一个用户界面，输入你的小说主题或关键词，然后点击生成按钮，AI将根据你输入的内容生成小说。

您也可以将他部署到服务器上，然后通过网络进行访问。