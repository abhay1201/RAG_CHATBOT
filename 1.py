import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCZElVwB4zgBuV0Fgh2CSb7V_NN-AXX4BI")

# Use the correct model name
model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # use "gemini-1.5-pro" or others as needed

# Generate a response
response = model.generate_content("hii this is Aji from pwc")

# Print the result
print(response.text)
