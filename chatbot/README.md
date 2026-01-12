# UOK FAQ Chatbot

A professional, production-ready Android application for University of Kabianga (UOK) FAQ assistance, built with Python and Kivy.

## Features

- **AI Integration**: Connects to Google Gemini API for intelligent responses
- **Offline Support**: Falls back to local FAQ when internet is unavailable
- **Modern UI**: WhatsApp-style interface with UOK branding (Deep Green #006400 and Gold #FFD700)
- **Interactive Elements**: "Thinking..." animation while processing requests

## Building for Android

### Prerequisites

- Linux system (Ubuntu/Debian recommended) or Google Colab
- Python 3.6+
- Java JDK 8

### Installation and Setup

1. **Install Buildozer**:
   ```bash
   sudo apt update
   sudo apt install -y build-essential git python3 python3-pip autoconf libtool pkg-config
   pip3 install buildozer
   ```

2. **Initialize Buildozer** (if needed):
   ```bash
   buildozer init
   ```
   (This step is not needed if buildozer.spec is already present)

3. **Build the APK**:
   ```bash
   buildozer android debug
   ```

4. **For a release APK**:
   ```bash
   buildozer android release
   ```

### Google Colab Instructions

1. Open Google Colab (colab.research.google.com)
2. Create a new notebook
3. Run the following commands:

```bash
# Install dependencies
!apt update && apt install -y build-essential git python3 python3-pip autoconf libtool pkg-config

# Install buildozer
!pip3 install buildozer

# Clone your project (replace with your actual repository)
!git clone https://github.com/yourusername/uok-faq-chatbot.git
%cd uok-faq-chatbot

# Build the APK
!buildozer android debug
```

### Configuration Notes

- The application requires Internet and Network State permissions
- The app is configured for portrait orientation only
- Package name: `org.uok.faqbot`
- App title: `UOK FAQ Bot`

### API Key Setup

To use the Google Gemini API integration:

1. Get an API key from [Google AI Studio](https://aistudio.google.com/)
2. Replace `YOUR_GEMINI_API_KEY_HERE` in the `main.py` file with your actual API key
3. For production, consider using environment variables or secure storage

### Local Development

To run the application locally for testing:

```bash
pip install kivy kivy[base] requests urllib3
python main.py
```

### Troubleshooting

- If you encounter Java version issues, ensure you're using Java 8 or 11
- For memory issues during build, consider using a machine with at least 4GB RAM
- If the build fails, try cleaning with `buildozer android clean` before rebuilding

## App Structure

- `main.py`: Main application logic with AI integration and offline fallback
- `uok_chat.kv`: Kivy design language file for UI layout
- `buildozer.spec`: Build configuration for Android packaging

## FAQ Content

The offline FAQ includes information about:
- Admission processes and deadlines
- Fee structures and payment methods
- Student portal access
- General university information

## License

This project is available for use by the University of Kabianga community.