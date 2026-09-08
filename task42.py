"""Take a sentence containing double space and unwanted sentences.clean """

sent=input()

sent2=sent.strip()
sent3=sent2.replace("  "," ")

print(sent3)