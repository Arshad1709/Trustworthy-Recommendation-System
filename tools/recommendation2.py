import torch
# from torchtext.vocab import GloVe
from dataset_class import TextDataset
from utils import tokenize
from MTFM import MTFM, MTFMConfig
import numpy as np

def recommendation(input_text,n):

# Get vocabulary and embeddings
  ds = TextDataset()
  vocab = ds.vocab
  embeddings = ds.embed

  # Step 1: Load the Saved Model
  model_path = 'checkpoint/MTFM_0.5.h'
  config = MTFMConfig(ds)  # Instantiate MTFMConfig
  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  model = MTFM(config)  # Initialize MTFM model with config
  model.load_state_dict(torch.load(model_path))
  model.eval()
  model.to(device)

  # Step 2: Preprocess the Input Data
  # input_text = "Vizlingo is a new platform that animates each word of a text messages or social media posts with a user-generated video clip. Vizlingo messages are shared across social networks and on mobile devices, merging two prolific trends: social messaging and video sharing. Users can submit their own clips, see vat clips their friends use, and select favorites from an ever-growing database of more than 30,000 clips from over 40 countries."
  # input_text = "SnapSpeak revolutionizes communication by adding interactive filters to each spoken word in audio messages. Users can personalize their messages with a wide array of filters, from funny animations to informative overlays. SnapSpeak merges the convenience of voice messaging with the creativity of visual expression, creating engaging content for social media and beyond."
  # input_text="FinTechFacet transforms financial interactions by integrating customizable data overlays into each transactional communication. Users can personalize their financial messages with a vast selection of dynamic overlays, from real-time market trends to personalized budget insights. FinTechFacet merges the efficiency of financial messaging with the creativity of visual data representation, generating compelling content for investors, analysts, and financial institutions alike. This innovative platform not only enhances the clarity and depth of financial communication but also revolutionizes how financial data is shared and understood, fostering more informed decision-making processes in the financial sector and beyond"
  tokenized_sentence = tokenize(input_text)  # Tokenize the sentence
  sentence_ids = [ds.vocab[token] for token in tokenized_sentence]  # Convert tokens to IDs
  padded_sequence = sentence_ids[:ds.max_doc_len] + [1] * max(0, ds.max_doc_len - len(sentence_ids))  # Pad sequence
  # Tokenize the input text

  # print("step 3")
  # Step 3: Use the Model for Prediction
  with torch.no_grad():
      input_tensor = torch.tensor(padded_sequence, dtype=torch.long, device=device).unsqueeze(0)  # Add batch dimension

      api_pred, category_pred = model(input_tensor)

  # Convert the predictions into interpretable results
  api_pred = api_pred.cpu().numpy()
  category_pred = category_pred.cpu().numpy()

  # Example interpretation of predictions
  # Get the indices of the top 5 API predictions
  top_api_indices = np.argsort(api_pred.squeeze())[-n:][::-1]

  # Get the indices of the top 5 category predictions
  top_category_indices = np.argsort(category_pred.squeeze())[-n:][::-1]

  # Get the corresponding APIs and categories using the indices
  top_5_predicted_apis = [ds.mashup_ds.used_api_mlb.classes_[idx] for idx in top_api_indices]
  top_5_predicted_categories = [ds.mashup_ds.category_mlb.classes_[idx] for idx in top_category_indices]
  return top_5_predicted_apis,top_5_predicted_categories
  # Print or display the top 5 recommendations
  # print("Top 5 Recommended APIs with Categories:")
  # for i in range(len(top_5_predicted_apis)):
  #     print(f"API: {top_5_predicted_apis[i]}, Category: {top_5_predicted_categories[i]}")
