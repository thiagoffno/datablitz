
# coding: utf-8

# In[91]:


import numpy as np
import pandas as pd


# lendo arquivo do pgc

# In[92]:


GWAS = pd.read_csv ('/media/thiago/um_tera/arquivos/twins/scz.full.txt', delimiter="\t")


# conforme modelo do prs

# In[95]:


gwas = GWAS[['SNP', 'P', 'OR', 'A1', 'A2']]


# In[96]:


gwas.head()


# renomeando

# In[97]:


gwas.columns=['snpid', 'pval', 'or', 'a1', 'a2']


# In[ ]:


gwas.to_csv("gwas.vcf")

