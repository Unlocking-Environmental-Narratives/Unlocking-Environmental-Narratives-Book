import os
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.stats.mstats import mquantiles
from sklearn.preprocessing import LabelBinarizer

def sample_posterior(y1, y2, mu0, sigma20, nu0, delta0, gamma20, tau20, S):
    """Draw samples from posterior distribution using Gibbs sampling 
    Parameters
    ----------
    `S` is the number of samples
    Returns
    -------
    chains : dict of array
        Dictionary has keys: 'mu', 'delta', and 'sigma2'.
    """
    print('.', end='', flush=True)
    n1, n2 = len(y1), len(y2)
    mu = (np.mean(y1) + np.mean(y2))/2
    delta = (np.mean(y1) - np.mean(y2))/2
    vars = ['mu', 'delta', 'sigma2']
    chains = {key: np.empty(S) for key in vars}
    for s in range(S):
        #print(s)
        a = (nu0+n1+n2)/2
        b = (nu0*sigma20 + np.sum((y1-mu-delta)**2) + np.sum((y2-mu+delta)**2))/2
        sigma2 = 1 / np.random.gamma(a, 1/b)
        mu_var = 1/(1/gamma20 + (n1+n2)/sigma2)
        mu_mean = mu_var * (mu0/gamma20 + np.sum(y1-delta)/sigma2 +
                            np.sum(y2+delta)/sigma2)
        mu = np.random.normal(mu_mean, np.sqrt(mu_var))
        delta_var = 1/(1/tau20 + (n1+n2)/sigma2)
        delta_mean = delta_var * (delta0/tau20 + np.sum(y1-mu)/sigma2 -
                                np.sum(y2-mu)/sigma2)
        delta = np.random.normal(delta_mean, np.sqrt(delta_var))
        chains['mu'][s] = mu
        chains['delta'][s] = delta
        chains['sigma2'][s] = sigma2
    return chains

def delta_confidence(rates_one_word):
    S = 1000
    mu0 = 3
    tau20 = 1.5**2
    nu0 = 1
    sigma20 = 1
    delta0 = 0
    gamma20 = 1.5**2
    female_rates = rates_one_word[0:3]
    male_rates = rates_one_word[3:6]
    chains = sample_posterior(female_rates, male_rates, mu0, sigma20, nu0,
                              delta0, gamma20, tau20, S)
    delta = chains['delta']
    return np.max([np.mean(delta < 0), np.mean(delta > 0)])

raw_texts = []
female_indices = []
male_indices = []
idx = 0
with open('cd_gender.txt', 'r') as f:
    lines = f.readlines()
    for article in lines:
        elems = article.split("\t")
        #print(elems)
        if elems[1] == 'female':
            female_indices.append(idx)
        if elems[1] == 'male':
            male_indices.append(idx)
        raw_texts.append(elems[2])
        idx = idx + 1

vectorizer = CountVectorizer(input='content')
dtm = vectorizer.fit_transform(raw_texts)
vocab = np.array(vectorizer.get_feature_names())
dtm = dtm.toarray()
rates = 1000 * dtm / np.sum(dtm, axis=1, keepdims=True)

female_rates = rates[female_indices, :]
male_rates = rates[male_indices, :]

female_rates_avg = np.mean(female_rates, axis=0)
male_rates_avg = np.mean(male_rates, axis=0)

distinctive_indices = (female_rates_avg * male_rates_avg) == 0

ranking = np.argsort(female_rates_avg[distinctive_indices] + male_rates_avg[distinctive_indices])[::-1]

dtm = dtm[:, np.invert(distinctive_indices)]
rates = rates[:, np.invert(distinctive_indices)]
vocab = vocab[np.invert(distinctive_indices)]

female_rates = rates[female_indices, :]
male_rates = rates[male_indices, :]
female_rates_avg = np.mean(female_rates, axis=0)
male_rates_avg = np.mean(male_rates, axis=0)
rates_avg = np.mean(rates, axis=0)

keyness = np.apply_along_axis(delta_confidence, axis=0, arr=rates)
ranking = np.argsort(keyness)[::-1]

print(" ")
print(vocab[ranking][0:10])

print("female rates avg")
print(female_rates_avg[ranking][0:10])
print("male rates avg")
print(male_rates_avg[ranking][0:10])

