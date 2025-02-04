import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

spanish_text = """El significado de la vida
                    El significado de la vida es un tema universal que ha intrigado a la humanidad desde tiempos inmemoriales. Es una pregunta compleja, profunda y personal, cuya respuesta puede variar enormemente dependiendo de las creencias, experiencias, y contextos culturales de cada individuo. En esencia, la búsqueda del significado es un viaje interno que impulsa a las personas a reflexionar sobre su existencia y propósito en el universo. Aunque no hay una respuesta única o definitiva, podemos explorar este tema desde distintas perspectivas que abarcan lo filosófico, espiritual, social y personal.
                    Desde un punto de vista filosófico, grandes pensadores han intentado descifrar el propósito de la vida. Según Aristóteles, la felicidad (o eudaimonía) es el objetivo supremo de la vida humana, alcanzada a través de la virtud y la ética. Por otro lado, el existencialismo de pensadores como Jean-Paul Sartre y Albert Camus plantea que la vida no tiene un significado inherente, sino que corresponde a cada individuo crear su propio propósito mediante sus elecciones y acciones. En esta óptica, el significado de la vida no es algo que se encuentra, sino algo que se construye.
                    En términos espirituales o religiosos, muchas tradiciones ofrecen marcos para comprender el sentido de la existencia. Para algunas religiones, como el cristianismo o el islam, la vida tiene un propósito divino: acercarse a Dios, cumplir con mandatos éticos y prepararse para una existencia eterna después de la muerte. En contraste, filosofías orientales como el budismo enseñan que el propósito radica en alcanzar la iluminación, liberar el sufrimiento interno y comprender la naturaleza de la realidad. Estos enfoques brindan consuelo para quienes buscan una conexión trascendental.
                    Sin embargo, el significado de la vida no tiene que estar limitado a lo abstracto. Desde una perspectiva social, muchos encuentran propósito en las relaciones humanas, la comunidad y el impacto que pueden tener en el mundo. Amar, cuidar de los demás, criar hijos, contribuir al bienestar colectivo o participar en causas que traspasen nuestros propios intereses inmediatos son formas de darle sentido a la vida. En el fondo, ser útil para otros y dejar un legado positivo puede ser una fuente poderosa de satisfacción y propósito.
                    A nivel personal, cada individuo tiene la libertad de definir qué le da sentido a su vida. Para algunos, puede ser perseguir una pasión o un sueño profesional. Otros encuentran propósito en la creatividad, el arte, explorar el mundo, o simplemente vivir con gratitud y presencia en el momento. La idea de que la felicidad no es un lugar de llegada, sino el camino mismo, invita a apreciar lo cotidiano.
                    En resumen, el significado de la vida es un mosaico de experiencias, creencias y reflexiones. Es un tema amplio que abarca lo universal y lo individual, lo tangible y lo trascendental. Aunque la vida puede parecer enigmática, el verdadero significado se encuentra al forjar un propósito que resuene profundamente contigo, en constante exploración y evolución."""

response = client.complete(
    messages=[
        UserMessage(content=f"Translate the text into english {spanish_text}"),
    ],
    model="DeepSeek-R1",
    temperature=1.3,
)
print(response.choices[0].message.content)
