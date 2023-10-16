import spacy
import random
from spacy.training import Example

# dados para treino
train_data = [
    ('por que a tutela de urgência é imprescindível?', [(10, 28, 'DIREITO')]),
    ('Quem é periculum in mora Chaka Khan?', [(7, 24, 'LATIM')]),
    ('O importante agravo de petição possui diversos artigos', [(13, 30, 'TIPO')]),
    ('o CPC/2015 é uma revolução para o meio jurídico', [(2, 10, 'LEI')]),    
    ('o CPC támbém é uma lei muito importante', [(2, 5, 'LEI')]),    
    ('o CDC é outra norma', [(2, 5, 'LEI')]), 
    ('a decisao da tutela de urgência é uma garantia judicial', [(13, 31, 'DIREITO')]),    
    ('o agravo de petição é outro tipo de processo', [(2, 19, 'TIPO')]),   
    ('o termo tutela de urgência significa que é importante', [(8, 26, 'DIREITO')]), 
    ('Quem é fumus boni iuris Chaka Khan?', [(7, 23, 'LATIM')]),     
    ('eu gosto de per saltum Londres e agravo de petição Berlim.', [(33, 50, 'TIPO')])
]
nlp = spacy.load("pt_core_news_lg")


optimizer = nlp.create_optimizer()
for itn in range(15):
    random.shuffle(train_data)
    for raw_text, entity_offsets in train_data:
        doc = nlp.make_doc(raw_text)
        example = Example.from_dict(doc, {"entities": entity_offsets})
        nlp.update([example], sgd=optimizer)
nlp.to_disk("/output")

# texto utilizado para teste
doc = nlp(u'tutela de urgência. agravo de petição com efeito suspensivo. comprovação de requisitos legais. não caracterização. a concessão de efeito suspensivo ao apelo envolve situação excepcional, tratando-se de medida cautelar, de modo que, cara a sua concessão, é mister o preenchimento, concomitante, dos requisitos previstos no artigo 300 do CPC, quais seja, a probabilidade do direito (fumus boni iuris) e o perigo do dano ou risco ao resultado útil do processo (periculum in mora), observadas as peculiaridades do caso concreto.')


from spacy import displacy
colors = {'DIREITO': '#85C1E9', 'LEI': '#f2ff61', 'LATIM': '#61ffc2', 'TIPO': 'pink'}
options = {'ents': ['DIREITO', 'LEI', 'LATIM', 'TIPO'], 'colors':colors}
displacy.serve(doc, style="ent", options=options)