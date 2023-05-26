import openai
from sense_emu import SenseHat
from gtts import gTTS
openai.api_key_path = "API-Key.txt"

#sends a prompt to chatgpt
def get_answer(prompt):
	if (prompt_is_not_safe(prompt)):
		return
	messages=[
		{"role": "system", "content": "You are a helpful assistent. Answer as concisely as possible."},
		{"role": "user", "content": prompt}
	]
	return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=50)

def prompt_is_not_safe(prompt):
	response = openai.Moderation.create(input=prompt)
	return response["results"][0]["flagged"]

sense = SenseHat()

while True:

	userPrompt = input("> ")
	try:
		answer = get_answer(userPrompt)
	except:
		sense.show_message('Rate limit hit. wait a minute and try again')
	else:
		responseMessage = answer['choices'][0]['message']
		# print(answer)
		print(responseMessage['content'])

		# TTS
		tts = gTTS(responseMessage['content'], 'com', 'da')
		tts.save('test.mp3')

		# Sense hat
		sense.show_message(responseMessage['content'])