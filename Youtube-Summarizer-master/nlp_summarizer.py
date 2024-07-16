import spacy
import pytextrank

def nlp_spacy_summarizer():
      print("nlp_spacy entered")
      nlp = spacy.load("en_core_web_lg")
      nlp.add_pipe("textrank")


      # example_text = """Nikola Tesla was a Serbian-American inventor, electrical engineer, mechanical engineer, and futurist. He is best-known for his contributions to the design of the modern alternating current (AC) electricity supply system.
      # Born and raised in the Austrian Empire, Tesla studied engineering and physics in the 1870s without receiving a degree, gaining practical experience in the early 1880s working in telephony and at Continental Edison in the new electric power industry. In 1884 he emigrated to the United States, where he became a naturalized citizen. He worked for a short time at the Edison Machine Works in New York City before he struck out on his own. With the help of partners to finance and market his ideas, Tesla set up laboratories and companies in New York to develop a range of electrical and mechanical devices. His AC induction motor and related polyphase AC patents, licensed by Westinghouse Electric in 1888, earned him a considerable amount of money and became the cornerstone of the polyphase system which that company eventually marketed.
      # Attempting to develop inventions he could patent and market, Tesla conducted a range of experiments with mechanical oscillators/generators, electrical discharge tubes, and early X-ray imaging. He also built a wirelessly controlled boat, one of the first ever exhibited. Tesla became well known as an inventor and demonstrated his achievements to celebrities and wealthy patrons at his lab, and was noted for his showmanship at public lectures. Throughout the 1890s, Tesla pursued his ideas for wireless lighting and worldwide wireless electric power distribution in his high-voltage, high-frequency power experiments in New York and Colorado Springs. In 1893, he made pronouncements on the possibility of wireless communication with his devices. Tesla tried to put these ideas to practical use in his unfinished Wardenclyffe Tower project, an intercontinental wireless communication and power transmitter, but ran out of funding before he could complete it."""

      with open('transcript.txt',encoding="utf8") as f:
            example_text = f.read()

      doc = nlp(example_text)

      result=''
      for sent in doc._.textrank.summary(limit_phrases=20, limit_sentences=12):
            result+=sent.text
            # print(sent.text)

      print(result)
      print("nlp spacy done")
            
      return(result)
            
      # You can also take a look at the top 10 ranked phrases in the document:

      # phrases_and_ranks = [ 
      #     (phrase.chunks[0], phrase.rank) for phrase in doc._.phrases
      # ]
      # phrases_and_ranks[:10]
# nlp_spacy_summarizer()