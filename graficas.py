#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from PIL import Image

titanic_df=pd.read_csv('titanic.csv')
fig, axes=plt.subplots(2, 3, figsize=(16, 8))
plt.tight_layout(pad=3.0, w_pad=5.0, h_pad=4.0)#Mas espacio entre las graficas

#Primera grafica
class1_df=titanic_df[titanic_df['Pclass']==1]
class2_df=titanic_df[titanic_df['Pclass']==2]
class3_df=titanic_df[titanic_df['Pclass']==3]
indice_sup=[class1_df['Survived'].mean(),
         class2_df['Survived'].mean(),
         class3_df['Survived'].mean()]
clases=['1ra Clase','2da Clase','3ra Clase']
# Use the axes for plotting
axes[0,0].plot(clases, indice_sup, marker='o', 
               c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')
axes[0,0].set_ylabel('Indice de Supervivencia')
axes[0,0].set_xlabel('Clases')
axes[0,0].set_title('INDICE DE SUPERVIVENCIA POR CLASE')


#Segunda grafica 
#(No supe como arreglar que se vea asi de raro)
titanic_clean=titanic_df.dropna(subset=['Age'])
# Pass the axes into seaborn
axes[0,1].set_title('TARIFA PAGADA POR EDAD Y CLASE')
sns.scatterplot(x=titanic_clean['Fare'],y=titanic_clean['Age'],
                hue=titanic_clean['Pclass'],s=20,ax=axes[0,1]);
axes[0,1].set_ylabel('Edad')
axes[0,1].set_xlabel('Tarifa')
axes[0,1].legend(['1ra Clase', '2da Clase','3ra Clase']);

#Tercera grafica 
# Use the axes for plotting
axes[0,2].set_title('DISTRIBUCION DE EDADES POR CLASE')
axes[0,2].hist([class1_df['Age'].dropna(), 
                class2_df['Age'].dropna(), 
                class3_df['Age'].dropna()],
                bins=np.arange(0, 80, 5),
                stacked=True);
axes[0,2].legend(['1ra Clase', '2da Clase','3ra Clase']);
axes[0,2].set_xlabel('Edad')
axes[0,2].set_ylabel('Numero de personas')


#Cuarta grafica 
# Pass the axes into seaborn
axes[1,0].set_title('SUPERVIVENCIA POR SEXO Y CLASE')
sns.barplot(x='Pclass', y='Survived', hue='Sex',
            data=titanic_df, ax=axes[1,0]);
axes[1,0].set_xlabel('Clase')
axes[1,0].set_ylabel('Indice de Supervivencia')


#Quinta grafica
alone=titanic_df[titanic_df['SibSp']==0][titanic_df['Parch']==0]
notAlone=titanic_df[titanic_df['SibSp']!=0][titanic_df['Parch']!=0]
estados=['Solo', 'Acompanado']
axes[1,1].set_title('NUMERO DE VIAJANTES EN FAMILIA O SOLOS')
axes[1,1].bar(estados, [len(notAlone), len(alone)], 
              color=['blue', 'orange']);
axes[1,1].set_ylabel('Numero de Personas')


#Sexta grafica
# Plot an image using the axes
img = Image.open('titanic.jpg')
axes[1,2].set_title('IMAGEN DEL TITANIC')
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xticks([])
axes[1,2].set_yticks([])
plt.tight_layout(pad=2);
# %%