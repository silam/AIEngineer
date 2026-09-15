from rag import rag_pipeline
from rag import llm, embeddings
from ragas import SingleTurnSample, EvaluationDataset, evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingWrapper
from ragas.metrics import ExactMatchMetric, LLMContextPrecisionwithReference, F1ScoreMetric, \
                        LLMContextRecallwithReference, Faithfulness, ResponseRelevanceMetric, \
                        LLMContextF1ScorewithReference, ConsistencyMetric, RobustnessMetric, \
                        Factualcorrectness, ResponseRelevancy, RobustnessMetric


evalquestions = [
    {
        "question": "How many casual leaves am I entitled to in a year?",
        "reference": "An employee can take 12 casual leaves in a year."
    },
    {
        "question" :"What is the notice period for resignation?",
        "reference": "The notice period for resignation is typically 60 days for confirmed employees."
    }
]

samples = []

for item in evalquestions:
    result = rag_pipeline({"question": item["question"]})

    #split the joined string back into a list of chunks if needed
    contexts = result["context"].split("\n\n") if "context" in result else []

    sample = SingleTurnSample(
        user_input=item["question"],
        retrieved_contexts=contexts,
        response=result["answer"] if "answer" in result else None,
        
        reference=item["reference"])

    
    samples.append(sample)
dataset = EvaluationDataset(samples=samples)