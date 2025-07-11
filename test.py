import google.generativeai as genai

# Paste your real cloud-created API key here
genai.configure(api_key="AIzaSyBACc9sWdzH6f4hSEWWxWEzOG96lef9QVc")

try:
    model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ correct name
    response = model.generate_content("What is the capital of France?")
    print(response.text)
except Exception as e:
    print("❌ API key is not working or setup is incomplete.")
    print("Error:", e)





