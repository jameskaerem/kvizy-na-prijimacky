from pathlib import Path
import json

# Shared row format for question batches (from batch UK 151 / LF MU 151 on):
# subject|chapter|source item|printed page|prompt|correct|distractor|distractor|distractor|explanation|memory aid
# The correct answer is rotated to position (id-1) % 4, as in the earlier batches.

def build(rows, start, counts, out, school, n=50):
    bank=[]
    for i,line in enumerate(rows.strip().splitlines(),start):
        parts=line.split('|')
        assert len(parts)==11,(i,line[:60])
        subject,chapter,number,page,prompt,correct,d1,d2,d3,explanation,memory=parts
        options=[correct,d1,d2,d3]
        answer=(i-1)%4
        options.insert(answer,options.pop(0))
        if school=='uk':
            item=number if subject=='Chemie' else ('úloha '+number if subject=='Fyzika' else 'otázka '+number)
            ref=f'UK · {subject} · {chapter} · {item}' + ('' if subject=='Chemie' else f' · str. {page}')
        else:
            ref=f'LF MU · {subject} · {chapter} {number} · str. {page}'
        bank.append(dict(id=i,subject=subject,category=subject+' · '+chapter,bookRef=ref,sourcePages=page,sourceItem=number,question=prompt,options=options,answer=answer,title=correct,paragraphs=[explanation],memory=memory))
    assert len(bank)==n and bank[-1]['id']==start+n-1
    assert [sum(q['subject']==s for q in bank) for s in ('Fyzika','Chemie','Biologie')]==counts,[sum(q['subject']==s for q in bank) for s in ('Fyzika','Chemie','Biologie')]
    for q in bank: assert len(set(q['options']))==4 and q['options'][q['answer']]==q['title']
    assert len({q['question'] for q in bank})==n
    Path(__file__).with_name(out).write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
