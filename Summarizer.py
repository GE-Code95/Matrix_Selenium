from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA
import json
import os

sample = {"Header": "German Covid protests turn nasty in row over rules and vaccinations",
          "URL": "https://www.bbc.com/news/world-europe-60059543",
          "Content": "Petra K\u00f6pping was at home when she realised that around 30 people wielding flaming torches had gathered outside her house.\nThe regional politician is responsible for public health in the eastern state of Saxony, and the shouting protesters on her doorstep were apparently furious about measures to tackle the coronavirus pandemic.\nThe protest last month, widely condemned by politicians and the public alike, was not a one-off. Every week tens of thousands of Germans take to the streets to demonstrate against restrictions and vaccination.\nMany protests are peaceful, but others explode into violence and experts are increasingly worried by the aggressive language and threats aimed at politicians and public figures online.\nTwo security officers stood guard as I interviewed Petra K\u00f6pping about her experience.\nSome of the hatred towards her, she says, is stirred up and exploited by the far right.\n\"We have to make a clear distinction between organisers who engage in right-wing extremist ideology and want to change society - they don't care about vaccination policy - and the people who come along because they're opposed to vaccination.\"\nPeople such as Bj\u00f6rn who I met at a recent demonstration in Berlin. He'd brought along his young son and, as he held his hand in the crowd, Bj\u00f6rn explained he wasn't vaccinated himself because he thought the jab had been developed too quickly.\n\"The discrepancy between what we know and what the media tell us makes me suspicious.\"\nCovid has divided Germany. The unvaccinated are banned from restaurants, non-essential shops, leisure and arts facilities. And politicians are considering compulsory vaccination.\nBj\u00f6rn was among several thousand people who marched through the brightly lit streets of the capital.\nAt the same time, in towns and cities across Germany, around 70,000 people took part in small, simultaneous demonstrations, some of which ended in scuffles and arrests.\nMany take place on Monday nights. By advertising them as Spazierg\u00e4nge, or strolls, organisers not only seek to bypass Covid laws, which might prevent a mass gathering, but also to invoke nostalgically the symbolism of the Monday night strolls that were used by pro-democracy protesters opposed to the communist regime of the old East Germany.\nThe crowd in Berlin shouted Freiheit - freedom - as loudspeakers blasted out antivax songs, misinformation and conspiracy: \"You'd be surprised by what our politicians and public broadcasters keep secret from you - and why!\"\nSome German politicians have acknowledged that they'll never persuade many of these people of the benefits and safety of the vaccine, let alone convince otherwise those who don't believe Covid exists.\nBut authorities are worried by the spread of conspiracy theories and the threat of radicalisation. The number of recorded politically motivated crimes rose to its highest level in a decade last year.\n\"The big shift we've seen during the pandemic is that the more inherently violent ideas of overthrowing democracy which we've seen from the beginning turn more into concrete ideas,\" said Miro Dittrich, who researches right-wing extremism at the Centre for Monitoring, Analysis and Strategy.\nHe spends his days undercover online, monitoring networks like the messaging app Telegram.\n\"So it's not just 'we'll do a big demonstration in Berlin', it's 'what are the private addresses of these people who we think are responsible for this and we have to visit their homes'.\"\nHe pointed to an example from Telegram: a picture of the German health minister with text suggesting people storm his flat and \"inject him with his own stuff\".\nWhile he believes it would be wrong to assume that all those who express such ideas online represent a physical danger, \"we've seen its crucial for people who actually do offline violence to feel that they have a community that agrees with them\".\nMost Germans dismiss the conspiracy theories and the protesters who are, after all, very much in the minority. But the voice of discontent is loud. It's disruptive and it's persistent."}


def summarizer(path):
    summarize = pipeline('summarization')
    '''for file in path:
        with open(f'{path}/{file}', 'r') as dict_file:
            content = json.loads(dict_file.read())[0]
            print(summarize(content, max_length=100, min_length=30, do_sample=False))
'''
    for file in os.listdir(path):
        if file.endswith(".json"):
            content = json.loads(file)["Content"]
            print(summarize(content, max_length=100, min_length=30, do_sample=False))


def sentiment_analyzer(file):
    sia = SIA()
    for sentence in file:
        ss = sia.polarity_scores(sentence)
    return ss


if __name__ == '__main__':
    summarizer(sample)
    some_file = 'x'
    sentiment_analyzer(some_file)
