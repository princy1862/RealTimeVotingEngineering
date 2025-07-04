
import google.generativeai as genai

# ✅ Paste your valid Gemini API key here
genai.configure(api_key="AIzaSyAhV4kPX6_cHvqwFiqCtTsd_gf8MCpRjAY")

# ✅ Use correct model name (v1-compatible)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Your prompt
prompt = "Write an email to my boss for resignation."

# ✅ Generate the content
response = model.generate_content(prompt)

# ✅ Show result
print(response.text)



