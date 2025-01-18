# STORYCanvas

STORYCanvas is a web application designed to bring joy and entertainment to disabled individuals by creating beautiful, engaging stories. The application uses advanced algorithms to generate stories and seamlessly insert descriptive images, enhancing the explicability and immersive experience of the story.

## Features

### 1. Interactive Story Generation
- Create engaging, descriptive, and positive stories based on user-provided prompts.
- Select from various themes such as Adventure, Fantasy, Friendship, Mystery, and Nature.

### 2. AI-Powered Image Integration
- Automatically searches for and inserts relevant images into the story to enhance its visual appeal.
- Robust image search ensures high-quality results even when queries are ambiguous.

### 3. Downloadable Stories
- Save the generated story as a Word document for offline use or sharing.
- Each paragraph is complemented by an image to create a visually enriched storytelling experience.

### 4. Accessibility-Focused Design
- Designed with accessibility in mind, ensuring an inclusive experience for all users.

## Technologies Used

- **Python Libraries**:
  - `spacy`: For Natural Language Processing and extracting Subject-Verb-Object (SVO) pairs.
  - `sentence-transformers`: To compute sentence embeddings and measure semantic similarity.
  - `BeautifulSoup`: For parsing HTML during image searches.
  - `gradio`: For creating an intuitive and interactive web interface.
  - `python-docx`: To save stories as Word documents.
  - `requests`: For making API calls and handling HTTP requests.
  - `scikit-learn`: For computing cosine similarity.

- **External APIs**:
  - Google Image Search: To find relevant images for the story content.
  - Groq API: To generate compelling story content using advanced AI models.

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/STORYCanvas.git
   cd STORYCanvas
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

The application will launch in your default web browser.

## Usage

1. **Enter a Prompt**: Provide a brief description or idea for your story.
2. **Select a Theme**: Choose a theme from the dropdown menu or leave it blank to use a randomly selected theme.
3. **Generate the Story**: Click the button to generate your story. The app will enhance it with relevant images.
4. **Download the Story**: Save the enhanced story as a Word document for offline use.

## Example Workflow

1. Input Prompt: "A brave explorer sets out on an adventure to find a hidden treasure."
2. Select Theme: "Adventure"
3. Output: A rich story with descriptive paragraphs and beautiful images.
4. Download: Save the story as a Word document with images embedded after each paragraph.

## File Structure

```
STORYCanvas/
|-- app.py               # Main application code
|-- requirements.txt     # Dependencies
|-- README.md            # Project documentation

```

## Future Enhancements

- Add multilingual support for story generation.
- Incorporate advanced customization options for themes and story length.
- Explore additional accessibility features for visually or hearing-impaired users.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the creators of `spaCy`, `sentence-transformers`, and `Gradio` for their powerful tools.
- Thanks to Google Image Search and Groq API for enabling seamless story enhancement.

