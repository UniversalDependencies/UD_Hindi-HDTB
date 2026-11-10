#!/usr/bin/env python3
"""
Fix 'too-many-subjects' errors in UD_Hindi-HDTB.

Each entry in FIXES maps sent_id -> list of operations:
  ('deprel', ord, new_deprel)          – change deprel of node with that ord
  ('parent', ord, new_parent_ord)      – reparent node to node with new_parent_ord
"""

import os
import udapi

FIXES = {
    # ── TRAIN ────────────────────────────────────────────────────────────────
    # आपको महसूस होगा: आपको(dative experiencer)→iobj; embedded clause→ccomp
    'train-s157':  [('deprel', 7, 'iobj'), ('deprel', 18, 'ccomp')],

    # यह कोई नई बात नहीं है: कोई→det (यह stays nsubj)
    'train-s187':  [('deprel', 46, 'det')],

    # सेक्स वर्किंग को…प्राप्त: वर्किंग(ko-dative)→iobj
    'train-s260':  [('deprel', 3, 'iobj')],

    # X को Y मिलना type constructions (experiencer→iobj):
    'train-s274':  [('deprel', 5, 'iobj')],

    # X को अभिभूत करना: आपको(accusative)→obj
    'train-s325':  [('deprel', 5, 'obj')],

    'train-s459':  [('deprel', 4, 'iobj')],
    'train-s711':  [('deprel', 20, 'iobj')],

    # X को Y मिलना + compound noun verb:
    'train-s804':  [('deprel', 22, 'iobj'), ('deprel', 24, 'compound')],

    # यह कोई X नहीं है: कोई→det (यह stays nsubj)
    'train-s831':  [('deprel', 2, 'det')],

    'train-s970':  [('deprel', 5, 'iobj')],
    'train-s991':  [('deprel', 15, 'iobj')],
    'train-s992':  [('deprel', 30, 'iobj')],

    # X को Y मिलना + compound:
    'train-s1124': [('deprel', 23, 'iobj'), ('deprel', 25, 'compound')],

    'train-s1142': [('deprel', 7, 'iobj')],

    'train-s1143': [('deprel', 2, 'iobj')],

    'train-s1154': [('deprel', 7, 'iobj')],
    'train-s1160': [('deprel', 14, 'iobj')],
    'train-s1180': [('deprel', 22, 'iobj')],
    'train-s1414': [('deprel', 23, 'iobj')],
    'train-s1424': [('deprel', 26, 'iobj')],
    'train-s1436': [('deprel', 9, 'iobj')],
    'train-s1471': [('deprel', 10, 'iobj')],
    'train-s1587': [('deprel', 7, 'iobj')],
    'train-s1745': [('deprel', 4, 'iobj')],
    'train-s1771': [('deprel', 11, 'iobj')],

    # X को iobj + ki-clause→ccomp:
    'train-s1834': [('deprel', 2, 'iobj'), ('deprel', 15, 'ccomp')],

    'train-s1861': [('deprel', 4, 'iobj')],
    'train-s1872': [('deprel', 5, 'iobj')],
    'train-s1917': [('deprel', 7, 'iobj')],

    # X को iobj + embedded clause→ccomp:
    'train-s1920': [('deprel', 4, 'iobj'), ('deprel', 22, 'ccomp')],

    'train-s2028': [('deprel', 23, 'iobj')],
    'train-s2071': [('deprel', 18, 'iobj')],
    'train-s2080': [('deprel', 7, 'iobj')],
    'train-s2169': [('deprel', 5, 'iobj')],
    'train-s2189': [('deprel', 12, 'iobj')],
    'train-s2334': [('deprel', 21, 'iobj')],
    'train-s2352': [('deprel', 3, 'iobj')],
    'train-s2453': [('deprel', 7, 'iobj')],
    'train-s2697': [('deprel', 37, 'iobj')],
    'train-s2705': [('deprel', 7, 'iobj')],
    'train-s2776': [('deprel', 8, 'iobj')],

    # नेटवर्क wrongly attached as nsubj of मिलने; reparent to उपक्रम as nmod:
    'train-s2800': [('parent', 5, 14), ('deprel', 5, 'nmod')],

    'train-s2803': [('deprel', 2, 'iobj')],
    'train-s2804': [('deprel', 3, 'iobj')],
    'train-s2871': [('deprel', 9, 'iobj')],
    'train-s2885': [('deprel', 15, 'iobj')],

    # खुद को is reflexive obj:
    'train-s2985': [('deprel', 6, 'obj')],

    'train-s3016': [('deprel', 3, 'iobj')],
    'train-s3030': [('deprel', 2, 'iobj')],
    'train-s3268': [('deprel', 34, 'iobj')],

    # जो सबके लिए वैध हो: सबके is obl (for everyone), not subject:
    'train-s3301': [('deprel', 20, 'obl')],

    'train-s3596': [('deprel', 15, 'iobj')],
    'train-s3921': [('deprel', 20, 'iobj')],

    # X को Y मिलना (experiencer→iobj):
    'train-s3991': [('deprel', 1, 'iobj'), ('deprel', 15, 'ccomp')],
    'train-s4017': [('deprel', 5, 'iobj')],

    # X को कोई Y नहीं है: experiencer→iobj, कोई→det:
    'train-s4084': [('deprel', 29, 'iobj'), ('deprel', 30, 'det')],

    'train-s4108': [('deprel', 4, 'iobj')],
    'train-s4109': [('deprel', 1, 'iobj')],

    # X को कोई Y नहीं है:
    'train-s4123': [('deprel', 38, 'iobj'), ('deprel', 39, 'det')],

    'train-s4138': [('deprel', 1, 'iobj')],

    # महिलाओं को मौका मिला: महिलाओं(dative)→iobj, मौका stays nsubj:
    'train-s4179': [('deprel', 5, 'iobj')],

    'train-s4309': [('deprel', 20, 'iobj')],

    # X को कोई Y नहीं है:
    'train-s4318': [('deprel', 20, 'iobj'), ('deprel', 21, 'det')],

    # X को iobj + ki-clause→ccomp:
    'train-s4345': [('deprel', 1, 'iobj'), ('deprel', 13, 'ccomp')],

    'train-s4384': [('deprel', 1, 'iobj')],
    'train-s4388': [('deprel', 1, 'iobj')],
    'train-s4393': [('deprel', 17, 'iobj')],

    # सुरक्षाबलों को कामयाबियाँ मिली: सुरक्षाबलों(dative)→iobj:
    'train-s4400': [('deprel', 3, 'iobj')],

    # X को ki-clause→ccomp:
    'train-s4413': [('deprel', 26, 'iobj'), ('deprel', 34, 'ccomp')],

    # X को कोई Y नहीं: experiencer→iobj, कोई→det:
    'train-s4491': [('deprel', 11, 'iobj'), ('deprel', 12, 'det')],

    'train-s4537': [('deprel', 7, 'iobj')],
    'train-s4598': [('deprel', 6, 'iobj')],
    'train-s4606': [('deprel', 23, 'iobj')],
    'train-s4616': [('deprel', 9, 'iobj')],

    # हर किसी को लुभाना: किसी(accusative)→obj:
    'train-s4748': [('deprel', 12, 'obj')],

    'train-s4839': [('deprel', 7, 'iobj')],
    'train-s4895': [('deprel', 18, 'iobj')],
    'train-s5087': [('deprel', 1, 'iobj')],

    # लोगों को आकर्षित करना: लोगों(accusative)→obj:
    'train-s5152': [('deprel', 17, 'obj')],

    'train-s5423': [('deprel', 18, 'iobj')],

    # X को iobj + ki-clause→ccomp:
    'train-s5520': [('deprel', 16, 'iobj'), ('deprel', 24, 'ccomp')],

    'train-s5539': [('deprel', 1, 'iobj')],

    # X कोई Y नहीं है: कोई→det:
    'train-s5552': [('deprel', 5, 'det')],

    # X को मौका मिलना: X(dative)→iobj:
    'train-s5558': [('deprel', 3, 'iobj')],

    'train-s5577': [('deprel', 20, 'iobj')],
    'train-s5684': [('deprel', 18, 'iobj')],
    'train-s5697': [('deprel', 18, 'iobj')],
    'train-s5723': [('deprel', 12, 'iobj')],

    # X को झटका लगना: X(dative)→iobj:
    'train-s5907': [('deprel', 6, 'iobj')],

    'train-s5931': [('deprel', 43, 'iobj')],
    'train-s5955': [('deprel', 10, 'iobj')],
    'train-s5956': [('deprel', 1, 'iobj')],
    'train-s5959': [('deprel', 2, 'iobj')],
    'train-s5964': [('deprel', 2, 'iobj')],
    'train-s6119': [('deprel', 4, 'iobj')],
    'train-s6530': [('deprel', 1, 'iobj')],
    'train-s6682': [('deprel', 35, 'iobj')],
    'train-s6690': [('deprel', 14, 'iobj')],

    # X ने Y को तिलमिलाना: Y(accusative)→obj:
    'train-s7032': [('deprel', 13, 'obj')],

    'train-s7051': [('deprel', 10, 'iobj')],
    'train-s7059': [('deprel', 18, 'iobj')],
    'train-s7187': [('deprel', 13, 'iobj')],
    'train-s7422': [('deprel', 34, 'iobj')],
    'train-s7471': [('deprel', 11, 'iobj')],
    'train-s7547': [('deprel', 7, 'iobj')],
    'train-s7557': [('deprel', 17, 'iobj')],

    # X को चोट लगना: X(dative)→iobj:
    'train-s8081': [('deprel', 9, 'iobj')],

    'train-s8268': [('deprel', 13, 'iobj')],
    'train-s8346': [('deprel', 5, 'iobj')],
    'train-s8356': [('deprel', 25, 'iobj')],
    'train-s8368': [('deprel', 3, 'iobj')],
    'train-s8617': [('deprel', 11, 'iobj')],

    # उन्हें कोई ऐतराज नहीं होगा: उन्हें→iobj, कोई(det of ऐतराज)→det:
    'train-s8780': [('deprel', 34, 'iobj'), ('deprel', 35, 'det')],

    # उन्हें यह बात परेशान करना: उन्हें(accusative)→obj:
    'train-s8791': [('deprel', 22, 'obj')],

    'train-s8833': [('deprel', 18, 'iobj')],
    'train-s8868': [('deprel', 32, 'iobj')],
    'train-s8904': [('deprel', 5, 'iobj')],
    'train-s9331': [('deprel', 13, 'iobj')],
    'train-s9429': [('deprel', 1, 'iobj')],

    # उन्हें कोई आपत्ति नहीं है: उन्हें→iobj, कोई(det of आपत्ति)→det:
    'train-s9656': [('deprel', 16, 'iobj'), ('deprel', 17, 'det')],

    'train-s9775': [('deprel', 11, 'iobj')],

    # X को Y पहुंचाना pattern:
    'train-s10183': [('deprel', 47, 'iobj'), ('deprel', 48, 'obj')],

    'train-s10218': [('deprel', 34, 'iobj')],
    'train-s10305': [('deprel', 2, 'iobj')],
    'train-s10370': [('deprel', 29, 'iobj')],
    'train-s10372': [('deprel', 23, 'iobj')],
    'train-s10537': [('deprel', 6, 'iobj')],

    # X को दिल का दौरा पड़ना: X(dative)→iobj:
    'train-s10560': [('deprel', 13, 'iobj')],

    # X को सफलता मिलना: X(dative)→iobj:
    'train-s10602': [('deprel', 28, 'iobj')],

    'train-s10616': [('deprel', 2, 'iobj')],
    'train-s10682': [('deprel', 15, 'iobj')],
    'train-s10686': [('deprel', 6, 'iobj')],
    'train-s10693': [('deprel', 10, 'iobj')],

    # X को खतरा पैदा होना: X(dative)→iobj:
    'train-s10910': [('deprel', 15, 'iobj')],

    'train-s11000': [('deprel', 4, 'iobj')],

    # X कोई नई बात नहीं है: कोई→det:
    'train-s11305': [('deprel', 11, 'det')],

    'train-s11346': [('deprel', 9, 'iobj')],

    # X को बढ़ावा मिलना: X(dative)→iobj:
    'train-s11510': [('deprel', 14, 'iobj')],

    'train-s11535': [('deprel', 3, 'iobj')],
    'train-s11608': [('deprel', 15, 'iobj')],
    'train-s11611': [('deprel', 2, 'iobj')],
    'train-s11907': [('deprel', 31, 'iobj')],
    'train-s12038': [('deprel', 14, 'iobj')],

    # किसानों ने उन्हें भरोसा दिलाया: उन्हें(dative)→iobj:
    'train-s12109': [('deprel', 6, 'iobj')],

    'train-s12211': [('deprel', 8, 'iobj')],
    'train-s12249': [('deprel', 3, 'iobj')],

    # X को गति मिलना: X(dative)→iobj:
    'train-s12264': [('deprel', 14, 'iobj')],

    # X को कोई Y नहीं है: experiencer→iobj, कोई→det:
    'train-s12276': [('deprel', 11, 'iobj'), ('deprel', 12, 'det')],

    'train-s12291': [('deprel', 4, 'iobj')],
    'train-s12313': [('deprel', 9, 'iobj')],
    'train-s12328': [('deprel', 23, 'iobj')],
    'train-s12334': [('deprel', 1, 'iobj')],

    # खंडपीठ ने तीनों को आदेश दिए: तीनों(dative recipient)→iobj:
    'train-s12455': [('deprel', 7, 'iobj')],

    # जवानों द्वारा X के साथ: इराकियों के साथ is comitative obl:
    'train-s12526': [('deprel', 8, 'obl')],

    'train-s12555': [('deprel', 3, 'iobj')],

    # X को iobj + ki-clause→ccomp:
    'train-s12556': [('deprel', 1, 'iobj'), ('deprel', 17, 'ccomp')],

    'train-s12650': [('deprel', 30, 'iobj')],

    # Two separate X को Y मिलना clauses in one sentence:
    'train-s12653': [('deprel', 18, 'iobj'), ('deprel', 30, 'iobj')],

    'train-s12894': [('deprel', 23, 'iobj')],

    # लोगों को निराश होना स्वाभाविक है: reparent लोगों को under होना:
    'train-s12896': [('parent', 3, 10), ('deprel', 3, 'iobj')],

    'train-s13072': [('deprel', 5, 'iobj')],
    'train-s13223': [('deprel', 5, 'iobj')],

    # ── DEV ──────────────────────────────────────────────────────────────────
    # X कोई Y नहीं है: कोई→det:
    'dev-s238':  [('deprel', 15, 'det')],

    # X को कोई Y नहीं है: experiencer→iobj, कोई→det:
    'dev-s600':  [('deprel', 18, 'iobj'), ('deprel', 19, 'det')],

    'dev-s790':  [('deprel', 2, 'iobj')],

    # X (चिंता) Y को सताना: Y(accusative)→obj:
    'dev-s922':  [('deprel', 6, 'obj')],

    # गोस्वामी कैंप ने महंत को दरकिनार किया: महंत(accusative)→obj:
    'dev-s1098': [('deprel', 4, 'obj')],

    'dev-s1101': [('deprel', 9, 'iobj')],
    'dev-s1133': [('deprel', 17, 'iobj')],
    'dev-s1180': [('deprel', 11, 'iobj')],
    'dev-s1181': [('deprel', 4, 'iobj')],
    'dev-s1219': [('deprel', 13, 'iobj')],
    'dev-s1332': [('deprel', 4, 'iobj')],

    # X को Y compound verb: X(dative)→iobj:
    'dev-s1341': [('deprel', 7, 'iobj'), ('deprel', 14, 'compound')],

    # हमें नहीं लगता कि विहिप को कोई आपत्ति है:
    # हमें→iobj, embedded है→ccomp, विहिप को→iobj:
    'dev-s1518': [('deprel', 5, 'iobj'), ('deprel', 17, 'iobj'), ('deprel', 21, 'ccomp')],

    # X को आशा हुई + ki-clause→ccomp:
    'dev-s1550': [('deprel', 21, 'iobj'), ('deprel', 41, 'ccomp')],

    'dev-s1635': [('deprel', 2, 'iobj')],

    # ── TEST ─────────────────────────────────────────────────────────────────
    'test-s122':  [('deprel', 11, 'iobj')],
    'test-s215':  [('deprel', 8, 'iobj')],

    # X को Y compound: X(dative)→iobj:
    'test-s371':  [('deprel', 21, 'iobj'), ('deprel', 24, 'compound')],

    'test-s402':  [('deprel', 5, 'iobj')],

    # X ने Y को पीटा: Y(accusative)→obj:
    'test-s435':  [('deprel', 8, 'obj')],

    # जो सबके लिए: सबके is obl not subject:
    'test-s457':  [('deprel', 20, 'obl')],

    'test-s749':  [('deprel', 3, 'iobj')],
    'test-s775':  [('deprel', 14, 'iobj')],
    'test-s789':  [('deprel', 7, 'iobj')],

    # ताज को गौरव मिला: ताज(dative)→iobj:
    'test-s856':  [('deprel', 1, 'iobj')],

    'test-s986':  [('deprel', 7, 'iobj')],

    # भाजपा ने सरकार को बरखास्त करने की माँग की:
    # reparent सरकार under करने as obj:
    'test-s1002': [('parent', 8, 11), ('deprel', 8, 'obj')],

    'test-s1658': [('deprel', 1, 'iobj')],
}

# ── Apply fixes ──────────────────────────────────────────────────────────────

files = {
    'train': os.path.expanduser('hi_hdtb-ud-train.conllu'),
    'dev':   os.path.expanduser('hi_hdtb-ud-dev.conllu'),
    'test':  os.path.expanduser('hi_hdtb-ud-test.conllu'),
}

docs = {split: udapi.Document(path) for split, path in files.items()}

def find_tree(doc, sid):
    for bundle in doc.bundles:
        for tree in bundle.trees:
            if tree.sent_id == sid:
                return tree
    return None

applied = 0
missed  = 0

for sent_id, ops in FIXES.items():
    split = sent_id.split('-')[0]          # 'train', 'dev', or 'test'
    doc   = docs[split]
    tree  = find_tree(doc, sent_id)

    if tree is None:
        print(f"WARNING: sentence not found: {sent_id}")
        missed += 1
        continue

    nodes = {n.ord: n for n in tree.descendants}

    for op in ops:
        if op[0] == 'deprel':
            _, node_ord, new_deprel = op
            if node_ord not in nodes:
                print(f"WARNING: node {node_ord} not in {sent_id}")
                continue
            nodes[node_ord].deprel = new_deprel

        elif op[0] == 'parent':
            _, node_ord, new_parent_ord = op
            if node_ord not in nodes or new_parent_ord not in nodes:
                print(f"WARNING: reparent op references missing node in {sent_id}")
                continue
            nodes[node_ord].parent = nodes[new_parent_ord]

        else:
            print(f"WARNING: unknown op type '{op[0]}' in {sent_id}")

    applied += 1

print(f"\nApplied fixes to {applied} sentences ({missed} not found).")

# ── Save ─────────────────────────────────────────────────────────────────────
for split, path in files.items():
    docs[split].store_conllu(path)
    print(f"Saved {path}")
