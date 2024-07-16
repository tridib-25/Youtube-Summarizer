# Step 1: Import the required libraries

from transformers import BertTokenizer, BertModel
import torch
import numpy as np

def bertScore_basic():
    print("bertScore_basic started")
# Step 2: Load the pre-trained BERT model and tokenizer

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")

    # Step 3: Define the two texts to compare

    # text1 = "Nikola Tesla was a Serbian-American inventor, electrical engineer, mechanical engineer, and futurist. He is best-known for his contributions to the design of the modern alternating current (AC) electricity supply system. Born and raised in the Austrian Empire, Tesla studied engineering and physics in the 1870s without receiving a degree, gaining practical experience in the early 1880s working in telephony and at Continental Edison in the new electric power industry. In 1884 he emigrated to the United States, where he became a naturalized citizen. He worked for a short time at the Edison Machine Works in New York City before he struck out on his own. With the help of partners to finance and market his ideas, Tesla set up laboratories and companies in New York to develop a range of electrical and mechanical devices. His AC induction motor and related polyphase AC patents, licensed by Westinghouse Electric in 1888, earned him a considerable amount of money and became the cornerstone of the polyphase system which that company eventually marketed. Attempting to develop inventions he could patent and market, Tesla conducted a range of experiments with mechanical oscillators/generators, electrical discharge tubes, and early X-ray imaging. He also built a wirelessly controlled boat, one of the first ever exhibited. Tesla became well known as an inventor and demonstrated his achievements to celebrities and wealthy patrons at his lab, and was noted for his showmanship at public lectures. Throughout the 1890s, Tesla pursued his ideas for wireless lighting and worldwide wireless electric power distribution in his high-voltage, high-frequency power experiments in New York and Colorado Springs. In 1893, he made pronouncements on the possibility of wireless communication with his devices. Tesla tried to put these ideas to practical use in his unfinished Wardenclyffe Tower project, an intercontinental wireless communication and power transmitter, but ran out of funding before he could complete it."

    # text2 = "Nikola Tesla was a Serbian-American inventor, electrical engineer, mechanical engineer, and futurist. He is best-known for his contributions to the design of the modern alternating current (AC) electricity supply system. In 1884 he emigrated to the United States, where he became a naturalized citizen. He worked for a short time at the Edison Machine Works in New York City before he struck out on his own. With the help of partners to finance and market his ideas, Tesla set up laboratories and companies in New York to develop a range of electrical and mechanical devices. Attempting to develop inventions he could patent and market, Tesla conducted a range of experiments with mechanical oscillators/generators, electrical discharge tubes, and early X-ray imaging. He also built a wirelessly controlled boat, one of the first ever exhibited. Tesla became well known as an inventor and demonstrated his achievements to celebrities and wealthy patrons at his lab, and was noted for his showmanship at public lectures. Throughout the 1890s, Tesla pursued his ideas for wireless lighting and worldwide wireless electric power distribution in his high-voltage, high-frequency power experiments in New York and Colorado Springs. In 1893, he made pronouncements on the possibility of wireless communication with his devices."

    text1 = open("./summary.txt","r",encoding="utf8").read()
    text2 = open("./transcript.txt","r",encoding="utf8").read()
    # Step 4: Prepare the texts for BERT

    inputs1 = tokenizer(text1, return_tensors="pt", padding=True, truncation=True)
    inputs2 = tokenizer(text2, return_tensors="pt", padding=True, truncation=True)

    # Step 5: Feed the texts to the BERT model

    outputs1 = model(**inputs1)
    outputs2 = model(**inputs2)

    # Step 6: Obtain the representation vectors

    embeddings1 = outputs1.last_hidden_state.mean(dim=1).detach().numpy()
    embeddings2 = outputs2.last_hidden_state.mean(dim=1).detach().numpy()

    # Step 7: Calculate cosine similarity

    similarity = np.dot(embeddings1, embeddings2.T) / (np.linalg.norm(embeddings1) * np.linalg.norm(embeddings2))

    # Step 8: Print the result

    print("bertScore_basic end")
    print("Similarity between the texts: {:.4f}".format(similarity[0][0]))
    return(round(similarity[0][0],2))

# bertScore_basic()

    ### Output: Similarity between the texts: 0.9000