import openai
from dotenv import load_dotenv
import os
import openai
from dotenv import load_dotenv
import os
# Tải các biến môi trường từ file .env
load_dotenv()
# Tải các biến môi trường từ file .env
load_dotenv()
# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")

# Hàm gọi API OpenAI GPT-4
def get_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4",  # Bạn có thể thay bằng các engine khác như "text-davinci-003"
        prompt=prompt,
        max_tokens=150
    )if __name__ == "__main__":if __name__ == "__main__":
    return response.choices[0].text.strip()

# Kiểm tra đầu ra
if __name__ == "__main__":
    user_input = "What is the capital of France?"
    print(get_response(user_input))
  print(get_response(user_input))
  print(get_response(user_input))
  print(get_response(user_input))
  print(get_response(user_input))# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")
  print(get_response(user_input))
  print(get_response(user_input))
  print(get_response(user_input))
# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")
# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")
# Tải các biến môi trường từ file .env
# Tải các biến môi trường từ file .env
# Tải các biến môi trường từ file .env
# Tải các biến môi trường từ file .env
