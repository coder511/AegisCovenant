#!/usr/bin/env python
# coding: utf-8

# In[11]:


import PyPDF2
import re


# In[12]:


with open("AWS_Lambda_Pricing.pdf", 'rb') as pdfFile:
    reader = PyPDF2.PdfReader(pdfFile)
    page1 = reader.pages[0]
    text = page1.extract_text()
    print(text)


# In[18]:


rex = re.compile("(?<=fees)(.*)", re.DOTALL)


# In[19]:


body=re.search(rex, text).group(0)


# In[20]:


body


# In[21]:


import json

# input string
input_str = '\nAWS Lambda Pricing\nId\nArchitecture\nDuration\nRequests\n0\nFirst 6 Billion GB-seconds / month\n$0.0000166667 for\nevery GB-second\n$0.20 per 1M\nrequests\n1\nNext 9 Billion GB-seconds / month\n$0.000015 for every\nGB-second\n$0.20 per 1M\nrequests\n2\nOver 15 Billion GB-seconds / month\n$0.0000133334 for\nevery GB-second\n$0.20 per 1M\nrequests\n3\nFirst 7.5 Billion GB-seconds / month\n$0.0000133334 for\nevery GB-second\n$0.20 per 1M\nrequests\n4\nNext 1 1.25 Billion GB-seconds / month\n$0.0000120001 for\nevery GB-second\n$0.20 per 1M\nrequests\n5\nOver 18.75 Billion GB-seconds / month\n$0.0000106667 for\nevery GB-second\n$0.20 per 1M\nrequests'

# regex pattern to extract the data
pattern = r'\n(\d+)\n(.*?)\n(.*?)\n(.*?)\n'

# extract data using regex and convert to JSON
output = []
for match in re.finditer(pattern, input_str):
    output.append({
        'id': match.group(1),
        'Architecture': match.group(2),
        'Duration': match.group(3),
        'Requests': match.group(4),
    })

result = {'output': output}

# convert to JSON string and pretty print
json_str = json.dumps(result, indent=2)
print(json_str)


# In[ ]:




