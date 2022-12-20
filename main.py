import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
from simplet5 import SimpleT5

#! Make the imports
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

############################################################
# Callback function called on update config
############################################################


def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
model = SimpleT5()
model.from_pretrained(model_type="t5", model_name="t5-base")
model.load_model("t5","./simplet5-epoch-9-train-loss-1.4592-val-loss-2.3113") # , use_gpu=True


def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    
    #! I am assuming that context is already coming into the function, and it is a part of a long blog.
    #! I am also assuming that the request.text is a list of questions based on the context.

    output = []
    # for text in request.text:

        #! Instantiate the model and tokenizer
        # tokenizer = AutoTokenizer.from_pretrained("ixa-ehu/SciBERT-SQuAD-QuAC")
        # model = AutoModelForQuestionAnswering.from_pretrained(
        #     "ixa-ehu/SciBERT-SQuAD-QuAC")


    # def predictions(text):
    # text = 'question:Can children be affected by Covid19?'
    print("THIS IS THE REQUST",request.text)
    predicted_ans = model.predict(request.text[0])
    #print(predicted_ans)
        # return predicted_ans


        # def predictions(context, question):
        #     nlp = pipeline('question-answering',
        #                    model=model, tokenizer=tokenizer)

        #     return nlp({'question': question, 'context': context})['answer']
            
    # response = predictions(text)

    #     output.append(response)
    #     #! And the output is a list of answers.

    return SimpleText(dict(text=predicted_ans))



if __name__== '__main__':
	text = input("Please input your question about covid-19: \n")
	print(execute(text, 'hello').text)

#? This code is defining a function named execute that takes in a request object, an ray object, and a context object, and returns a SimpleText object. The request object is expected to contain a list of questions, and the context object is a variable that contains the context for the questions.

#? The execute function first instantiates a tokenizer and model from the Hugging Face transformers library, and then defines a predictions function that takes in a context and a question, and uses the instantiated tokenizer and model to generate an answer to the question based on the given context.

#?Finally, the execute function loops through each of the questions in the request object, uses the predictions function to generate an answer for each question, and stores the answers in a list. The list of answers is then returned as a SimpleText object.
