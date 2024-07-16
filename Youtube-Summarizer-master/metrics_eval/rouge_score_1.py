import torch
import rouge
# from rouge import Rouge
# import statistics as np

def rouge_func():
    print("Rouge started")
    generated_summary = open("./summary.txt","r",encoding="utf8").read()
    reference_summary = open("./transcript.txt","r",encoding="utf8").read()
    # print(generated_summary)
    # metrics=['rouge-n', 'rouge-l', 'rouge-w']
    metrics=['rouge-n', 'rouge-l']
    # metrics=['rouge-1','rouge-2', 'rouge-l']
    # rouge2 = Rouge(metrics,max_n=2)
    rouge2 = rouge.rouge.Rouge(metrics,max_n=2)

    scores = rouge2.get_scores(generated_summary, reference_summary)

    # print(scores)
    total_f_score = 0.0
    cnt=0
    for metric, values in scores.items():
        f_value = values['f']
        print(f"{metric}: F = {f_value}")
        total_f_score += f_value
        cnt+=1

    avg= total_f_score/cnt
    print("\nTotal F Score:", total_f_score)
    print("\Avg F Score:", avg)
    # avg = np.mean([score["rouge-1"]["f"], score["rouge-2"]["f"], score["rouge-l"]["f"]])

    print("Rouge ended")
    return(round(avg,2))

# rouge_func()













# from rouge_score import rouge_scorer

# scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
# scores = scorer.score('Born and raised in the Austrian Empire, Tesla studied engineering and physics in the 1870s without receiving a degree, gaining practical experience in the early 1880s working in telephony and at Continental Edison in the new electric power industry. With the help of partners to finance and market his ideas, Tesla set up laboratories and companies in New York to develop a range of electrical and mechanical devices. Attempting to develop inventions he could patent and market, Tesla conducted a range of experiments with mechanical oscillators/generators, electrical discharge tubes, and early X-ray imaging. Throughout the 1890s, Tesla pursued his ideas for wireless lighting and worldwide wireless electric power distribution in his high-voltage, high-frequency power experiments in New York and Colorado Springs. Tesla tried to put these ideas to practical use in his unfinished Wardenclyffe Tower project, an intercontinental wireless communication and power transmitter, but ran out of funding before he could complete it.', 'Nikola Tesla was a Serbian-American inventor, electrical engineer, mechanical engineer, and futurist. He is best-known for his contributions to the design of the modern alternating current (AC) electricity supply system. Born and raised in the Austrian Empire, Tesla studied engineering and physics in the 1870s without receiving a degree, gaining practical experience in the early 1880s working in telephony and at Continental Edison in the new electric power industry. In 1884 he emigrated to the United States, where he became a naturalized citizen. He worked for a short time at the Edison Machine Works in New York City before he struck out on his own. With the help of partners to finance and market his ideas, Tesla set up laboratories and companies in New York to develop a range of electrical and mechanical devices. His AC induction motor and related polyphase AC patents, licensed by Westinghouse Electric in 1888, earned him a considerable amount of money and became the cornerstone of the polyphase system which that company eventually marketed. Attempting to develop inventions he could patent and market, Tesla conducted a range of experiments with mechanical oscillators/generators, electrical discharge tubes, and early X-ray imaging. He also built a wirelessly controlled boat, one of the first ever exhibited. Tesla became well known as an inventor and demonstrated his achievements to celebrities and wealthy patrons at his lab, and was noted for his showmanship at public lectures. Throughout the 1890s, Tesla pursued his ideas for wireless lighting and worldwide wireless electric power distribution in his high-voltage, high-frequency power experiments in New York and Colorado Springs. In 1893, he made pronouncements on the possibility of wireless communication with his devices. Tesla tried to put these ideas to practical use in his unfinished Wardenclyffe Tower project, an intercontinental wireless communication and power transmitter, but ran out of funding before he could complete it.')
# print(scores)