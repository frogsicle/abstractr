""" The whole goal is to make papers more fun to read, but harder to understand =D
"""
__author__ = 'ali'

import random
import nltk

INTERESTING_TAGS = ['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNPS', 'NNS', 'RB', 'RBR', 'RBS', 'VB', 'VBD',
                            'VBG', 'VBN', 'VBP', 'VBZ']
class Paper():
    def __init__(self, text):
        self.text = text
        self.tokens = nltk.word_tokenize(text)
        self.tagged = nltk.pos_tag(self.tokens)
        self.tagged = [x for x in self.tagged if x[1] in INTERESTING_TAGS]

    def madlib(self, madtext):
        madtokens = nltk.word_tokenize(madtext)
        madtags = nltk.pos_tag(madtokens)
        madtags = [x for x in madtags if x[1] in INTERESTING_TAGS]
        max_replace = min(len(self.tagged) / 5, len(madtags))
        for i in range(max_replace):
            current_tag = madtags[i][1]
            matching_tags = [x for x in self.tagged if x[1]==current_tag]
            word_to_replace = random.choice(matching_tags)
            self.text = self.text.replace(word_to_replace[0], madtags[i][0])
#            print("replacing: " + word_to_replace[0] + " with: " + madtags[i][0])

    def __str__(self):
        return self.text


def test():
    thetext = """Abstract
BACKGROUND:
Gene duplication provides raw material for the evolution of functional innovation. We recently developed a phylogenetic method that classifies evolutionary processes driving the retention of duplicate genes by quantifying divergence between their spatial gene expression profiles and that of their single-copy orthologous gene in a closely related sister species.

RESULTS:
Here, we apply our classification method to pairs of duplicate genes in eight mammalian genomes, using data from 11 tissues to construct spatial gene expression profiles. We find that young mammalian duplicates are often functionally conserved, and that expression divergence rapidly increases over evolutionary time. Moreover, expression divergence results in increased tissue specificity, with an overrepresentation of expression in male kidney, underrepresentation of expression in female liver, and strong underrepresentation of expression in testis. Thus, duplicate genes acquire a diversity of new tissue-specific functions outside of the testis, possibly contributing to the origin of a multitude of complex phenotypes during mammalian evolution.

CONCLUSIONS:
Our findings reveal that mammalian duplicate genes are initially functionally conserved, and then undergo rapid functional divergence over evolutionary time, acquiring diverse tissue-specific biological roles. These observations are in stark contrast to the much faster expression divergence and acquisition of broad housekeeping roles we previously observed in Drosophila duplicate genes. Due to the smaller effective population sizes of mammals relative to Drosophila, these analyses implicate natural selection in the functional evolution of duplicate genes."""
    themadtext = """Scientists have discovered a winged dinosaur - an ancestor of the velociraptor - that they say was on the cusp of becoming a bird.
The 6ft 6in (2m) creature was almost perfectly preserved in limestone, thanks to a volcanic eruption that had buried it in north-east China.
And the 125-million year-old fossil suggests many other dinosaurs, including velociraptors, would have looked like "big, fluffy killer birds".
But it is unlikely that it could fly."""
    paper = Paper(thetext)
    paper.madlib(themadtext)
    print(paper)

if __name__ == "__main__":
    test()

# todo: get