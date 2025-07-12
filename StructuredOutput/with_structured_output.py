from langchain_groq import ChatGroq
from typing import TypedDict , Annotated , Optional , Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate , load_prompt

model = ChatGroq(
    model_name="llama3-70b-8192",
    api_key="GROQ_API_KEY",
    temperature=0.5)

class Review(TypedDict):
    key_themes: Annotated[list[str] , 'write downall the key themes discussed on the review']
    summary: Annotated[str , 'a brief summary of the text']
    sentiment: Annotated[Literal['pos' , 'neg'] , 'give a sentiment of the text either negative , neutral or positive']
    pros: Annotated[Optional[list[str]] , 'write down all the pros of the review']
    cons: Annotated[Optional[list[str]] , 'write down all the cons of the review']

structured_model  = model.with_structured_output(Review)

result = structured_model.invoke("""Product Review: AudioX Pro 750 Wireless Headphones
I've been using the AudioX Pro 750 for a few weeks now, and overall, I'm quite impressed.
Pros:
Great Sound Quality: Clear highs, solid mids, and deep bass. Music and calls sound excellent.
Strong Noise Cancelling: Effectively blocks out most background noise — ideal for travel or work.
Comfortable Fit: Soft ear cups and lightweight design make them easy to wear for long periods.
Long Battery Life: Around 35 hours with ANC on, and quick charging is a bonus.
Multipoint Connectivity: Easily switches between my phone and laptop without reconnecting.
 Cons:
Bulky Design: Not very portable; they don’t fold down compactly.
Touch Controls Can Be Oversensitive: Sometimes trigger actions unintentionally when adjusting.
Slight Audio Lag on Some Devices: A small delay when watching videos via Bluetooth on older hardware.
App Is Basic: Limited EQ options and no advanced features.
Verdict:
The AudioX Pro 750 is a strong choice for those wanting great sound and effective noise cancelling. While it’s
 a bit bulky and pricey, the performance makes it worth considering.
Rating: 4.3/5""")

print(result['sentiment'])