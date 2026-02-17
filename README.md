# OmniTalk X

**English** | [简体中文](./docs/README_zh-CN.md)

## Introduction

> OmniTalk X is a secondary development based on the [OpenAOE](https://github.com/InternLM/OpenAOE) project, mainly borrowing its frontend design with functional extensions and optimizations.

**OmniTalk X** is an **AI multi-model group chat platform** based on OpenRouter.

With OmniTalk X, you can:

- **Group Chat Mode**: Get responses from multiple AI models simultaneously with one message
- **Private Chat Mode**: Have private conversations with a single AI
- **@Mention**: Use @ command to specify which AI should reply
- **Custom Prompt**: Set exclusive System Prompt for each AI
- **Group Management**: Create different AI groups and flexibly configure participating models
- **Context Memory**: Intelligently remember conversation history
- **Streaming Output**: Display AI responses in real-time

---

## Features

| Feature | Description |
|---------|-------------|
| Multi-Model Parallel Response | 10 mainstream AIs respond simultaneously |
| Private Chat Mode | Private conversation with a single AI |
| @Mention | Specify which AI to reply |
| System Prompt | Custom prompts for each AI |
| Group Function | Create and manage AI groups |
| Context Memory | Intelligently remember conversation history |
| Streaming Output | Display AI responses in real-time |

---

## Supported AI Models

| Model | Provider | Model ID |
|-------|----------|----------|
| ChatGPT | openai | openai/gpt-5.2 |
| Claude | anthropic | anthropic/claude-opus-4.5 |
| Grok | xai | x-ai/grok-4 |
| Gemini | google | google/gemini-3-pro-preview |
| GLM | zhipu | z-ai/glm-5 |
| Kimi | moonshot | moonshotai/kimi-k2.5 |
| MiniMax | minimax | minimax/minimax-m2.5 |
| Qwen | qwen | qwen/qwen3-max-thinking |
| DeepSeek | deepseek | deepseek/deepseek-v3.2 |
| Seed | bytedance | bytedance/seed-1.6-flash |

---

## Quick Start

### Requirements

- Python >= 3.9
- Node.js >= 16
- OpenRouter API Key

### Installation & Run

```bash
# 1. Clone the project
git clone https://github.com/niushuanan/omnitalk-x
cd omnitalk-x

# 2. Install frontend dependencies
cd omnitalkx/frontend
npm install

# 3. Build frontend
npm run build

# 4. Start backend
cd ../..
pip install -r requirements.txt
python main.py
```

After the service starts, visit:
- Frontend: http://localhost:5173
- Backend: http://localhost:8000

---

## Configuration

### Get OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/) to register an account
2. Get your API Key
3. Click the settings icon on the right side of the page and enter your API Key

### Custom System Prompt

Click the settings icon on the right side to set custom System Prompt for each AI model.

---

## Project Structure

```
OmniTalk X/
├── omnitalkx/
│   ├── frontend/          # Frontend project
│   │   ├── src/
│   │   │   ├── pages/    # Page components
│   │   │   ├── components/# Common components
│   │   │   ├── store/    # State management
│   │   │   └── config/   # Configuration files
│   │   └── public/       # Static resources
│   ├── backend/          # Backend project
│   │   ├── api/          # API routes
│   │   ├── service/      # Business services
│   │   └── config/       # Configuration files
│   └── main.py           # Project entry
└── docs/                 # Documentation
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 18 + TypeScript + Vite |
| State Management | Zustand |
| UI Components | sea-lion-ui |
| Backend | FastAPI + Python |
| API Aggregation | OpenRouter |

---

## Code Architecture Principles

### Frontend Architecture

- **Component-based Development**: Using React functional components + Hooks pattern
- **State Management**: Using Zustand for global state management, divided by functional modules
- **Type Safety**: TypeScript strict mode with clear interface definitions
- **Style Management**: Less preprocessor with unified theme color variables

### Backend Architecture

- **RESTful API**: Clear route design
- **Service Layering**: API → Service → Model layered decoupling
- **Configuration Management**: YAML configuration files, supporting multi-environment switching
- **Logging System**: Unified logging specification

### Core Design Patterns

1. **Frontend**
   - Custom Hooks: Reuse business logic
   - Context: Global configuration management
   - Interceptors: Unified request/response handling

2. **Backend**
   - Dependency Injection: Service layer decoupling
   - Streaming Response: Server-Sent Events (SSE)
   - CORS: Cross-Origin Resource Sharing configuration

---

## FAQ

### 1. How to get OpenRouter API Key?

Visit [OpenRouter](https://openrouter.ai/) to register an account and get your API Key in the personal center.

### 2. Why did the message sending fail?

- Check if the API Key is valid
- Check if the network connection is normal
- Confirm if the selected AI model is available

### 3. How to check consumed credits?

View usage statistics on the OpenRouter account page.

### 4. Does it support custom models?

Currently supports all models provided by OpenRouter, new models can be added through configuration files.

---

## License

MIT License
