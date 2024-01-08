# GGUF-PY-AGENT

Python server for GGUF model-based assistance that I quickly whipped up to test/implement some models supported by llama.ccp.

<br>

## Prerequisites

1. **Visual Studio:**

   - C++ CMake tools for Windows
   - C++ core features
   - Windows 10/11 SDK

2. **CUDA Toolkit:**

   Download and install CUDA Toolkit 12.2 from [NVIDIA CUDA Toolkit Archive](https://developer.nvidia.com/cuda-12-2-0-download-archive?target_os=Windows)


3. **Conda Environment (Recommend):**
   ```bash
   conda create --name {your_env_name}
   conda activate {your_env_name}
   ```
<br>

## Installation Steps

1. **Set CMake Arguments:**

   ```bash
   set CMAKE_ARGS=-DLLAMA_CUBLAS=on
   set FORCE_CMAKE=1

   ```

2. **Install Llama-Cpp-Python:**
   ```bash
   pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
   ```

For a detailed installation guide with reference information, you can follow the tutorial on Medium: [Installing Llama-Cpp-Python with NVIDIA GPU Acceleration on Windows: A Short Guide](https://medium.com/@piyushbatra1999/installing-llama-cpp-python-with-nvidia-gpu-acceleration-on-windows-a-short-guide-0dfac475002d)

<br>

3. **Install Packages:**
   ```bash
   pip install -r requirements.txt
   ```
<br>

## ENV
**Create .env file.** \
Make sure to replace *{Your model path}* with the actual path and model you want to use.
```env
MODEL_PATH={Your model path}
N_GPU_LAYERS=-1
N_CTX=2048
N_BATCH=32
PORT=8083
APP_URL=localhost
AGENT_PROMPT=You are a professional assistance.
PREDEFINED_MESSAGES_FORMATTER_TYPE=CHATML
DEBUG_OUTPUT=True
```
<br>

## Run
```bash
python app.py
```

<br>

## Example Request
```bash
curl --location 'http://127.0.0.1:8083/generate' \
--header 'Content-Type: application/json' \
--data '{"input_text": "Hey, what can you do?", "max_tokens": 72}'
```