def createSentences(subject,verb,obj):
    sentences = []
    for i in range(len(subject)):
        for j in range(len(verb)):
            for k in range(len(obj)):
                newSentence = subject[i] + ' ' + verb[j] + ' ' + obj[k] +'.'
                sentences.append(newSentence)
    return sentences
