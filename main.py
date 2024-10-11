from intentService import IntentService
from responseService import ResponseService
from dataService import DataService

pdf_path = "D:\\PythonProjectsPycharm\\Search_in_PDF_baseon_Redis\\1.pdf"

data_service = DataService()

#Drop all data from Redis if needed
data_service.drop_redis_data()

#Load data from pdf file to Redis
embeddings_data = data_service.pdf_to_embeddings(pdf_path)
data_service.load_data_to_redis(embeddings_data)

intent_service = IntentService()
response_service = ResponseService()

question = "What are the postcodes of the properties?"
#Get the intent of the user's question
intents = intent_service.get_intent(question)
#Get the facts from the file
facts = data_service.search_redis(intents)
#Get the answer
print(response_service.generate_response(facts, question))


