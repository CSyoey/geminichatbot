import google.generativeai as genai

# The SDK automatically finds the GOOGLE_API_KEY from your environment variables
model = genai.GenerativeModel('gemini-1.5-flash')

try:
    response = model.generate_content("Explain the concept of 'git' in a single, simple sentence.")
    print("🤖 Gemini:", response.text)
except Exception as e:
    print(f"An error occurred: {e}")