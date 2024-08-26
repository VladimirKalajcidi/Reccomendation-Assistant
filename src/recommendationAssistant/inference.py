from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers.string import StrOutputParser


class PredictionPipeline:
    def __init__(self, input):
        self.input=input
    
    def generate(self):

        llm = HuggingFaceEndpoint(
            repo_id="NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
            task="text-generation",
            max_tokens=-1,
            do_sample=False,
            repetition_penalty=1.03,
        )

        chat_model = ChatHuggingFace(llm=llm)

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "Дан диалог покупателя и продавца. Исходя из диалога, напиши несколько утоянющих вопросов, которые продавец мог бы задать покупателю"),
                ("human", "По данному диалогу напиши несколько утоянющих вопросов, которые продавец мог бы задать покупателю: {input}"),
            ]
        )

        chain = prompt | chat_model | StrOutputParser()
        output = chain.invoke({"input": self.input})

        return output