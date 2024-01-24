# Sentimint: AI-Powered Crypto Sentiment Analysis

## Overview

Sentimint harnesses the power of AI to analyze sentiment in the cryptocurrency market, providing real-time insights. This project aims to parse through the latest news headlines and social media posts, identifying overall market sentiment as bullish, bearish, or neutral. Such insights are critical for investors and enthusiasts looking to make informed decisions in the fast-paced world of cryptocurrencies.

## Features

- **Real-Time Data Processing:** Fetches the latest news and social media posts related to cryptocurrencies.
- **Sentiment Analysis:** Utilizes advanced AI algorithms to assess and classify sentiments as positive, negative, or neutral.
- **User-Friendly Interface:** Displays the sentiment analysis results on a straightforward and intuitive web interface.
- **Oraichain Integration:** Planned integration with Oraichain for decentralized and reliable AI data processing.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8 or later
- Node.js and npm
- Access to news and sentiment analysis APIs

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your_username_/Sentimint.git
   ```
2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Setup the Frontend:**
   Navigate to the frontend directory and install dependencies:
   ```sh
   cd Sentimint/frontend
   npm install
   ```

### Configuration

- Set up API keys and endpoints in the configuration file.
- Configure the connection to Oraichain (future implementation).

## Usage

- Run the Python backend to start fetching and processing data:
  ```sh
  python3 crypto.py
  ```
- Start the frontend application:
  ```sh
  npm start
  ```

## Roadmap

- [x] Initial setup with news API and sentiment analysis.
- [ ] Integrate with Oraichain for decentralized AI services.
- [ ] Enhance the user interface for better experience and data visualization.
- [ ] Expand the data sources to include more social media platforms and news outlets.

## Contributing

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
