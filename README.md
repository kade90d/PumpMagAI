# AI Magazine Generator

An automated AI-powered magazine creation tool that fetches news, generates original articles, creates visuals, and designs a complete magazine for publishing.

## Features
- Fetch trending AI-related news and summarize them.
- Generate original long-form articles using GPT models.
- Create visuals using DALL·E.
- Layout and design magazines with pre-built templates.
- Publish magazines online or distribute via email.

## Setup Instructions

### Prerequisites
- Python 3.9+
- OpenAI API Key
- NewsAPI Key (optional for news fetching)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Magazine-Generator.git
   cd AI-Magazine-Generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Copy `.env.example` to `.env` and add your API keys.

5. Run the application:
   ```bash
   python app.py
   ```

## Usage
- Access the web interface at `http://localhost:5000`.
- Select topics and generate magazines.

## Deployment
Use the provided `Dockerfile` for containerized deployment.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for feedback.

## License
This project is licensed under the MIT License.