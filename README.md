# Bhande's Kitchen: Smart Recipe Generator

An interactive, AI-powered culinary companion built with Streamlit and the OpenAI API. It transforms available pantry ingredients into structured, step-by-step recipes tailored to specific dietary preferences, preparation times, and cooking styles.

## Features

- **Ingredient-Based Prompt Synthesis**: Enter arbitrary on-hand ingredients (spices, proteins, produce) to receive tailored meal concepts.
- **Customization Controls**: Select meal types (breakfast, lunch, dinner, snack), target prep times, spice levels, and dietary guidelines (vegetarian, vegan, keto, gluten-free).
- **Structured Recipe Output**: Generates ingredient checklists with precise measurements, step-by-step cooking instructions, and nutritional estimates.
- **Responsive UI**: Custom styled Streamlit interface optimized for mobile and desktop screens.

## Project Structure

```
BhandeKitchen/
├── SmartRecipeCreator.py  # Core Streamlit application and OpenAI API handler
├── requirements.txt       # Dependencies (streamlit, openai)
├── .env.example           # Environment template for API keys
├── .gitignore             # Python, Streamlit, and environment ignore rules
├── LICENSE                # MIT License
└── README.md              # Application overview and execution instructions
```

## Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Siddhesh-Bhande/BhandeKitchen.git
   cd BhandeKitchen
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API key:
   ```bash
   cp .env.example .env
   # Add your OpenAI API key inside .env, or input it directly in the app sidebar
   ```

4. Launch the application:
   ```bash
   streamlit run SmartRecipeCreator.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
