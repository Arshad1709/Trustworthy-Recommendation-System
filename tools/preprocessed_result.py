# Instantiate the TextDataset
# from torchtext.vocab import GloVe
from dataset_class import TextDataset
from utils import tokenize
ds = TextDataset()

# Prepare the input sentence
input_sentence = "Emojinate brings emojis to life by animating each emoji in text messages or social media posts. Users can select from a vast collection of animated emojis or even create their own personalized animations. Emojinate messages inject fun and expression into everyday conversations, making communication more engaging and entertaining for users worldwide. with the database of 30,000+ users"

# Preprocess the input sentence
tokenized_sentence = tokenize(input_sentence)  # Tokenize the sentence
sentence_ids = [ds.vocab[token] for token in tokenized_sentence]  # Convert tokens to IDs
padded_sequence = sentence_ids[:ds.max_doc_len] + [1] * max(0, ds.max_doc_len - len(sentence_ids))  # Pad sequence

# Print preprocessed results
print("Input Sentence:", input_sentence)
print("\nPreprocessed Results:")
print("-" * 50)
print(f"{'Tokenized Sentence:':<20}", tokenized_sentence)
print(f"{'Sentence IDs:':<20}", sentence_ids)
print(f"{'Padded Sequence:':<20}", padded_sequence)


