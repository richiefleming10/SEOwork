import openai
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You:")
#         if user_input.lower() in ["quit,", "exit", "bye"]:
#             break
#         response = chat_with_gpt(user_input)
#         print("Chatbot:", response)
print(chat_with_gpt("Write a blog post on the best types of fish"))