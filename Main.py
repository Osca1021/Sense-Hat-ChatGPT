import openai
openai.api_key_path = "API-Key.txt"

#sends a prompt to chatgpt
def get_answer(prompt):
	if (prompt_is_not_safe(prompt)):
		return
	return openai.Completion.create(model="text-davinci-002", prompt=prompt, max_tokens=10)

def prompt_is_not_safe(prompt):
	response = openai.Moderation.create(input=prompt)
	return response["results"][0]["flagged"]

userPrompt = input("> ")
answer = get_answer(userPrompt)
print(answer)
