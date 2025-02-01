from groq import Groq
from youtube_transcript_api import YouTubeTranscriptApi 

video_link = input("Video linki: ")

if "?v=" in video_link:
    video_link = video_link.split("?v=")[1]

altyazi = YouTubeTranscriptApi.get_transcript(video_link, ["tr"])
altyazi_metni = ""

for x in altyazi:
    altyazi_metni += x["text"]

prompt = "Elimde bir youtube videosunun altyazıları var ve bunu sana vereceğim. Yapmanı istediğim şey bu altyazıları okuduktan sonra videonun özetini bana kısa ve açıklayıcı bir şekilde iletmen. İşte altyazılar: "

client = Groq(
    api_key= "API_KEY"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{prompt} {altyazi_metni}",
        }
    ],
    model="llama-3.3-70b-versatile",
    stream=False,
)

print(chat_completion.choices[0].message.content)