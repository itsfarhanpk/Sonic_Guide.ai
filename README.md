# 🎯 SonicGuide AI • Immersive Audio Tours

> **Transform Your Journey with Intelligent Audio Tours** - Where every step tells a story, and every landmark has a voice.

## 🌟 Overview

SonicGuide AI is an advanced audio tour generation system that creates personalized, immersive audio experiences for any location worldwide. Using cutting-edge AI agents, it crafts engaging narratives across architecture, history, culinary, and cultural themes, delivering studio-quality audio tours in seconds.

<img width="1303" height="634" alt="image" src="https://github.com/user-attachments/assets/29dd6b59-16c8-4e58-942e-46989d15f4b6" />

<img width="1298" height="637" alt="image" src="https://github.com/user-attachments/assets/512f2225-146c-4e4d-977b-6b7c023dd19b" />

## 🚀 Features

- 🎯 **Multi-Agent Architecture**: Specialized AI agents for different tour aspects
- 🌍 **Global Coverage**: Generate tours for any location worldwide
- 🎧 **Studio-Quality Audio**: Professional text-to-speech conversion
- ⚡ **Real-time Generation**: Create complete tours in under 60 seconds
- 🎨 **Personalized Content**: Tailored to user interests and preferences
- 📱 **Beautiful UI**: Modern gradient interface with intuitive controls
- 💾 **Downloadable Tours**: Save MP3 files for offline listening

## 🏗️ Architecture

```
SonicGuide AI Architecture:
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │◄──►│  Tour Manager   │◄──►│  AI Agents      │
│   (Frontend)    │    │  (Orchestrator) │    │  - Architecture │
└─────────────────┘    └─────────────────┘    │  - History      │
         │                     │              │  - Culinary     │
         ▼                     ▼              │  - Culture      │
┌─────────────────┐    ┌─────────────────┐    └─────────────────┘
│   OpenAI TTS    │    │   Web Search    │            │
│   (Audio Gen)   │    │   (Real-time)   │            ▼
└─────────────────┘    └─────────────────┘    ┌─────────────────┐
                                               │   OpenAI GPT    │
                                               │   (Content)     │
                                               └─────────────────┘
```

## 🛠️ Tech Stack

- **🤖 AI Framework**: OpenAI Agents SDK
- **🧠 Language Models**: GPT-4o, GPT-4o-mini
- **🎤 Text-to-Speech**: OpenAI TTS-1
- **🎨 Frontend**: Streamlit
- **🐍 Backend**: Python 3.12
- **📊 Data Handling**: Pydantic, JSON
- **🎭 UI Styling**: Custom CSS, Gradient Themes
- **🔍 Real-time Data**: Web Search Integration

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Aiengineer360/Sonic_Guide.Ai
cd Sonic_Guide.Ai
```

### 2. Create Conda Environment

```bash
# Create new conda environment
conda create -n sonicguide python=3.10 -y

# Activate environment
conda activate sonicguide
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up OpenAI API Key

```bash
# Option 1: Environment variable
export OPENAI_API_KEY='your-api-key-here'

# Option 2: Set in the app UI (recommended)
```

## 🎮 Usage

### Starting the Application

```bash
streamlit run ai-audio-tour-agent.py
```

### Quick Start Guide

1. **🔐 Enter API Key**: Input your OpenAI API key in the sidebar
2. **📍 Choose Destination**: Enter any city, landmark, or location
3. **🎯 Select Interests**: Choose from Architecture, History, Culinary, Culture
4. **⚙️ Configure Settings**: Set duration and voice style in sidebar
5. **🚀 Generate Tour**: Click the generate button
6. **🎧 Listen & Download**: Play the audio or download MP3

## 🤖 AI Agents Overview

### 🏗️ Architecture Agent
- **Role**: Describes buildings, design elements, urban planning
- **Style**: Detailed, descriptive, technical insights
- **Output**: Architectural narratives and visual descriptions

### 📜 History Agent
- **Role**: Provides historical context and stories
- **Style**: Authoritative, professorial, engaging narratives
- **Output**: Historical facts and timeline-based content

### 🍜 Culinary Agent
- **Role**: Highlights local food and dining experiences
- **Style**: Enthusiastic, passionate, appetizing descriptions
- **Output**: Food recommendations and culinary traditions

### 🎭 Culture Agent
- **Role**: Explores local traditions and customs
- **Style**: Warm, respectful, authentic insights
- **Output**: Cultural practices and community insights

### 🎛️ Orchestrator Agent
- **Role**: Combines all agent outputs into cohesive tour
- **Style**: Natural, conversational, seamless transitions
- **Output**: Complete audio tour script

### 📊 Planner Agent
- **Role**: Allocates time based on user preferences
- **Style**: Analytical, optimized distribution
- **Output**: Time allocation plan for each section

## 📁 Project Structure

```
Sonic_Guide.Ai/
├── ai-audio-tour-agent.py     # Main Streamlit application
├── agent.py                   # AI agent definitions and configurations
├── manager.py                 # Tour management and orchestration
├── printer.py                 # Console output formatting
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
```

### Customization Options

- Modify `agent.py` to adjust agent instructions
- Update CSS in `ai-audio-tour-agent.py` for different themes
- Adjust word limits in `manager.py` for content length
- Modify TTS parameters for different voice styles

## 🚀 Deployment

### Local Deployment

```bash
# Run with specific port
streamlit run ai-audio-tour-agent.py --server.port 8501
```

## 📊 Performance

- ⏱️ **Generation Time**: 30-60 seconds for complete tour
- 🎧 **Audio Quality**: Studio-grade 128kbps MP3
- 🌐 **Location Coverage**: Global, any address or landmark
- 📝 **Content Length**: 150 words per minute (adjustable)

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🆘 Support

If you encounter any issues:

1. Check the [OpenAI API status](https://status.openai.com/)
2. Verify your API key has sufficient credits
3. Ensure all dependencies are installed correctly
4. Check the browser console for errors

## 🙏 Acknowledgments

- **OpenAI** for GPT models and TTS technology
- **Streamlit** for the excellent web framework
- **Community contributors** for feedback and testing

## 📞 Contact

- **GitHub**: [@itsfarhanpk](https://github.com/itsfarhanpk)
- **Email**: [itsfarhan.pk@gmail.com]
- **Phone No**: [+92 304 040 0067]

---

**⭐ If you find this project useful, please give it a star on GitHub!**

---

*SonicGuide AI - Making every journey an immersive story waiting to be heard.* 🎧✨
